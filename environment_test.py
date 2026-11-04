import sys

import numpy
import pandas
import matplotlib
import PIL
import cv2


print("=== RealTrace AI Environment Test ===")

print("Python version:", sys.version.split()[0])
print("Python executable:", sys.executable)

print("NumPy version:", numpy.__version__)
print("Pandas version:", pandas.__version__)
print("Matplotlib version:", matplotlib.__version__)
print("Pillow version:", PIL.__version__)
print("OpenCV version:", cv2.__version__)

print("\nEnvironment test completed successfully.")