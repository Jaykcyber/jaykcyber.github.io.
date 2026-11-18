from datasets import load_dataset

DATASET_NAME = "Rajarshi-Roy-research/Defactify_Image_Dataset"

print("Loading only 10 samples...")

dataset = load_dataset(
    DATASET_NAME,
    split="train[:10]"
)

print("\nSUCCESS")
print(dataset)

print("\nColumns:")
print(dataset.column_names)

print("\nFeatures:")
print(dataset.features)

print("\nFirst sample metadata:")

sample = dataset[0]

for key in dataset.column_names:
    if key.lower() not in ["image", "img"]:
        print(key, ":", sample[key])

print("\nImage fields:")
for key in dataset.column_names:
    value = sample[key]
    if hasattr(value, "size"):
        print(key, ":", type(value), value.size)