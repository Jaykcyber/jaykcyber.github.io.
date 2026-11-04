import os
import sys
import json
import torch
import pandas as pd

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)
sys.path.insert(0, PROJECT_ROOT)

from src.models.model_factory import create_model
from experiments.evaluate_robustness import (
    RobustnessDataset,
    DEVICE,
    CHECKPOINTS,
    DATASETS,
    CONDITIONS,
    BATCH_SIZE
)

from torch.utils.data import DataLoader
from sklearn.metrics import confusion_matrix, classification_report


OUTPUT_DIR = "experiments/evaluation/prediction_analysis"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def analyze(model, dataset_path, condition):

    dataset = RobustnessDataset(dataset_path, condition)

    loader = DataLoader(
        dataset,
        batch_size=BATCH_SIZE,
        shuffle=False,
        num_workers=0
    )

    records = []

    model.eval()

    with torch.inference_mode():

        for batch in loader:

            images = batch["image"].to(DEVICE)
            labels = batch["label"].tolist()
            generators = batch["generator"]

            outputs = model(images)
            probabilities = torch.softmax(outputs, dim=1)

            ai_probabilities = probabilities[:, 1].cpu().tolist()
            predictions = outputs.argmax(dim=1).cpu().tolist()

            for label, prediction, ai_probability, generator in zip(
                labels,
                predictions,
                ai_probabilities,
                generators
            ):

                records.append({
                    "true_label": int(label),
                    "predicted_label": int(prediction),
                    "ai_probability": float(ai_probability),
                    "real_probability": float(1.0 - ai_probability),
                    "generator": str(generator)
                })

    df = pd.DataFrame(records)

    labels = df["true_label"]
    predictions = df["predicted_label"]

    cm = confusion_matrix(
        labels,
        predictions,
        labels=[0, 1]
    )

    real = df[df["true_label"] == 0]
    ai = df[df["true_label"] == 1]

    summary = {
        "images": len(df),
        "confusion_matrix": cm.tolist(),
        "classification_report": classification_report(
            labels,
            predictions,
            labels=[0, 1],
            target_names=["REAL", "AI_GENERATED"],
            output_dict=True,
            zero_division=0
        ),
        "average_ai_probability_real": float(
            real["ai_probability"].mean()
        ),
        "average_ai_probability_ai": float(
            ai["ai_probability"].mean()
        ),
        "real_predicted_as_ai": int(
            ((df.true_label == 0) &
             (df.predicted_label == 1)).sum()
        ),
        "ai_predicted_as_real": int(
            ((df.true_label == 1) &
             (df.predicted_label == 0)).sum()
        )
    }

    return df, summary


def main():

    all_summaries = {}

    for model_name, checkpoint_path in CHECKPOINTS.items():

        print("\nMODEL:", model_name)

        checkpoint = torch.load(
            checkpoint_path,
            map_location="cpu",
            weights_only=False
        )

        model = create_model("efficientnet_b0")

        model.load_state_dict(
            checkpoint["model_state_dict"]
        )

        model.to(DEVICE)
        model.eval()

        for dataset_name, dataset_path in DATASETS.items():

            for condition in CONDITIONS:

                print(
                    "Analyzing:",
                    dataset_name,
                    condition
                )

                df, summary = analyze(
                    model,
                    dataset_path,
                    condition
                )

                key = f"{model_name}_{dataset_name}_{condition}"

                all_summaries[key] = summary

                df.to_csv(
                    os.path.join(
                        OUTPUT_DIR,
                        key + "_predictions.csv"
                    ),
                    index=False
                )

                print(
                    "False positives:",
                    summary["real_predicted_as_ai"]
                )

                print(
                    "False negatives:",
                    summary["ai_predicted_as_real"]
                )

                print(
                    "Average AI probability (REAL):",
                    round(
                        summary["average_ai_probability_real"],
                        4
                    )
                )

                print(
                    "Average AI probability (AI):",
                    round(
                        summary["average_ai_probability_ai"],
                        4
                    )
                )

        del model
        del checkpoint

        if DEVICE.type == "cuda":
            torch.cuda.empty_cache()

    with open(
        os.path.join(OUTPUT_DIR, "prediction_analysis.json"),
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(all_summaries, f, indent=4)

    print("\nANALYSIS COMPLETED")
    print("Output:", OUTPUT_DIR)


if __name__ == "__main__":
    main()

