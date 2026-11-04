import torch


print("=== RealTrace AI GPU Test ===")

print("PyTorch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())

if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))
    print("CUDA version used by PyTorch:", torch.version.cuda)
    print("GPU count:", torch.cuda.device_count())
else:
    print("CUDA is NOT available.")

print("GPU test completed.")