import os
import sys

from datasets import load_from_disk

sys.path.append(
    os.path.abspath(".")
)

from src.inference.analyze_image import analyze_image


dataset = load_from_disk(
    "data/processed/test_seen"
)

image = dataset[0]["image"]

result = analyze_image(
    image,
    "checkpoints/efficientnet_b0_best.pt"
)

print("Prediction:", result["prediction"])
print("Confidence:", result["confidence"])
print("Model:", result["model_name"])
print("Real probability:", result["real_probability"])
print("AI probability:", result["ai_probability"])