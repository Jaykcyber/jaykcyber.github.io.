import io

import matplotlib.pyplot as plt

from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas


def array_to_png_buffer(array, cmap=None):

    buffer = io.BytesIO()

    plt.figure(figsize=(5, 5))

    if cmap:
        plt.imshow(array, cmap=cmap)
    else:
        plt.imshow(array)

    plt.axis("off")
    plt.tight_layout()

    plt.savefig(
        buffer,
        format="png",
        bbox_inches="tight"
    )

    plt.close()

    buffer.seek(0)

    return buffer


def generate_report(original_image, result):

    output = io.BytesIO()

    c = canvas.Canvas(
        output,
        pagesize=A4
    )

    width, height = A4

    y = height - 50

    # --------------------------------
    # TITLE
    # --------------------------------

    c.setFont(
        "Helvetica-Bold",
        18
    )

    c.drawString(
        50,
        y,
        "RealTrace AI Forensic Analysis Report"
    )

    y -= 40

    # --------------------------------
    # PREDICTION INFORMATION
    # --------------------------------

    c.setFont(
        "Helvetica-Bold",
        12
    )

    c.drawString(
        50,
        y,
        "Analysis Result"
    )

    y -= 25

    c.setFont(
        "Helvetica",
        11
    )

    c.drawString(
        50,
        y,
        f"Prediction: {result['prediction']}"
    )

    y -= 20

    c.drawString(
        50,
        y,
        f"Confidence: {result['confidence'] * 100:.2f}%"
    )

    y -= 20

    c.drawString(
        50,
        y,
        f"Model: {result['model_name']}"
    )

    y -= 20

    c.drawString(
        50,
        y,
        f"Real probability: {result['real_probability'] * 100:.2f}%"
    )

    y -= 20

    c.drawString(
        50,
        y,
        f"AI-generated probability: {result['ai_probability'] * 100:.2f}%"
    )

    y -= 40

    # --------------------------------
    # ORIGINAL IMAGE
    # --------------------------------

    c.setFont(
        "Helvetica-Bold",
        11
    )

    c.drawString(
        50,
        y,
        "Uploaded Image"
    )

    c.drawString(
        300,
        y,
        "Grad-CAM"
    )

    y -= 190

    original_buffer = io.BytesIO()

    original_image.convert("RGB").save(
        original_buffer,
        format="PNG"
    )

    original_buffer.seek(0)

    c.drawImage(
        ImageReader(original_buffer),
        50,
        y,
        width=200,
        height=170,
        preserveAspectRatio=True,
        anchor="c"
    )

    # --------------------------------
    # GRAD-CAM
    # --------------------------------

    gradcam_buffer = array_to_png_buffer(
        result["gradcam_overlay"]
    )

    c.drawImage(
        ImageReader(gradcam_buffer),
        300,
        y,
        width=200,
        height=170,
        preserveAspectRatio=True
    )

    y -= 35

    c.setFont(
        "Helvetica",
        8
    )

    c.drawString(
        50,
        y,
        "Grad-CAM indicates image regions that contributed strongly to the model prediction."
    )

    y -= 40

    # --------------------------------
    # FREQUENCY ANALYSIS
    # --------------------------------

    c.setFont(
        "Helvetica-Bold",
        11
    )

    c.drawString(
        50,
        y,
        "FFT Magnitude Spectrum"
    )

    c.drawString(
        300,
        y,
        "DCT Magnitude Spectrum"
    )

    y -= 190

    fft_buffer = array_to_png_buffer(
        result["fft"],
        cmap="gray"
    )

    dct_buffer = array_to_png_buffer(
        result["dct"],
        cmap="gray"
    )

    c.drawImage(
        ImageReader(fft_buffer),
        50,
        y,
        width=200,
        height=170,
        preserveAspectRatio=True
    )

    c.drawImage(
        ImageReader(dct_buffer),
        300,
        y,
        width=200,
        height=170,
        preserveAspectRatio=True
    )

    y -= 35

    # --------------------------------
    # DISCLAIMER
    # --------------------------------

    c.setFont(
        "Helvetica-Oblique",
        8
    )

    c.drawString(
        50,
        y,
        "RealTrace AI provides model-based forensic analysis."
    )

    y -= 12

    c.drawString(
        50,
        y,
        "Predictions, Grad-CAM regions, FFT and DCT representations are not definitive forensic proof."
    )

    c.save()

    output.seek(0)

    return output