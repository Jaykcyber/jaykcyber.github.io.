import numpy as np

from pytorch_grad_cam import GradCAM
from pytorch_grad_cam.utils.image import show_cam_on_image
from pytorch_grad_cam.utils.model_targets import ClassifierOutputTarget


def get_target_layer(model, model_name):

    if model_name == "baseline":
        # Last convolution layer of BaselineCNN
        return model.features[-4]

    if model_name == "resnet18":
        return model.layer4[-1]

    if model_name == "efficientnet_b0":
        return model.features[-1]

    raise ValueError(
        f"Grad-CAM target layer not configured for: {model_name}"
    )


def generate_gradcam(
    model,
    model_name,
    input_tensor,
    original_rgb_float,
    target_class
):

    target_layer = get_target_layer(
        model,
        model_name
    )

    targets = [
        ClassifierOutputTarget(
            target_class
        )
    ]

    with GradCAM(
        model=model,
        target_layers=[target_layer]
    ) as cam:

        grayscale_cam = cam(
            input_tensor=input_tensor,
            targets=targets
        )[0]

    overlay = show_cam_on_image(
        original_rgb_float,
        grayscale_cam,
        use_rgb=True
    )

    return (
        grayscale_cam,
        overlay
    )