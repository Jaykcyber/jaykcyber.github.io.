import torch
import torch.nn as nn


print("=== RealTrace AI — Binary Classification Basics ===")


# --------------------------------------------------
# 1. Create a tiny artificial dataset
# --------------------------------------------------

# Class 0: values near 0
class_0 = torch.tensor([
    [0.0],
    [0.1],
    [0.2],
    [0.3],
    [0.4]
])

# Class 1: values near 1
class_1 = torch.tensor([
    [0.6],
    [0.7],
    [0.8],
    [0.9],
    [1.0]
])


# Combine the data
x = torch.cat([class_0, class_1])


# Labels
# 0 = Class 0
# 1 = Class 1

y = torch.tensor([
    [0.0],
    [0.0],
    [0.0],
    [0.0],
    [0.0],
    [1.0],
    [1.0],
    [1.0],
    [1.0],
    [1.0]
])


# --------------------------------------------------
# 2. Create a neural network
# --------------------------------------------------

model = nn.Sequential(
    nn.Linear(1, 8),
    nn.ReLU(),
    nn.Linear(8, 1)
)


# --------------------------------------------------
# 3. Loss function
# --------------------------------------------------

loss_function = nn.BCEWithLogitsLoss()


# --------------------------------------------------
# 4. Optimizer
# --------------------------------------------------

optimizer = torch.optim.SGD(
    model.parameters(),
    lr=0.1
)


# --------------------------------------------------
# 5. Training
# --------------------------------------------------

for epoch in range(1000):

    # Forward pass
    logits = model(x)

    # Calculate loss
    loss = loss_function(logits, y)

    # Clear old gradients
    optimizer.zero_grad()

    # Backpropagation
    loss.backward()

    # Update weights
    optimizer.step()


# --------------------------------------------------
# 6. Test the model
# --------------------------------------------------

test_data = torch.tensor([
    [0.2],
    [0.8]
])

with torch.no_grad():

    test_logits = model(test_data)

    probabilities = torch.sigmoid(test_logits)

    predictions = (probabilities >= 0.5).float()


print("\nTraining completed.")

for i in range(len(test_data)):

    print(
        "Input:",
        test_data[i].item(),
        "| Probability of Class 1:",
        probabilities[i].item(),
        "| Prediction:",
        int(predictions[i].item())
    )