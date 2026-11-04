from PIL import Image
import numpy as np
import torch


print("=== RealTrace AI — Dimensions & Normalization ===")

# Create a small RGB image
image = Image.new("RGB", (2, 2))

pixels = image.load()

pixels[0, 0] = (255, 0, 0)
pixels[1, 0] = (0, 128, 0)
pixels[0, 1] = (0, 0, 255)
pixels[1, 1] = (255, 255, 255)

# Convert to NumPy
image_array = np.array(image)

print("\nOriginal NumPy shape:")
print(image_array.shape)

print("\nOriginal pixel values:")
print(image_array)

# Convert HWC → CHW
image_chw = np.transpose(image_array, (2, 0, 1))

print("\nAfter HWC → CHW:")
print("Shape:", image_chw.shape)
print(image_chw)

# Convert to float
image_float = image_chw.astype(np.float32)

# Normalize 0–255 → 0–1
image_normalized = image_float / 255.0

print("\nNormalized values:")
print(image_normalized)

# Convert to PyTorch tensor
tensor = torch.from_numpy(image_normalized)

print("\nPyTorch tensor:")
print(tensor)

print("\nTensor shape:", tensor.shape)
print("Tensor dtype:", tensor.dtype)

if torch.cuda.is_available():
    tensor_gpu = tensor.to("cuda")

    print("\nTensor moved to:", tensor_gpu.device)
    print("GPU:", torch.cuda.get_device_name(0))