from src.models.baseline_cnn import BaselineCNN

from src.models.transfer_models import (
    get_resnet18,
    get_efficientnet_b0,
    get_vit_b16,
)


def create_model(model_name):

    if model_name == "baseline":
        return BaselineCNN()

    if model_name == "resnet18":
        return get_resnet18()

    if model_name == "efficientnet_b0":
        return get_efficientnet_b0()

    if model_name == "vit_b16":
        return get_vit_b16()

    raise ValueError(
        f"Unsupported model: {model_name}"
    )