import torch
import torch.nn as nn


print("=== RealTrace AI — Convolution Basics ===")


# --------------------------------------------------
# 1. Create a tiny grayscale image
# --------------------------------------------------

image = torch.tensor([
    [1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0]
])


# --------------------------------------------------
# 2. Convert it into CNN input format
# --------------------------------------------------

# PyTorch Conv2D expects:
# (batch, channels, height, width)

image = image.unsqueeze(0).unsqueeze(0)

print("\nInput shape:")
print(image.shape)


# --------------------------------------------------
# 3. Create a convolution layer
# --------------------------------------------------

conv = nn.Conv2d(
    in_channels=1,
    out_channels=1,
    kernel_size=3,
    stride=1,
    padding=1,
    bias=False
)


# --------------------------------------------------
# 4. Set a simple kernel manually
# --------------------------------------------------

kernel = torch.tensor([
    [-1.0, -1.0, -1.0],
    [ 0.0,  0.0,  0.0],
    [ 1.0,  1.0,  1.0]
])

conv.weight.data = kernel.unsqueeze(0).unsqueeze(0)


# --------------------------------------------------
# 5. Perform convolution
# --------------------------------------------------

feature_map = conv(image)


print("\nFeature map shape:")
print(feature_map.shape)

print("\nFeature map:")
print(feature_map)