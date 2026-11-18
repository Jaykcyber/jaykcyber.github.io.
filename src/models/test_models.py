import os
import sys
import torch

sys.path.append(
    os.path.abspath(".")
)

from src.models.model_factory import create_model


device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

print("Device:", device)

models = [
    "baseline",
    "resnet18",
    "efficientnet_b0",
    "vit_b16",
]

dummy = torch.randn(
    2,
    3,
    224,
    224
).to(device)


for name in models:

    print("\nTesting:", name)

    model = create_model(name).to(device)

    model.eval()

    with torch.no_grad():
        output = model(dummy)

    print("Output shape:", output.shape)

    del model

    if torch.cuda.is_available():
        torch.cuda.empty_cache()


print("\nAll model tests completed.")