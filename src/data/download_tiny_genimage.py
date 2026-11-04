from datasets import load_dataset

DATASET_NAME = "TheKernel01/Tiny-GenImage"

print("Loading Tiny-GenImage...")

dataset = load_dataset(DATASET_NAME)

print(dataset)

print("\nTrain rows:", len(dataset["train"]))
print("Validation rows:", len(dataset["validation"]))

print("\nColumns:", dataset["train"].column_names)

print("\nLabel names:")
print(dataset["train"].features["label"].names)

print("\nGenerator names:")
print(dataset["train"].features["generator"].names)

print("\nTiny-GenImage ready.")