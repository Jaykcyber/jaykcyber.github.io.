import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader


print("=== RealTrace AI — Training a Tiny CNN ===")


# ==================================================
# 1. Create artificial image data
# ==================================================

torch.manual_seed(42)


num_samples_per_class = 100


# ------------------------------------------
# Class 0: vertical pattern
# ------------------------------------------

class_0 = torch.zeros(
    num_samples_per_class,
    1,
    28,
    28
)

class_0[:, :, :, 6:10] = 1.0
class_0[:, :, :, 18:22] = 1.0


# ------------------------------------------
# Class 1: horizontal pattern
# ------------------------------------------

class_1 = torch.zeros(
    num_samples_per_class,
    1,
    28,
    28
)

class_1[:, :, 6:10, :] = 1.0
class_1[:, :, 18:22, :] = 1.0


# ==================================================
# 2. Combine the classes
# ==================================================

x = torch.cat(
    [class_0, class_1],
    dim=0
)


# Labels:
# 0 = vertical
# 1 = horizontal

y = torch.cat(
    [
        torch.zeros(num_samples_per_class),
        torch.ones(num_samples_per_class)
    ]
).long()


print("\nDataset shape:")
print(x.shape)

print("Labels shape:")
print(y.shape)


# ==================================================
# 3. Create PyTorch Dataset
# ==================================================

dataset = TensorDataset(x, y)


# ==================================================
# 4. Create DataLoader
# ==================================================

dataloader = DataLoader(
    dataset,
    batch_size=16,
    shuffle=True
)


# ==================================================
# 5. Define CNN
# ==================================================

class TinyCNN(nn.Module):

    def __init__(self):

        super().__init__()

        self.features = nn.Sequential(

            nn.Conv2d(
                in_channels=1,
                out_channels=8,
                kernel_size=3,
                padding=1
            ),

            nn.ReLU(),

            nn.MaxPool2d(2),

            nn.Conv2d(
                in_channels=8,
                out_channels=16,
                kernel_size=3,
                padding=1
            ),

            nn.ReLU(),

            nn.MaxPool2d(2)
        )

        self.classifier = nn.Linear(
            16 * 7 * 7,
            2
        )


    def forward(self, x):

        x = self.features(x)

        x = torch.flatten(
            x,
            start_dim=1
        )

        x = self.classifier(x)

        return x


# ==================================================
# 6. Create model
# ==================================================

model = TinyCNN()


# ==================================================
# 7. Loss function
# ==================================================

loss_function = nn.CrossEntropyLoss()


# ==================================================
# 8. Optimizer
# ==================================================

optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)


# ==================================================
# 9. Training
# ==================================================

num_epochs = 10


for epoch in range(num_epochs):

    model.train()

    total_loss = 0.0
    correct = 0
    total = 0


    for images, labels in dataloader:

        # Forward pass
        outputs = model(images)


        # Calculate loss
        loss = loss_function(
            outputs,
            labels
        )


        # Clear old gradients
        optimizer.zero_grad()


        # Backpropagation
        loss.backward()


        # Update weights
        optimizer.step()


        # Track loss
        total_loss += loss.item()


        # Calculate predictions
        predictions = torch.argmax(
            outputs,
            dim=1
        )


        # Count correct predictions
        correct += (
            predictions == labels
        ).sum().item()


        total += labels.size(0)


    accuracy = 100 * correct / total


    print(
        f"Epoch [{epoch + 1}/{num_epochs}] "
        f"Loss: {total_loss:.4f} "
        f"Accuracy: {accuracy:.2f}%"
    )


# ==================================================
# 10. Final message
# ==================================================

print("\nTraining completed.")