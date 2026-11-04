import os

MODEL_DIR = "checkpoints"

os.makedirs(MODEL_DIR, exist_ok=True)

print("Model download setup is not configured yet.")
print("Expected model files:")

models = [
    "baseline_best.pt",
    "resnet18_best.pt",
    "efficientnet_b0_best.pt",
    "efficientnet_b0_generalized.pt",
]

for model in models:
    print("-", os.path.join(MODEL_DIR, model))

print(
    "\nUpload these checkpoints to Hugging Face or GitHub Releases, "
    "then add their download URLs to this script."
)