import argparse
import json
import os
import sys

import torch
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)

sys.path.append(os.path.abspath("."))

from datasets import load_from_disk
from torch.utils.data import DataLoader

from src.data.dataloader import RealTraceDataset
from src.models.model_factory import create_model


def load_model(checkpoint_path, device):

    checkpoint = torch.load(
        checkpoint_path,
        map_location=device,
        weights_only=False
    )

    model = create_model(
        checkpoint["model_name"]
    )

    model.load_state_dict(
        checkpoint["model_state_dict"]
    )

    model.to(device)
    model.eval()

    return model, checkpoint


def evaluate_generator(
    model,
    dataset_path,
    generator_id,
    generator_name,
    device,
    batch_size
):

    hf_dataset = load_from_disk(
        dataset_path
    )

    real_dataset = hf_dataset.filter(
        lambda x: x["label"] == 0
    )

    generator_dataset = hf_dataset.filter(
        lambda x:
            x["generator"] == generator_id
            and x["label"] == 1
    )

    # Keep equal number of real and AI samples
    n = min(
        len(real_dataset),
        len(generator_dataset)
    )

    if n == 0:
        return None

    real_dataset = real_dataset.select(
        range(n)
    )

    generator_dataset = generator_dataset.select(
        range(n)
    )

    from datasets import concatenate_datasets

    combined = concatenate_datasets([
        real_dataset,
        generator_dataset
    ])

    temp_path = (
        f"data/processed/temp_{generator_name}"
    )

    if os.path.exists(temp_path):

        import shutil
        shutil.rmtree(temp_path)

    combined.save_to_disk(temp_path)

    dataset = RealTraceDataset(
        temp_path,
        train=False
    )

    loader = DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=False,
        num_workers=0
    )

    labels_all = []
    preds_all = []

    with torch.no_grad():

        for batch in loader:

            images = batch["image"].to(
                device
            )

            labels = batch["label"].to(
                device
            )

            outputs = model(images)

            preds = outputs.argmax(
                dim=1
            )

            labels_all.extend(
                labels.cpu().tolist()
            )

            preds_all.extend(
                preds.cpu().tolist()
            )

    result = {
        "generator": generator_name,
        "samples": len(labels_all),
        "accuracy": accuracy_score(
            labels_all,
            preds_all
        ),
        "precision": precision_score(
            labels_all,
            preds_all,
            zero_division=0
        ),
        "recall": recall_score(
            labels_all,
            preds_all,
            zero_division=0
        ),
        "f1": f1_score(
            labels_all,
            preds_all,
            zero_division=0
        ),
    }

    import shutil

    shutil.rmtree(
        temp_path,
        ignore_errors=True
    )

    return result


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--checkpoint",
        required=True
    )

    parser.add_argument(
        "--dataset",
        default="data/processed/test_seen"
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

    model, checkpoint = load_model(
        args.checkpoint,
        device
    )

    hf_dataset = load_from_disk(
        args.dataset
    )

    generator_names = (
        hf_dataset.features[
            "generator"
        ].names
    )

    results = []

    for generator_id, generator_name \
            in enumerate(generator_names):

        if generator_name == "Real":
            continue

        print(
            "\nEvaluating:",
            generator_name
        )

        result = evaluate_generator(
            model,
            args.dataset,
            generator_id,
            generator_name,
            device,
            args.batch_size
        )

        if result is not None:

            results.append(result)

            print(result)

    os.makedirs(
        "experiments/cross_generator",
        exist_ok=True
    )

    output_path = (
        "experiments/cross_generator/"
        f"{checkpoint['model_name']}.json"
    )

    with open(
        output_path,
        "w"
    ) as file:

        json.dump(
            results,
            file,
            indent=4
        )

    print(
        "\nSaved:",
        output_path
    )


if __name__ == "__main__":
    main()