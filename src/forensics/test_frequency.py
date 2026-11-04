import os
import sys

import matplotlib.pyplot as plt

from datasets import load_from_disk

sys.path.append(
    os.path.abspath(".")
)

from src.forensics.frequency import (
    compute_fft,
    compute_dct,
)


dataset = load_from_disk(
    "data/processed/test_seen"
)

image = dataset[0]["image"]

fft_image = compute_fft(
    image
)

dct_image = compute_dct(
    image
)


plt.figure()

plt.imshow(
    fft_image,
    cmap="gray"
)

plt.title(
    "FFT Magnitude Spectrum"
)

plt.axis(
    "off"
)

plt.savefig(
    "experiments/fft_test.png",
    bbox_inches="tight"
)

plt.close()


plt.figure()

plt.imshow(
    dct_image,
    cmap="gray"
)

plt.title(
    "DCT Magnitude Spectrum"
)

plt.axis(
    "off"
)

plt.savefig(
    "experiments/dct_test.png",
    bbox_inches="tight"
)

plt.close()


print(
    "FFT and DCT tests completed."
)