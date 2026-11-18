import os
import sys

# Add project root to Python import path
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)
sys.path.insert(0, PROJECT_ROOT)

import json
import torch
import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from datasets import load_from_disk

from src.models.model_factory import create_model

CHECKPOINTS = {
    "Original": "checkpoints/efficientnet_b0_best.pt",
    "Generalized": "checkpoints/efficientnet_b0_generalized.pt"
}

TEST_DATASETS = {
    "Seen": "data/processed/test_seen",
    "Unseen_Wukong": "data/processed/test_unseen_wukong"
}

OUTPUT_DIR = "experiments/evaluation/checkpoint_comparison"
os.makedirs(OUTPUT_DIR, exist_ok=True)

BATCH_SIZE = 8

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

class EvaluationDataset(Dataset):
    def __init__(self, path):
        self.data = load_from_disk(path)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        item = self.data[index]
        return (
            transform(item["image"].convert("RGB")),
            int(item["label"]),
            str(item["generator"])
        )

def evaluate(model, loader, device):
    y_true, y_pred, generators = [], [], []
    model.eval()

    with torch.inference_mode():
        for batch_index, (images, labels, gen) in enumerate(loader):
            images = images.to(device, non_blocking=True)

            with torch.autocast(
                device_type=device.type,
                dtype=torch.float16,
                enabled=device.type == "cuda"
            ):
                outputs = model(images)

            y_pred.extend(outputs.argmax(dim=1).cpu().tolist())
            y_true.extend(labels.tolist())
            generators.extend(gen)

            if (batch_index + 1) % 50 == 0:
                print(f"Processed {batch_index + 1}/{len(loader)} batches")

    return y_true, y_pred, generators

def calculate_metrics(y_true, y_pred):
    return {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "precision": float(precision_score(y_true, y_pred, zero_division=0)),
        "recall": float(recall_score(y_true, y_pred, zero_division=0)),
        "f1": float(f1_score(y_true, y_pred, zero_division=0)),
        "confusion_matrix": confusion_matrix(
            y_true, y_pred, labels=[0, 1]
        ).tolist()
    }

def main():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print("\nDevice:", device)

    results = {}
    generator_rows = []

    for dataset_name, dataset_path in TEST_DATASETS.items():
        print("\n" + "=" * 60)
        print("DATASET:", dataset_name)
        print("=" * 60)

        dataset = EvaluationDataset(dataset_path)

        loader = DataLoader(
            dataset,
            batch_size=BATCH_SIZE,
            shuffle=False,
            num_workers=0,
            pin_memory=device.type == "cuda"
        )

        results[dataset_name] = {}

        for model_name, checkpoint_path in CHECKPOINTS.items():
            print(f"\nEvaluating: {model_name}")

            checkpoint = torch.load(
                checkpoint_path,
                map_location="cpu",
                weights_only=False
            )

            model = create_model(checkpoint["model_name"])
            model.load_state_dict(checkpoint["model_state_dict"])
            model.to(device)

            y_true, y_pred, generators = evaluate(model, loader, device)
            metrics = calculate_metrics(y_true, y_pred)
            results[dataset_name][model_name] = metrics

            print(json.dumps(metrics, indent=4))
            print(classification_report(
                y_true, y_pred,
                target_names=["REAL", "AI_GENERATED"],
                zero_division=0
            ))

            frame = pd.DataFrame({
                "generator": generators,
                "true": y_true,
                "predicted": y_pred
            })

            for generator, group in frame.groupby("generator"):
                generator_rows.append({
                    "dataset": dataset_name,
                    "model": model_name,
                    "generator": generator,
                    "images": len(group),
                    "accuracy": float(
                        (group["true"] == group["predicted"]).mean()
                    )
                })

            del model
            if device.type == "cuda":
                torch.cuda.empty_cache()

    with open(os.path.join(OUTPUT_DIR, "comparison_metrics.json"), "w") as f:
        json.dump(results, f, indent=4)

    pd.DataFrame(generator_rows).to_csv(
        os.path.join(OUTPUT_DIR, "per_generator_metrics.csv"),
        index=False
    )

    summary = []
    for dataset_name, model_results in results.items():
        for model_name, metrics in model_results.items():
            summary.append({
                "dataset": dataset_name,
                "model": model_name,
                "accuracy": metrics["accuracy"],
                "precision": metrics["precision"],
                "recall": metrics["recall"],
                "f1": metrics["f1"]
            })

    summary_df = pd.DataFrame(summary)
    summary_df.to_csv(
        os.path.join(OUTPUT_DIR, "comparison_summary.csv"),
        index=False
    )

    print("\n========== FINAL COMPARISON ==========")
    print(summary_df.to_string(index=False))
    print("\nResults saved in:", OUTPUT_DIR)

if __name__ == "__main__":
    main()
