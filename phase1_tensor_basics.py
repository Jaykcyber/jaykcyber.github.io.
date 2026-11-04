from PIL import Image
import numpy as np
import torch


print("=== RealTrace AI — Tensor Basics ===")

# Create a small RGB image
image = Image.new("RGB", (2, 2))

pixels = image.load()

pixels[0, 0] = (255, 0, 0)       # Red
pixels[1, 0] = (0, 255, 0)       # Green
pixels[0, 1] = (0, 0, 255)       # Blue
pixels[1, 1] = (255, 255, 255)   # White

# Convert image to NumPy array
image_array = np.array(image)

print("\nNumPy array:")
print(image_array)

print("\nNumPy shape:", image_array.shape)
print("NumPy data type:", image_array.dtype)


# Convert NumPy array to PyTorch tensor
tensor = torch.from_numpy(image_array)

print("\nPyTorch tensor:")
print(tensor)

print("\nTensor shape:", tensor.shape)
print("Tensor data type:", tensor.dtype)


# Check CUDA
if torch.cuda.is_available():

    device = torch.device("cuda")

    tensor_gpu = tensor.to(device)

    print("\nGPU is available.")
    print("Tensor device:", tensor_gpu.device)
    print("GPU:", torch.cuda.get_device_name(0))

else:

    print("\nCUDA is not available.")