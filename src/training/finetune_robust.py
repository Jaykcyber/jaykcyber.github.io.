import os
import sys
import time
import io
import random
import argparse
import pandas as pd
import torch

from PIL import Image, ImageFilter
from datasets import load_from_disk
from sklearn.model_selection import train_test_split
from torch import nn
from torch.utils.data import Dataset, DataLoader, ConcatDataset
from torchvision import transforms

sys.path.insert(0, os.path.abspath("."))

from src.models.model_factory import create_model


# Paths
OLD_TRAIN_PATH = "data/processed/train_seen"
OLD_VAL_PATH = "data/processed/validation_seen"

MODERN_ROOT = "data/processed/modern_supplement"
MODERN_CSV = os.path.join(MODERN_ROOT, "metadata.csv")

BASE_CHECKPOINT = "checkpoints/efficientnet_b0_generalized.pt"
OUTPUT_CHECKPOINT = "checkpoints/efficientnet_b0_robust.pt"

HISTORY_PATH = "experiments/training/efficientnet_b0_robust_history.csv"

MEAN = [0.485, 0.456, 0.406]
STD = [0.229, 0.224, 0.225]

to_tensor = transforms.ToTensor()
normalize = transforms.Normalize(MEAN, STD)


# Robustness augmentation
def robust_transform(image):

    image = image.resize((224, 224))

    if random.random() < 0.5:
        image = transforms.functional.hflip(image)

    # Apply one random corruption to some training images
    if random.random() < 0.70:

        corruption = random.choice([
            "jpeg",
            "blur",
            "resize",
            "noise"
        ])

        if corruption == "jpeg":
            quality = random.randint(40, 85)
            buffer = io.BytesIO()
            image.save(buffer, format="JPEG", quality=quality)
            buffer.seek(0)
            image = Image.open(buffer).convert("RGB")

        elif corruption == "blur":
            radius = random.uniform(0.5, 1.2)
            image = image.filter(
                ImageFilter.GaussianBlur(radius=radius)
            )

        elif corruption == "resize":
            small_size = random.choice([112, 160, 180])
            image = image.resize(
                (small_size, small_size),
                Image.Resampling.BILINEAR
            )
            image = image.resize(
                (224, 224),
                Image.Resampling.BILINEAR
            )

    tensor = to_tensor(image)

    if random.random() < 0.35:
        noise_std = random.uniform(0.01, 0.04)
        noise = torch.randn_like(tensor) * noise_std
        tensor = torch.clamp(tensor + noise, 0, 1)

    return normalize(tensor)


def eval_transform(image):
    image = image.resize((224, 224))
    return normalize(to_tensor(image))


class TinyDataset(Dataset):

    def __init__(self, dataset, training=False):
        self.dataset = dataset
        self.training = training

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, index):
        sample = self.dataset[index]
        image = sample["image"].convert("RGB")

        if self.training:
            image = robust_transform(image)
        else:
            image = eval_transform(image)

        return image, int(sample["label"])


