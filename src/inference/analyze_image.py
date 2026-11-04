import os
import sys

import numpy as np
import torch

from PIL import Image
from torchvision import transforms

sys.path.append(
    os.path.abspath(".")
)

from src.models.model_factory import create_model
from src.explainability.gradcam_utils import generate_gradcam
from src.forensics.frequency import compute_fft, compute_dct


CLASS_NAMES = {
    0: "REAL",
    1: "AI_GENERATED"
}


TRANSFORM = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])


def load_checkpoint(
    checkpoint_path,
    device
):

    checkpoint = torch.load(
        checkpoint_path,
        map_location=device,
        weights_only=False
    )

    model_name = checkpoint["model_name"]

    model = create_model(
        model_name
    )

    model.load_state_dict(
        checkpoint["model_state_dict"]
    )

    model.to(device)
    model.eval()

    return model, model_name


def analyze_image(
    image,
    checkpoint_path
):

    device = torch.device(
        "cuda"
        if torch.cuda.is_available()
        else "cpu"
    )

    if not isinstance(
        image,
        Image.Image
    ):
        image = Image.open(image)

    image = image.convert("RGB")

    model, model_name = load_checkpoint(
        checkpoint_path,
        device
    )

    input_tensor = TRANSFORM(
        image
    ).unsqueeze(0).to(device)

    with torch.no_grad():

        logits = model(
            input_tensor
        )

        probabilities = torch.softmax(
            logits,
            dim=1
        )[0]

        predicted_class = int(
            torch.argmax(
                probabilities
            ).item()
        )

    confidence = float(
        probabilities[
            predicted_class
        ].item()
    )

    resized = image.resize(
        (224, 224)
    )

    rgb_float = (
        np.array(resized)
        .astype(np.float32)
        / 255.0
    )

    _, gradcam_overlay = generate_gradcam(
    model,
    model_name,
    input_tensor,
    rgb_float,
    predicted_class
)

    fft_image = compute_fft(
        image
    )

    dct_image = compute_dct(
        image
    )

    return {
        "prediction":
            CLASS_NAMES[
                predicted_class
            ],

        "confidence":
            confidence,

        "real_probability":
            float(
                probabilities[0]
                .item()
            ),

        "ai_probability":
            float(
                probabilities[1]
                .item()
            ),

        "model_name":
            model_name,

        "gradcam_overlay":
            gradcam_overlay,

        "fft":
            fft_image,

        "dct":
            dct_image
    }