import argparse
import json
import os
import sys

import numpy as np
import torch

from PIL import Image, ImageFilter
from torchvision import transforms

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)

sys.path.append(
    os.path.abspath(".")
)

from datasets import load_from_disk
from src.models.model_factory import create_model


NORMALIZE = transforms.Normalize(
    mean=[0.485, 0.456, 0.406],
    std=[0.229, 0.224, 0.225]
)


def load_model(
    checkpoint_path,
    device
):

    checkpoint = torch.load(
        checkpoint_path,
        map_location=device,
        weights_only=False
    )

    model = create_model(
        checkpoint["model_name"]
    )

    model.load_state_dict(
        checkpoint[
            "model_state_dict"
        ]
    )

    model.to(device)
    model.eval()

    return model, checkpoint


def apply_degradation(
    image,
    mode
):

    image = image.convert("RGB")

    if mode == "original":

        return image


    if mode == "jpeg90":

        import io

        buffer = io.BytesIO()

        image.save(
            buffer,
            format="JPEG",
            quality=90
        )

        buffer.seek(0)

        return Image.open(
            buffer
        ).convert("RGB")


    if mode == "jpeg70":

        import io

        buffer = io.BytesIO()

        image.save(
            buffer,
            format="JPEG",
            quality=70
        )

        buffer.seek(0)

        return Image.open(
            buffer
        ).convert("RGB")


    if mode == "jpeg50":

        import io

        buffer = io.BytesIO()

        image.save(
            buffer,
            format="JPEG",
            quality=50
        )

        buffer.seek(0)

        return Image.open(
            buffer
        ).convert("RGB")


    if mode == "resize50":

        width, height = image.size

        image = image.resize(
            (
                max(1, width // 2),
                max(1, height // 2)
            )
        )

        return image


    if mode == "noise":

        array = np.array(
            image
        ).astype(
            np.float32
        )

        noise = np.random.normal(
            0,
            10,
            array.shape
        )

        array = np.clip(
            array + noise,
            0,
            255
        ).astype(
            np.uint8
        )

        return Image.fromarray(
            array
        )


    if mode == "blur":

        return image.filter(
            ImageFilter.GaussianBlur(
                radius=1.0
            )
        )


    raise ValueError(
        mode
    )


def preprocess(image):

    transform = transforms.Compose([
        transforms.Resize(
            (224, 224)
        ),
        transforms.ToTensor(),
        NORMALIZE
    ])

    return transform(image)


def evaluate(
    model,
    dataset,
    mode,
    device
):

    labels_all = []
    preds_all = []

    for index in range(
        len(dataset)
    ):

        item = dataset[index]

        image = apply_degradation(
            item["image"],
            mode
        )

        tensor = preprocess(
            image
        ).unsqueeze(0).to(
            device
        )

        label = item["label"]

        with torch.no_grad():

            output = model(
                tensor
            )

            prediction = (
                output.argmax(
                    dim=1
                ).item()
            )

        labels_all.append(
            label
        )

        preds_all.append(
            prediction
        )

    return {
        "accuracy":
            accuracy_score(
                labels_all,
                preds_all
            ),

        "precision":
            precision_score(
                labels_all,
                preds_all,
                zero_division=0
            ),

        "recall":
            recall_score(
                labels_all,
                preds_all,
                zero_division=0
            ),

        "f1":
            f1_score(
                labels_all,
                preds_all,
                zero_division=0
            )
    }


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--checkpoint",
        required=True
    )

    parser.add_argument(
        "--dataset",
        default=(
            "data/processed/"
            "test_seen"
        )
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

    dataset = load_from_disk(
        args.dataset
    )

    modes = [
        "original",
        "jpeg90",
        "jpeg70",
        "jpeg50",
        "resize50",
        "noise",
        "blur",
    ]

    results = {}

    for mode in modes:

        print(
            "\nTesting:",
            mode
        )

        result = evaluate(
            model,
            dataset,
            mode,
            device
        )

        results[mode] = result

        print(result)

    os.makedirs(
        "experiments/robustness",
        exist_ok=True
    )

    path = (
        "experiments/robustness/"
        f"{checkpoint['model_name']}.json"
    )

    with open(
        path,
        "w"
    ) as file:

        json.dump(
            results,
            file,
            indent=4
        )

    print(
        "\nSaved:",
        path
    )


if __name__ == "__main__":
    main()