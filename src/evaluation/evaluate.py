import argparse
import csv
import json
import os
import sys

import torch

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
)

sys.path.append(
    os.path.abspath(".")
)

from src.data.dataloader import create_loader
from src.models.model_factory import create_model


def load_model(
    checkpoint_path,
    device
):

    checkpoint = torch.load(
        checkpoint_path,
        map_location=device,
        weights_only=False
    )

    model_name = checkpoint["model_name"]

    model = create_model(
        model_name
    )

    model.load_state_dict(
        checkpoint["model_state_dict"]
    )

    model.to(device)

    model.eval()

    return model, checkpoint


def evaluate(
    model,
    loader,
    device
):

    all_labels = []
    all_predictions = []
    all_generators = []
    all_probabilities = []

    with torch.no_grad():

        for batch in loader:

            images = batch["image"].to(
                device,
                non_blocking=True
            )

            labels = batch["label"].to(
                device
            )

            outputs = model(images)

            probabilities = torch.softmax(
                outputs,
                dim=1
            )

            predictions = outputs.argmax(
                dim=1
            )

            all_labels.extend(
                labels.cpu().tolist()
            )

            all_predictions.extend(
                predictions.cpu().tolist()
            )

            all_probabilities.extend(
                probabilities[:, 1]
                .cpu()
                .tolist()
            )

            all_generators.extend(
                batch["generator"].tolist()
            )

    return (
        all_labels,
        all_predictions,
        all_probabilities,
        all_generators
    )


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--checkpoint",
        required=True
    )

    parser.add_argument(
        "--dataset",
        required=True
    )

    parser.add_argument(
        "--name",
        required=True
    )

    parser.add_argument(
        "--batch-size",
        type=int,
        default=16
    )

    args = parser.parse_args()

    device = torch.device(
        "cuda"
        if torch.cuda.is_available()
        else "cpu"
    )

    print("Device:", device)

    model, checkpoint = load_model(
        args.checkpoint,
        device
    )

    model_name = checkpoint["model_name"]

    print("Model:", model_name)
    print("Dataset:", args.dataset)

    loader = create_loader(
        args.dataset,
        batch_size=args.batch_size,
        shuffle=False,
        train=False
    )

    (
        labels,
        predictions,
        probabilities,
        generators
    ) = evaluate(
        model,
        loader,
        device
    )

    accuracy = accuracy_score(
        labels,
        predictions
    )

    precision = precision_score(
        labels,
        predictions,
        zero_division=0
    )

    recall = recall_score(
        labels,
        predictions,
        zero_division=0
    )

    f1 = f1_score(
        labels,
        predictions,
        zero_division=0
    )

    matrix = confusion_matrix(
        labels,
        predictions
    )

    report = classification_report(
        labels,
        predictions,
        target_names=[
            "REAL",
            "AI_GENERATED"
        ],
        zero_division=0
    )

    print("\n===== RESULTS =====")

    print(
        f"Accuracy:  {accuracy:.4f}"
    )

    print(
        f"Precision: {precision:.4f}"
    )

    print(
        f"Recall:    {recall:.4f}"
    )

    print(
        f"F1-score:  {f1:.4f}"
    )

    print("\nConfusion Matrix:")
    print(matrix)

    print("\nClassification Report:")
    print(report)

    os.makedirs(
        "experiments/evaluation",
        exist_ok=True
    )

    result = {
        "model": model_name,
        "dataset": args.name,
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "confusion_matrix":
            matrix.tolist()
    }

    json_path = (
        f"experiments/evaluation/"
        f"{model_name}_{args.name}.json"
    )

    with open(
        json_path,
        "w"
    ) as file:

        json.dump(
            result,
            file,
            indent=4
        )

    csv_path = (
        f"experiments/evaluation/"
        f"{model_name}_{args.name}"
        f"_predictions.csv"
    )

    with open(
        csv_path,
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "label",
            "prediction",
            "ai_probability",
            "generator"
        ])

        for row in zip(
            labels,
            predictions,
            probabilities,
            generators
        ):
            writer.writerow(row)

    print(
        "\nSaved:",
        json_path
    )

    print(
        "Saved:",
        csv_path
    )


if __name__ == "__main__":
    main()