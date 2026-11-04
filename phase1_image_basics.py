from PIL import Image
import numpy as np


print("=== RealTrace AI — Image Basics ===")

# Create a tiny 2 × 2 RGB image
image = Image.new("RGB", (2, 2))

# Get the pixels
pixels = image.load()

# Set individual pixels
pixels[0, 0] = (255, 0, 0)       # Red
pixels[1, 0] = (0, 255, 0)       # Green
pixels[0, 1] = (0, 0, 255)       # Blue
pixels[1, 1] = (255, 255, 255)    # White

# Convert the image into a NumPy array
image_array = np.array(image)

print("Image size:", image.size)
print("Array shape:", image_array.shape)
print("Array data:")
print(image_array)