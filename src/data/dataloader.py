from datasets import load_from_disk
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms


class RealTraceDataset(Dataset):

    def __init__(self, dataset_path, train=False):

        self.dataset = load_from_disk(dataset_path)

        if train:
            self.transform = transforms.Compose([
                transforms.Resize((224, 224)),
                transforms.RandomHorizontalFlip(),
                transforms.RandomResizedCrop(
                    224,
                    scale=(0.8, 1.0)
                ),
                transforms.ToTensor(),
                transforms.Normalize(
                    mean=[0.485, 0.456, 0.406],
                    std=[0.229, 0.224, 0.225]
                )
            ])
        else:
            self.transform = transforms.Compose([
                transforms.Resize((224, 224)),
                transforms.ToTensor(),
                transforms.Normalize(
                    mean=[0.485, 0.456, 0.406],
                    std=[0.229, 0.224, 0.225]
                )
            ])

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, index):

        item = self.dataset[index]

        image = item["image"].convert("RGB")
        image = self.transform(image)

        return {
            "image": image,
            "label": item["label"],
            "generator": item["generator"]
        }


def create_loader(
    path,
    batch_size=16,
    shuffle=False,
    train=False
):

    dataset = RealTraceDataset(
        path,
        train=train
    )

    return DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=shuffle,
        num_workers=0,
        pin_memory=True
    )


if __name__ == "__main__":

    loader = create_loader(
        "data/processed/train_seen",
        batch_size=4,
        shuffle=True,
        train=True
    )

    batch = next(iter(loader))

    print("Images:", batch["image"].shape)
    print("Labels:", batch["label"])
    print("Generators:", batch["generator"])