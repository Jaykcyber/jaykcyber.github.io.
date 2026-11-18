import os
import sys

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import io
import json
import time
import pandas as pd
import torch

from PIL import Image, ImageFilter
from datasets import load_from_disk
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

from src.models.model_factory import create_model


# ---------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
BATCH_SIZE = 8

CHECKPOINTS = {
    "Original": "checkpoints/efficientnet_b0_best.pt",
    "Generalized": "checkpoints/efficientnet_b0_generalized.pt",
    "Robust": "checkpoints/efficientnet_b0_robust.pt"
}

DATASETS = {
    "Seen": "data/processed/test_seen",
    "Unseen_Wukong": "data/processed/test_unseen_wukong"
}

OUTPUT_DIR = "experiments/evaluation/robustness_comparison"

os.makedirs(OUTPUT_DIR, exist_ok=True)

MEAN = [0.485, 0.456, 0.406]
STD = [0.229, 0.224, 0.225]

NORMALIZE = transforms.Normalize(MEAN, STD)
TO_TENSOR = transforms.ToTensor()

CONDITIONS = [
    "Clean",
    "JPEG_Q70",
    "Resize_Degradation",
    "Gaussian_Noise",
    "Gaussian_Blur"
]


# ---------------------------------------------------------
# DATASET WITH ROBUSTNESS TRANSFORMATIONS
# ---------------------------------------------------------

class RobustnessDataset(Dataset):

    def __init__(self, dataset_path, condition):

        self.dataset = load_from_disk(dataset_path)
        self.condition = condition

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, index):

        item = self.dataset[index]

        image = item["image"].convert("RGB")

        # Standard image size
        image = image.resize(
            (224, 224),
            Image.Resampling.BILINEAR
        )

        # 1. JPEG compression
        if self.condition == "JPEG_Q70":

            buffer = io.BytesIO()

            image.save(
                buffer,
                format="JPEG",
                quality=70
            )

            buffer.seek(0)
            image = Image.open(buffer).convert("RGB")

        # 2. Resize degradation
        elif self.condition == "Resize_Degradation":

            image = image.resize(
                (112, 112),
                Image.Resampling.BILINEAR
            )

            image = image.resize(
                (224, 224),
                Image.Resampling.BILINEAR
            )

        # 3. Gaussian blur
        elif self.condition == "Gaussian_Blur":

            image = image.filter(
                ImageFilter.GaussianBlur(radius=1.0)
            )

        image_tensor = TO_TENSOR(image)

        # 4. Gaussian noise
        if self.condition == "Gaussian_Noise":

            generator = torch.Generator().manual_seed(index + 12345)

            noise = torch.randn(
                image_tensor.shape,
                generator=generator
            ) * 0.03

            image_tensor = torch.clamp(
                image_tensor + noise,
                0.0,
                1.0
            )

        image_tensor = NORMALIZE(image_tensor)

        return {
            "image": image_tensor,
            "label": item["label"],
            "generator": item["generator"]
        }


# ---------------------------------------------------------
# METRICS
# ---------------------------------------------------------

def calculate_metrics(labels, predictions):

    return {
        "accuracy": accuracy_score(labels, predictions),
        "precision": precision_score(
            labels, predictions, zero_division=0
        ),
        "recall": recall_score(
            labels, predictions, zero_division=0
        ),
        "f1": f1_score(
            labels, predictions, zero_division=0
        ),
        "confusion_matrix": confusion_matrix(
            labels,
            predictions,
            labels=[0, 1]
        ).tolist()
    }


# ---------------------------------------------------------
# EVALUATION
# ---------------------------------------------------------

def evaluate_model(model, dataset_path, condition):

    dataset = RobustnessDataset(
        dataset_path,
        condition
    )

    loader = DataLoader(
        dataset,
        batch_size=BATCH_SIZE,
        shuffle=False,
        num_workers=0,
        pin_memory=(DEVICE.type == "cuda")
    )

    all_labels = []
    all_predictions = []
    generator_results = {}

    model.eval()

    with torch.inference_mode():

        for batch in loader:

            images = batch["image"].to(DEVICE)
            labels = batch["label"]

            outputs = model(images)

            predictions = torch.argmax(
                outputs,
                dim=1
            ).cpu().tolist()

            labels = labels.tolist()

            generators = batch["generator"]

            if torch.is_tensor(generators):
                generators = generators.tolist()

            all_labels.extend(labels)
            all_predictions.extend(predictions)

            for generator, label, prediction in zip(
                generators,
                labels,
                predictions
            ):

                generator = str(generator)

                if generator not in generator_results:

                    generator_results[generator] = {
                        "labels": [],
                        "predictions": []
                    }

                generator_results[generator]["labels"].append(label)
                generator_results[generator]["predictions"].append(
                    prediction
                )

    metrics = calculate_metrics(
        all_labels,
        all_predictions
    )

    per_generator = {}

    for generator, values in generator_results.items():

        gen_labels = values["labels"]
        gen_predictions = values["predictions"]

        per_generator[generator] = {
            "images": len(gen_labels),
            "accuracy": accuracy_score(
                gen_labels,
                gen_predictions
            )
        }

    return metrics, per_generator


# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------

def main():

    print("=" * 65)
    print("REALTRACE AI - ROBUSTNESS EVALUATION")
    print("=" * 65)

    print("Device:", DEVICE)

    if DEVICE.type == "cuda":
        print("GPU:", torch.cuda.get_device_name(0))

    results = {}
    summary_rows = []
    generator_rows = []

    start_time = time.time()

    for model_name, checkpoint_path in CHECKPOINTS.items():

        print("\n" + "=" * 65)
        print("LOADING MODEL:", model_name)
        print("=" * 65)

        if not os.path.exists(checkpoint_path):
            raise FileNotFoundError(checkpoint_path)

        checkpoint = torch.load(
            checkpoint_path,
            map_location="cpu",
            weights_only=False
        )

        model = create_model("efficientnet_b0")

        model.load_state_dict(
            checkpoint["model_state_dict"]
        )

        model = model.to(DEVICE)
        model.eval()

        results[model_name] = {}

        for dataset_name, dataset_path in DATASETS.items():

            print("\nDataset:", dataset_name)

            if not os.path.exists(dataset_path):
                raise FileNotFoundError(dataset_path)

            results[model_name][dataset_name] = {}

            for condition in CONDITIONS:

                print(
                    "\nEvaluating:",
                    model_name,
                    "|",
                    dataset_name,
                    "|",
                    condition
                )

                metrics, per_generator = evaluate_model(
                    model,
                    dataset_path,
                    condition
                )

                results[model_name][dataset_name][condition] = {
                    "metrics": metrics,
                    "per_generator": per_generator
                }

                print(
                    "Accuracy: {:.4f} | Precision: {:.4f} | "
                    "Recall: {:.4f} | F1: {:.4f}".format(
                        metrics["accuracy"],
                        metrics["precision"],
                        metrics["recall"],
                        metrics["f1"]
                    )
                )

                summary_rows.append({
                    "model": model_name,
                    "dataset": dataset_name,
                    "condition": condition,
                    "accuracy": metrics["accuracy"],
                    "precision": metrics["precision"],
                    "recall": metrics["recall"],
                    "f1": metrics["f1"]
                })

                for generator, values in per_generator.items():

                    generator_rows.append({
                        "model": model_name,
                        "dataset": dataset_name,
                        "condition": condition,
                        "generator": generator,
                        "images": values["images"],
                        "accuracy": values["accuracy"]
                    })

        del model
        del checkpoint

        if DEVICE.type == "cuda":
            torch.cuda.empty_cache()

    # -----------------------------------------------------
    # SAVE RESULTS
    # -----------------------------------------------------

    json_path = os.path.join(
        OUTPUT_DIR,
        "robustness_metrics.json"
    )

    csv_path = os.path.join(
        OUTPUT_DIR,
        "robustness_summary.csv"
    )

    generator_path = os.path.join(
        OUTPUT_DIR,
        "robustness_per_generator.csv"
    )

    with open(json_path, "w", encoding="utf-8") as file:
        json.dump(results, file, indent=4)

    pd.DataFrame(summary_rows).to_csv(
        csv_path,
        index=False
    )

    pd.DataFrame(generator_rows).to_csv(
        generator_path,
        index=False
    )

    elapsed = (time.time() - start_time) / 60

    print("\n" + "=" * 65)
    print("ROBUSTNESS EVALUATION COMPLETED")
    print("=" * 65)

    print("Time taken: {:.2f} minutes".format(elapsed))
    print("Results saved:")
    print(json_path)
    print(csv_path)
    print(generator_path)

    print("\nSUMMARY:")
    print(pd.DataFrame(summary_rows).to_string(index=False))


if __name__ == "__main__":
    main()


