import argparse
import os
import sys
import time

import pandas as pd
import torch
from datasets import load_from_disk
from PIL import Image
from sklearn.model_selection import train_test_split
from torch import nn
from torch.utils.data import Dataset, DataLoader, ConcatDataset
from torchvision import transforms

sys.path.append(os.path.abspath("."))

from src.models.model_factory import create_model


# ---------------------------------------------------------
# Paths
# ---------------------------------------------------------

OLD_TRAIN_PATH = "data/processed/train_seen"
OLD_VAL_PATH = "data/processed/validation_seen"

MODERN_ROOT = "data/processed/modern_supplement"
MODERN_CSV = os.path.join(
    MODERN_ROOT,
    "metadata.csv"
)

BASE_CHECKPOINT = "checkpoints/efficientnet_b0_best.pt"

OUTPUT_CHECKPOINT = (
    "checkpoints/efficientnet_b0_generalized.pt"
)

HISTORY_PATH = (
    "experiments/training/"
    "efficientnet_b0_generalized_history.csv"
)


# ---------------------------------------------------------
# Transforms
# ---------------------------------------------------------

TRAIN_TRANSFORM = transforms.Compose([
    transforms.Resize((256, 256)),

    transforms.RandomResizedCrop(
        224,
        scale=(0.8, 1.0)
    ),

    transforms.RandomHorizontalFlip(),

    transforms.ToTensor(),

    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])


EVAL_TRANSFORM = transforms.Compose([
    transforms.Resize((224, 224)),

    transforms.ToTensor(),

    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])


# ---------------------------------------------------------
# Tiny-GenImage Dataset Wrapper
# ---------------------------------------------------------

class TinyGenImageDataset(Dataset):

    def __init__(
        self,
        dataset,
        transform
    ):

        self.dataset = dataset
        self.transform = transform

    def __len__(self):

        return len(self.dataset)

    def __getitem__(self, index):

        sample = self.dataset[index]

        image = sample["image"].convert("RGB")

        label = int(
            sample["label"]
        )

        image = self.transform(
            image
        )

        return image, label


# ---------------------------------------------------------
# Modern Dataset Wrapper
# ---------------------------------------------------------

class ModernDataset(Dataset):

    def __init__(
        self,
        dataframe,
        root,
        transform
    ):

        self.dataframe = dataframe.reset_index(
            drop=True
        )

        self.root = root
        self.transform = transform

    def __len__(self):

        return len(
            self.dataframe
        )

    def __getitem__(self, index):

        row = self.dataframe.iloc[
            index
        ]

        relative_path = row[
            "image_path"
        ]

        # Handles Windows backslashes safely
        relative_path = relative_path.replace(
            "\\",
            os.sep
        ).replace(
            "/",
            os.sep
        )

        image_path = os.path.join(
            self.root,
            relative_path
        )

        image = Image.open(
            image_path
        ).convert("RGB")

        label = int(
            row["label"]
        )

        image = self.transform(
            image
        )

        return image, label


# ---------------------------------------------------------
# Accuracy helper
# ---------------------------------------------------------

