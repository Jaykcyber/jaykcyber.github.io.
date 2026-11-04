import torch
import torch.nn as nn


print("=== RealTrace AI — Neural Network Basics ===")

# Training data
x = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
y = torch.tensor([[2.0], [4.0], [6.0], [8.0]])


# Create a very simple neural network
model = nn.Linear(1, 1)

print("\nInitial model:")
print(model)


# Loss function
loss_function = nn.MSELoss()

# Optimizer
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)


# Training
for epoch in range(1000):

    # Forward pass
    prediction = model(x)

    # Calculate error
    loss = loss_function(prediction, y)

    # Clear previous gradients
    optimizer.zero_grad()

    # Backpropagation
    loss.backward()

    # Update weights
    optimizer.step()


print("\nTraining completed.")

print("Learned weight:", model.weight.item())
print("Learned bias:", model.bias.item())


# Test the model
test_input = torch.tensor([[5.0]])

prediction = model(test_input)

print("\nInput:", test_input.item())
print("Predicted output:", prediction.item())
print("Expected output:", 10.0)