import torch
import torch.nn as nn


print("=== RealTrace AI — Tiny CNN ===")


# --------------------------------------------------
# 1. Create a tiny CNN
# --------------------------------------------------

class TinyCNN(nn.Module):

    def __init__(self):

        super().__init__()

        self.features = nn.Sequential(

            # First convolution
            nn.Conv2d(
                in_channels=1,
                out_channels=8,
                kernel_size=3,
                padding=1
            ),

            nn.ReLU(),

            nn.MaxPool2d(kernel_size=2),

            # Second convolution
            nn.Conv2d(
                in_channels=8,
                out_channels=16,
                kernel_size=3,
                padding=1
            ),

            nn.ReLU(),

            nn.MaxPool2d(kernel_size=2)
        )


        # For a 28x28 input:
        #
        # 28x28
        #   ↓ MaxPool
        # 14x14
        #   ↓ MaxPool
        # 7x7
        #
        # 16 feature maps × 7 × 7

        self.classifier = nn.Linear(
            16 * 7 * 7,
            2
        )


    def forward(self, x):

        x = self.features(x)

        print("Feature shape before flatten:", x.shape)

        x = torch.flatten(x, start_dim=1)

        print("Shape after flatten:", x.shape)

        x = self.classifier(x)

        return x


# --------------------------------------------------
# 2. Create the model
# --------------------------------------------------

model = TinyCNN()

print("\nModel:")
print(model)


# --------------------------------------------------
# 3. Create a dummy image
# --------------------------------------------------

image = torch.randn(
    1,
    1,
    28,
    28
)


print("\nInput image shape:")
print(image.shape)


# --------------------------------------------------
# 4. Perform a forward pass
# --------------------------------------------------

output = model(image)


print("\nOutput shape:")
print(output.shape)

print("\nRaw model output:")
print(output)