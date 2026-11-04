import argparse
import csv
import os
import sys

import torch
import torch.nn as nn
from tqdm import tqdm

sys.path.append(
    os.path.abspath(".")
)

from src.data.dataloader import create_loader
from src.models.model_factory import create_model


def evaluate(model, loader, device, criterion):

    model.eval()

    total = 0
    correct = 0
    total_loss = 0.0

    with torch.no_grad():

        for batch in loader:

            images = batch["image"].to(
                device,
                non_blocking=True
            )

            labels = batch["label"].to(
                device,
                non_blocking=True
            )

            outputs = model(images)

            loss = criterion(
                outputs,
                labels
            )

            total_loss += (
                loss.item() * labels.size(0)
            )

            predictions = outputs.argmax(dim=1)

            correct += (
                predictions == labels
            ).sum().item()

            total += labels.size(0)

    return (
        total_loss / total,
        correct / total
    )


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--model",
        choices=[
            "baseline",
            "resnet18",
            "efficientnet_b0",
            "vit_b16",
        ],
        required=True
    )

    parser.add_argument(
        "--epochs",
        type=int,
        default=5
    )

    parser.add_argument(
        "--batch-size",
        type=int,
        default=16
    )

    parser.add_argument(
        "--lr",
        type=float,
        default=0.0001
    )

    args = parser.parse_args()

    device = torch.device(
        "cuda"
        if torch.cuda.is_available()
        else "cpu"
    )

    print("Model:", args.model)
    print("Device:", device)
    print("Epochs:", args.epochs)
    print("Batch size:", args.batch_size)
    print("Learning rate:", args.lr)

    train_loader = create_loader(
        "data/processed/train_seen",
        batch_size=args.batch_size,
        shuffle=True,
        train=True
    )

    val_loader = create_loader(
        "data/processed/validation_seen",
        batch_size=args.batch_size,
        shuffle=False,
        train=False
    )

    model = create_model(
        args.model
    ).to(device)

    criterion = nn.CrossEntropyLoss()

    optimizer = torch.optim.AdamW(
        model.parameters(),
        lr=args.lr
    )

    os.makedirs(
        "checkpoints",
        exist_ok=True
    )

    os.makedirs(
        "experiments/training",
        exist_ok=True
    )

    history_path = (
        f"experiments/training/"
        f"{args.model}_history.csv"
    )

    with open(
        history_path,
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "epoch",
            "train_loss",
            "train_accuracy",
            "val_loss",
            "val_accuracy",
        ])

    best_val_accuracy = -1.0

    for epoch in range(1, args.epochs + 1):

        model.train()

        total = 0
        correct = 0
        total_loss = 0.0

        progress = tqdm(
            train_loader,
            desc=f"Epoch {epoch}/{args.epochs}"
        )

        for batch in progress:

            images = batch["image"].to(
                device,
                non_blocking=True
            )

            labels = batch["label"].to(
                device,
                non_blocking=True
            )

            optimizer.zero_grad()

            outputs = model(images)

            loss = criterion(
                outputs,
                labels
            )

            loss.backward()

            optimizer.step()

            total_loss += (
                loss.item() * labels.size(0)
            )

            predictions = outputs.argmax(
                dim=1
            )

            correct += (
                predictions == labels
            ).sum().item()

            total += labels.size(0)

            progress.set_postfix(
                loss=f"{loss.item():.4f}"
            )

        train_loss = total_loss / total
        train_accuracy = correct / total

        val_loss, val_accuracy = evaluate(
            model,
            val_loader,
            device,
            criterion
        )

        print(
            f"\nEpoch {epoch}: "
            f"train_loss={train_loss:.4f}, "
            f"train_acc={train_accuracy:.4f}, "
            f"val_loss={val_loss:.4f}, "
            f"val_acc={val_accuracy:.4f}"
        )

        with open(
            history_path,
            "a",
            newline=""
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                epoch,
                train_loss,
                train_accuracy,
                val_loss,
                val_accuracy,
            ])

        if val_accuracy > best_val_accuracy:

            best_val_accuracy = val_accuracy

            checkpoint_path = (
                f"checkpoints/"
                f"{args.model}_best.pt"
            )

            torch.save(
                {
                    "model_name": args.model,
                    "model_state_dict":
                        model.state_dict(),
                    "optimizer_state_dict":
                        optimizer.state_dict(),
                    "epoch": epoch,
                    "val_accuracy":
                        val_accuracy,
                    "image_size": 224,
                    "class_mapping": {
                        0: "REAL",
                        1: "AI_GENERATED",
                    }
                },
                checkpoint_path
            )

            print(
                "Saved best checkpoint:",
                checkpoint_path
            )

    print("\nTraining completed.")
    print(
        "Best validation accuracy:",
        best_val_accuracy
    )


if __name__ == "__main__":
    main()