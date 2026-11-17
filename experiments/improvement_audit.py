import os
from collections import Counter

import pandas as pd
import torch
from datasets import load_from_disk

print("\n========== CHECKPOINT AUDIT ==========")

for path in [
    "checkpoints/efficientnet_b0_best.pt",
    "checkpoints/efficientnet_b0_generalized.pt"
]:
    print(f"\n{path}")

    ckpt = torch.load(path, map_location="cpu", weights_only=False)

    for key in [
        "model_name", "epoch", "val_accuracy",
        "image_size", "training_stage", "base_checkpoint"
    ]:
        print(f"{key}: {ckpt.get(key, 'Not recorded')}")

print("\n========== MODERN DATASET AUDIT ==========")

csv_path = "data/processed/modern_supplement/metadata.csv"
df = pd.read_csv(csv_path)

print("Total images:", len(df))
print("\nGenerator counts:")
print(df["generator"].value_counts())

print("\nLabel counts:")
print(df["label"].value_counts().sort_index())

print("\nGenerator and label cross-check:")
print(pd.crosstab(df["generator"], df["label"]))

missing = sum(
    not os.path.isfile(
        os.path.join("data/processed/modern_supplement", p)
    )
    for p in df["image_path"]
)

print("\nMissing image files:", missing)

print("\n========== TEST DATASET AUDIT ==========")

for path in [
    "data/processed/test_seen",
    "data/processed/test_unseen_wukong"
]:
    print(f"\nDataset: {path}")

    ds = load_from_disk(path)

    print("Total images:", len(ds))
    print("Columns:", ds.column_names)

    if "label" in ds.column_names:
        print("Label counts:", Counter(map(int, ds["label"])))

    if "generator" in ds.column_names:
        print("Generator counts:", Counter(map(str, ds["generator"])))

print("\n========== AUDIT COMPLETE ==========")
