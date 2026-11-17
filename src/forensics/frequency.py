import cv2
import numpy as np

from scipy.fftpack import dct
from PIL import Image


def prepare_grayscale(image):

    if isinstance(
        image,
        Image.Image
    ):

        image = np.array(
            image.convert("RGB")
        )

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_RGB2GRAY
    )

    return gray.astype(
        np.float32
    )


def compute_fft(image):

    gray = prepare_grayscale(
        image
    )

    fft = np.fft.fft2(
        gray
    )

    shifted = np.fft.fftshift(
        fft
    )

    magnitude = np.log1p(
        np.abs(
            shifted
        )
    )

    magnitude = (
        magnitude -
        magnitude.min()
    )

    max_value = (
        magnitude.max()
    )

    if max_value > 0:

        magnitude = (
            magnitude /
            max_value
        )

    return magnitude


def compute_dct(image):

    gray = prepare_grayscale(
        image
    )

    dct_rows = dct(
        gray,
        axis=0,
        norm="ortho"
    )

    dct_result = dct(
        dct_rows,
        axis=1,
        norm="ortho"
    )

    magnitude = np.log1p(
        np.abs(
            dct_result
        )
    )

    magnitude = (
        magnitude -
        magnitude.min()
    )

    max_value = (
        magnitude.max()
    )

    if max_value > 0:

        magnitude = (
            magnitude /
            max_value
        )

    return magnitude