def calculate_accuracy(
    correct,
    total
):

    if total == 0:
        return 0.0

    return correct / total


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--epochs",
        type=int,
        default=3
    )

    parser.add_argument(
        "--batch-size",
        type=int,
        default=16
    )

    parser.add_argument(
        "--lr",
        type=float,
        default=2e-5
    )

    args = parser.parse_args()

    os.makedirs(
        "checkpoints",
        exist_ok=True
    )

    os.makedirs(
        "experiments/training",
        exist_ok=True
    )

    device = torch.device(
        "cuda"
        if torch.cuda.is_available()
        else "cpu"
    )

    print(
        "\nDevice:",
        device
    )

    if torch.cuda.is_available():

        print(
            "GPU:",
            torch.cuda.get_device_name(0)
        )

    # -----------------------------------------------------
    # Load original datasets
    # -----------------------------------------------------

    print(
        "\nLoading Tiny-GenImage training dataset..."
    )

    old_train_hf = load_from_disk(
        OLD_TRAIN_PATH
    )

    old_val_hf = load_from_disk(
        OLD_VAL_PATH
    )

    print(
        "Original train:",
        len(old_train_hf)
    )

    print(
        "Original validation:",
        len(old_val_hf)
    )

    # -----------------------------------------------------
    # Load modern metadata
    # -----------------------------------------------------

    print(
        "\nLoading modern supplement metadata..."
    )

    modern_df = pd.read_csv(
        MODERN_CSV
    )

    print(
        "Modern total:",
        len(modern_df)
    )

    print(
        "\nModern generator counts:"
    )

    print(
        modern_df[
            "generator"
        ].value_counts()
    )

    # -----------------------------------------------------
    # Modern 90 / 10 split
    #
    # Stratify by generator so each source appears
    # proportionally in train and validation.
    # -----------------------------------------------------

    modern_train_df, modern_val_df = (
        train_test_split(
            modern_df,
            test_size=0.10,
            random_state=42,
            stratify=modern_df[
                "generator"
            ]
        )
    )

    print(
        "\nModern train:",
        len(modern_train_df)
    )

    print(
        "Modern validation:",
        len(modern_val_df)
    )

    # -----------------------------------------------------
    # Construct PyTorch datasets
    # -----------------------------------------------------

    old_train_dataset = (
        TinyGenImageDataset(
            old_train_hf,
            TRAIN_TRANSFORM
        )
    )

    old_val_dataset = (
        TinyGenImageDataset(
            old_val_hf,
            EVAL_TRANSFORM
        )
    )

    modern_train_dataset = ModernDataset(
        modern_train_df,
        MODERN_ROOT,
        TRAIN_TRANSFORM
    )

    modern_val_dataset = ModernDataset(
        modern_val_df,
        MODERN_ROOT,
        EVAL_TRANSFORM
    )

    # -----------------------------------------------------
    # Mixed datasets
    # -----------------------------------------------------

    train_dataset = ConcatDataset([
        old_train_dataset,
        modern_train_dataset
    ])

    validation_dataset = ConcatDataset([
        old_val_dataset,
        modern_val_dataset
    ])

    print(
        "\n=============================="
    )

    print(
        "MIXED DATASET"
    )

    print(
        "=============================="
    )

    print(
        "Training:",
        len(train_dataset)
    )

    print(
        "Validation:",
        len(validation_dataset)
    )

    # -----------------------------------------------------
    # DataLoaders
    # -----------------------------------------------------

    train_loader = DataLoader(
        train_dataset,
        batch_size=args.batch_size,
        shuffle=True,
        num_workers=0,
        pin_memory=True
    )

    validation_loader = DataLoader(
        validation_dataset,
        batch_size=args.batch_size,
        shuffle=False,
        num_workers=0,
        pin_memory=True
    )

    # -----------------------------------------------------
    # Load original EfficientNet checkpoint
    # -----------------------------------------------------

    print(
        "\nLoading original EfficientNet checkpoint..."
    )

    checkpoint = torch.load(
        BASE_CHECKPOINT,
        map_location=device,
        weights_only=False
    )

    model_name = checkpoint[
        "model_name"
    ]

    print(
        "Base model:",
        model_name
    )

    model = create_model(
        model_name
    )

    model.load_state_dict(
        checkpoint[
            "model_state_dict"
        ]
    )

    model = model.to(
        device
    )

    # -----------------------------------------------------
    # Loss / optimizer
    # -----------------------------------------------------

    criterion = nn.CrossEntropyLoss()

    optimizer = torch.optim.AdamW(
        model.parameters(),
        lr=args.lr,
        weight_decay=1e-4
    )

    # Reduce LR if validation stops improving
    scheduler = (
        torch.optim.lr_scheduler.ReduceLROnPlateau(
            optimizer,
            mode="max",
            factor=0.5,
            patience=1
        )
    )

    # -----------------------------------------------------
    # AMP
    # -----------------------------------------------------

    use_amp = (
        device.type == "cuda"
    )

    scaler = torch.cuda.amp.GradScaler(
        enabled=use_amp
    )

    print(
        "\nMixed precision:",
        use_amp
    )

    print(
        "Learning rate:",
        args.lr
    )

    print(
        "Epochs:",
        args.epochs
    )

    print(
        "Batch size:",
        args.batch_size
    )

    # -----------------------------------------------------
    # Training
    # -----------------------------------------------------

    best_val_accuracy = 0.0

    history = []

    for epoch in range(
        1,
        args.epochs + 1
    ):

        epoch_start = time.time()

        print(
            "\n===================================="
        )

        print(
            f"EPOCH {epoch}/{args.epochs}"
        )

        print(
            "===================================="
        )

        # -------------------------------------------------
        # Training phase
        # -------------------------------------------------

        model.train()

        train_loss = 0.0
        train_correct = 0
        train_total = 0

        for batch_index, (
            images,
            labels
        ) in enumerate(
            train_loader,
            start=1
        ):

            images = images.to(
                device,
                non_blocking=True
            )

            labels = labels.to(
                device,
                non_blocking=True
            )

            optimizer.zero_grad(
                set_to_none=True
            )

            with torch.cuda.amp.autocast(
                enabled=use_amp
            ):

                outputs = model(
                    images
                )

                loss = criterion(
                    outputs,
                    labels
                )

            scaler.scale(
                loss
            ).backward()

            scaler.step(
                optimizer
            )

            scaler.update()

            train_loss += (
                loss.item()
                * images.size(0)
            )

            predictions = outputs.argmax(
                dim=1
            )

            train_correct += (
                predictions == labels
            ).sum().item()

            train_total += (
                labels.size(0)
            )

            if batch_index % 200 == 0:

                current_acc = (
                    train_correct
                    / train_total
                )

                print(
                    f"Batch "
                    f"{batch_index}/"
                    f"{len(train_loader)}"
                    f" | Loss: "
                    f"{loss.item():.4f}"
                    f" | Acc: "
                    f"{current_acc:.4f}"
                )

        train_loss /= train_total

        train_accuracy = (
            calculate_accuracy(
                train_correct,
                train_total
            )
        )

        # -------------------------------------------------
        # Validation phase
        # -------------------------------------------------

        model.eval()

        val_loss = 0.0
        val_correct = 0
        val_total = 0

        with torch.no_grad():

            for images, labels in validation_loader:

                images = images.to(
                    device,
                    non_blocking=True
                )

                labels = labels.to(
                    device,
                    non_blocking=True
                )

                with torch.cuda.amp.autocast(
                    enabled=use_amp
                ):

                    outputs = model(
                        images
                    )

                    loss = criterion(
                        outputs,
                        labels
                    )

                val_loss += (
                    loss.item()
                    * images.size(0)
                )

                predictions = outputs.argmax(
                    dim=1
                )

                val_correct += (
                    predictions == labels
                ).sum().item()

                val_total += (
                    labels.size(0)
                )

        val_loss /= val_total

        val_accuracy = (
            calculate_accuracy(
                val_correct,
                val_total
            )
        )

        scheduler.step(
            val_accuracy
        )

        elapsed = (
            time.time()
            - epoch_start
        )

        current_lr = optimizer.param_groups[
            0
        ]["lr"]

        print(
            "\nEpoch result:"
        )

        print(
            f"Train Loss:     "
            f"{train_loss:.4f}"
        )

        print(
            f"Train Accuracy: "
            f"{train_accuracy:.4f}"
        )

        print(
            f"Val Loss:       "
            f"{val_loss:.4f}"
        )

        print(
            f"Val Accuracy:   "
            f"{val_accuracy:.4f}"
        )

        print(
            f"Learning Rate:  "
            f"{current_lr:.8f}"
        )

        print(
            f"Time:           "
            f"{elapsed / 60:.2f} min"
        )

        history.append({
            "epoch": epoch,
            "train_loss": train_loss,
            "train_accuracy":
                train_accuracy,
            "val_loss": val_loss,
            "val_accuracy":
                val_accuracy,
            "learning_rate":
                current_lr
        })

        # -------------------------------------------------
        # Save best generalized model
        # -------------------------------------------------

        if (
            val_accuracy
            > best_val_accuracy
        ):

            best_val_accuracy = (
                val_accuracy
            )

            torch.save(
                {
                    "model_name":
                        model_name,

                    "model_state_dict":
                        model.state_dict(),

                    "optimizer_state_dict":
                        optimizer.state_dict(),

                    "epoch":
                        epoch,

                    "val_accuracy":
                        val_accuracy,

                    "image_size":
                        224,

                    "class_mapping": {
                        0: "REAL",
                        1: "AI_GENERATED"
                    },

                    "training_stage":
                        "generalization_finetuning",

                    "base_checkpoint":
                        BASE_CHECKPOINT,

                    "modern_generators": [
                        "SDXL",
                        "SD3",
                        "DALLE3",
                        "MidjourneyV6"
                    ]
                },
                OUTPUT_CHECKPOINT
            )

            print(
                "\n✓ New best generalized "
                "checkpoint saved."
            )

    # -----------------------------------------------------
    # Save history
    # -----------------------------------------------------

    pd.DataFrame(
        history
    ).to_csv(
        HISTORY_PATH,
        index=False
    )

    print(
        "\n===================================="
    )

    print(
        "GENERALIZATION FINE-TUNING COMPLETE"
    )

    print(
        "===================================="
    )

    print(
        f"Best validation accuracy: "
        f"{best_val_accuracy:.4f}"
    )

    print(
        "Checkpoint:",
        OUTPUT_CHECKPOINT
    )

    print(
        "History:",
        HISTORY_PATH
    )


if __name__ == "__main__":
    main()