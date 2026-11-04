import torch


print("=== GPU Computation Test ===")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print("Selected device:", device)

if device.type == "cuda":
    print("GPU:", torch.cuda.get_device_name(0))

    a = torch.tensor([1, 2, 3], device=device)
    b = torch.tensor([4, 5, 6], device=device)

    result = a + b

    print("Tensor A:", a)
    print("Tensor B:", b)
    print("A + B:", result)

    print("Tensor device:", result.device)

    print("\nGPU computation successful.")
else:
    print("CUDA is not available.")