class ModernDataset(Dataset):

    def __init__(self, dataframe, root, training=False):
        self.dataframe = dataframe.reset_index(drop=True)
        self.root = root
        self.training = training

    def __len__(self):
        return len(self.dataframe)

    def __getitem__(self, index):
        row = self.dataframe.iloc[index]

        relative_path = str(row["image_path"])
        relative_path = relative_path.replace("\\", os.sep)
        relative_path = relative_path.replace("/", os.sep)

        image_path = os.path.join(self.root, relative_path)

        with Image.open(image_path) as source:
            image = source.convert("RGB")

        if self.training:
            image = robust_transform(image)
        else:
            image = eval_transform(image)

        return image, int(row["label"])


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--epochs", type=int, default=2)
    parser.add_argument("--batch-size", type=int, default=8)
    parser.add_argument("--lr", type=float, default=5e-6)
    args = parser.parse_args()

    os.makedirs("checkpoints", exist_ok=True)
    os.makedirs("experiments/training", exist_ok=True)

    device = torch.device(
        "cuda" if torch.cuda.is_available() else "cpu"
    )

    print("\nDevice:", device)

    if device.type == "cuda":
        print("GPU:", torch.cuda.get_device_name(0))

    # Load datasets
    print("\nLoading datasets...")

    old_train = load_from_disk(OLD_TRAIN_PATH)
    old_val = load_from_disk(OLD_VAL_PATH)

    modern_df = pd.read_csv(MODERN_CSV)

    modern_train, modern_val = train_test_split(
        modern_df,
        test_size=0.10,
        random_state=42,
        stratify=modern_df["generator"]
    )

    train_dataset = ConcatDataset([
        TinyDataset(old_train, training=True),
        ModernDataset(modern_train, MODERN_ROOT, training=True)
    ])

    val_dataset = ConcatDataset([
        TinyDataset(old_val, training=False),
        ModernDataset(modern_val, MODERN_ROOT, training=False)
    ])

    print("Training images:", len(train_dataset))
    print("Validation images:", len(val_dataset))

    train_loader = DataLoader(
        train_dataset,
        batch_size=args.batch_size,
        shuffle=True,
        num_workers=0,
        pin_memory=(device.type == "cuda")
    )

    val_loader = DataLoader(
        val_dataset,
        batch_size=args.batch_size,
        shuffle=False,
        num_workers=0,
        pin_memory=(device.type == "cuda")
    )

    # Load generalized checkpoint
    print("\nLoading generalized EfficientNet-B0 checkpoint...")

    checkpoint = torch.load(
        BASE_CHECKPOINT,
        map_location=device,
        weights_only=False
    )

    model_name = checkpoint["model_name"]
    model = create_model(model_name)

    model.load_state_dict(checkpoint["model_state_dict"])
    model = model.to(device)

    criterion = nn.CrossEntropyLoss()

    optimizer = torch.optim.AdamW(
        model.parameters(),
        lr=args.lr,
        weight_decay=1e-4
    )

    scaler = torch.amp.GradScaler(
        "cuda",
        enabled=(device.type == "cuda")
    )

    use_amp = device.type == "cuda"

    best_val_accuracy = -1.0
    history = []

    print("\nStarting robustness-aware fine-tuning")
    print("Epochs:", args.epochs)
    print("Batch size:", args.batch_size)
    print("Learning rate:", args.lr)
    print("Mixed precision:", use_amp)

    for epoch in range(1, args.epochs + 1):

        start_time = time.time()

        # Training
        model.train()
        train_loss = 0.0
        train_correct = 0
        train_total = 0

        for batch_index, (images, labels) in enumerate(
            train_loader, start=1
        ):

            images = images.to(device, non_blocking=True)
            labels = labels.to(device, non_blocking=True)

            optimizer.zero_grad(set_to_none=True)

            with torch.autocast(
                device_type=device.type,
                enabled=use_amp
            ):
                outputs = model(images)
                loss = criterion(outputs, labels)

            scaler.scale(loss).backward()
            scaler.step(optimizer)
            scaler.update()

            train_loss += loss.item() * images.size(0)
            train_correct += (
                outputs.argmax(dim=1) == labels
            ).sum().item()
            train_total += labels.size(0)

            if batch_index % 200 == 0:
                print(
                    f"Epoch {epoch} | "
                    f"Batch {batch_index}/{len(train_loader)} | "
                    f"Loss: {loss.item():.4f}"
                )

        train_loss /= train_total
        train_accuracy = train_correct / train_total

        # Validation
        model.eval()
        val_loss = 0.0
        val_correct = 0
        val_total = 0

        with torch.no_grad():

            for images, labels in val_loader:

                images = images.to(device, non_blocking=True)
                labels = labels.to(device, non_blocking=True)

                with torch.autocast(
                    device_type=device.type,
                    enabled=use_amp
                ):
                    outputs = model(images)
                    loss = criterion(outputs, labels)

                val_loss += loss.item() * images.size(0)
                val_correct += (
                    outputs.argmax(dim=1) == labels
                ).sum().item()
                val_total += labels.size(0)

        val_loss /= val_total
        val_accuracy = val_correct / val_total

        elapsed = (time.time() - start_time) / 60

        print("\n========== EPOCH RESULT ==========")
        print(f"Epoch:          {epoch}/{args.epochs}")
        print(f"Train Loss:     {train_loss:.4f}")
        print(f"Train Accuracy: {train_accuracy:.4f}")
        print(f"Val Loss:       {val_loss:.4f}")
        print(f"Val Accuracy:   {val_accuracy:.4f}")
        print(f"Time:           {elapsed:.2f} minutes")

        history.append({
            "epoch": epoch,
            "train_loss": train_loss,
            "train_accuracy": train_accuracy,
            "val_loss": val_loss,
            "val_accuracy": val_accuracy
        })

        if val_accuracy > best_val_accuracy:

            best_val_accuracy = val_accuracy

            torch.save({
                "model_name": model_name,
                "model_state_dict": model.state_dict(),
                "optimizer_state_dict": optimizer.state_dict(),
                "epoch": epoch,
                "val_accuracy": val_accuracy,
                "image_size": 224,
                "class_mapping": {
                    0: "REAL",
                    1: "AI_GENERATED"
                },
                "training_stage": "robustness_aware_finetuning",
                "base_checkpoint": BASE_CHECKPOINT,
                "augmentations": [
                    "JPEG compression",
                    "Gaussian blur",
                    "Downsampling",
                    "Gaussian noise"
                ]
            }, OUTPUT_CHECKPOINT)

            print("\nBest improved checkpoint saved.")

    pd.DataFrame(history).to_csv(
        HISTORY_PATH,
        index=False
    )

    print("\n========== TRAINING COMPLETE ==========")
    print("Best validation accuracy:", best_val_accuracy)
    print("Checkpoint:", OUTPUT_CHECKPOINT)
    print("History:", HISTORY_PATH)


if __name__ == "__main__":
    main()
