from datasets import load_dataset, concatenate_datasets
from pathlib import Path
import shutil


DATASET_NAME = "TheKernel01/Tiny-GenImage"
HELD_OUT_GENERATOR_NAME = "Wukong"
SEED = 42


print("Loading Tiny-GenImage...")

dataset = load_dataset(DATASET_NAME)

train = dataset["train"]
official_validation = dataset["validation"]

generator_names = train.features["generator"].names

print("Generators:", generator_names)

held_out_id = generator_names.index(
    HELD_OUT_GENERATOR_NAME
)

real_id = generator_names.index("Real")

print("Real ID:", real_id)
print("Held-out Wukong ID:", held_out_id)


# ==================================================
# 1. TRAIN
# ==================================================
# Remove ALL Wukong images from training.

train_seen = train.filter(
    lambda row:
        row["generator"] != held_out_id
)


# ==================================================
# 2. SPLIT OFFICIAL VALIDATION
# ==================================================

split = official_validation.train_test_split(
    test_size=0.5,
    seed=SEED,
    stratify_by_column="generator"
)

validation_pool = split["train"]
test_pool = split["test"]


# ==================================================
# 3. VALIDATION
# ==================================================
# Validation must also exclude Wukong.

validation_seen = validation_pool.filter(
    lambda row:
        row["generator"] != held_out_id
)


# ==================================================
# 4. TEST POOL — REAL IMAGES
# ==================================================

real_test_pool = test_pool.filter(
    lambda row:
        row["generator"] == real_id
)

real_split = real_test_pool.train_test_split(
    test_size=0.5,
    seed=SEED
)

real_for_seen_test = real_split["train"]
real_for_unseen_test = real_split["test"]


# ==================================================
# 5. SEEN GENERATOR TEST
# ==================================================

seen_ai_test = test_pool.filter(
    lambda row:
        row["generator"] != held_out_id
        and row["generator"] != real_id
)

test_seen = concatenate_datasets([
    real_for_seen_test,
    seen_ai_test
])


# ==================================================
# 6. UNSEEN WUKONG TEST
# ==================================================

wukong_test = test_pool.filter(
    lambda row:
        row["generator"] == held_out_id
)

test_unseen_wukong = concatenate_datasets([
    real_for_unseen_test,
    wukong_test
])


# ==================================================
# 7. SAVE
# ==================================================

output_root = Path("data/processed")

if output_root.exists():
    shutil.rmtree(output_root)

output_root.mkdir(
    parents=True,
    exist_ok=True
)

train_seen.save_to_disk(
    output_root / "train_seen"
)

validation_seen.save_to_disk(
    output_root / "validation_seen"
)

test_seen.save_to_disk(
    output_root / "test_seen"
)

test_unseen_wukong.save_to_disk(
    output_root / "test_unseen_wukong"
)


# ==================================================
# 8. SUMMARY
# ==================================================

print("\n===== FINAL SPLIT SUMMARY =====")

print(
    "Train seen:",
    len(train_seen)
)

print(
    "Validation seen:",
    len(validation_seen)
)

print(
    "Seen-generator test:",
    len(test_seen)
)

print(
    "Unseen Wukong test:",
    len(test_unseen_wukong)
)

print("\nUnseen test labels:")
print(
    test_unseen_wukong["label"]
)

print("\nSplit creation complete.")