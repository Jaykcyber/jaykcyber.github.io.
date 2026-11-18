import torch.nn as nn

from torchvision.models import (
    resnet18,
    ResNet18_Weights,
    efficientnet_b0,
    EfficientNet_B0_Weights,
    vit_b_16,
    ViT_B_16_Weights,
)


def get_resnet18(num_classes=2):

    model = resnet18(
        weights=ResNet18_Weights.DEFAULT
    )

    model.fc = nn.Linear(
        model.fc.in_features,
        num_classes
    )

    return model


def get_efficientnet_b0(num_classes=2):

    model = efficientnet_b0(
        weights=EfficientNet_B0_Weights.DEFAULT
    )

    model.classifier[1] = nn.Linear(
        model.classifier[1].in_features,
        num_classes
    )

    return model


def get_vit_b16(num_classes=2):

    model = vit_b_16(
        weights=ViT_B_16_Weights.DEFAULT
    )

    model.heads.head = nn.Linear(
        model.heads.head.in_features,
        num_classes
    )

    return model