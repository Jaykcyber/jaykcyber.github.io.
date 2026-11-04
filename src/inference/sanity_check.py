import os
import sys

from datasets import load_from_disk

sys.path.append(os.path.abspath("."))

from src.inference.analyze_image import analyze_image


CHECKPOINT = "checkpoints/efficientnet_b0_best.pt"
DATASET_PATH = "data/processed/test_seen"

dataset = load_from_disk(DATASET_PATH)

real_correct = 0
real_total = 0

ai_correct = 0
ai_total = 0


print("Running inference sanity check...\n")


for item in dataset:

    label = item["label"]

    # Test only first 20 from each class
    if label == 0 and real_total >= 20:
        continue

    if label == 1 and ai_total >= 20:
        continue

    result = analyze_image(
        item["image"],
        CHECKPOINT
    )

    predicted_label = (
        0
        if result["prediction"] == "REAL"
        else 1
    )

    if label == 0:

        real_total += 1

        if predicted_label == 0:
            real_correct += 1

    else:

        ai_total += 1

        if predicted_label == 1:
            ai_correct += 1


    print(
        "Actual:",
        "REAL" if label == 0 else "AI",
        "| Predicted:",
        result["prediction"],
        "| AI probability:",
        f"{result['ai_probability']:.4f}"
    )


    if real_total >= 20 and ai_total >= 20:
        break


print("\n===== SANITY CHECK =====")

print(
    "Real correct:",
    real_correct,
    "/",
    real_total
)

print(
    "AI correct:",
    ai_correct,
    "/",
    ai_total
)