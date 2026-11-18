import csv
import os
from collections import defaultdict

from datasets import load_dataset


DATASET_NAME = "Rajarshi-Roy-research/Defactify_Image_Dataset"

OUTPUT_ROOT = "data/processed/modern_supplement"
IMAGE_ROOT = os.path.join(OUTPUT_ROOT, "images")
CSV_PATH = os.path.join(OUTPUT_ROOT, "metadata.csv")


GENERATOR_NAMES = {
    0: "Defactify_Real",
    1: "SD21",
    2: "SDXL",
    3: "SD3",
    4: "DALLE3",
    5: "MidjourneyV6",
}


TARGET_COUNTS = {
    0: 4000,   # Real
    2: 1000,   # SDXL
    3: 1000,   # SD3
    4: 1000,   # DALL-E 3
    5: 1000,   # Midjourney v6
}


def main():

    os.makedirs(IMAGE_ROOT, exist_ok=True)

    # Create one directory per source
    for generator_id in TARGET_COUNTS:

        generator_name = GENERATOR_NAMES[generator_id]

        os.makedirs(
            os.path.join(
                IMAGE_ROOT,
                generator_name
            ),
            exist_ok=True
        )

    print("Loading Defactify in streaming mode...")

    dataset = load_dataset(
        DATASET_NAME,
        split="train",
        streaming=True
    )

    collected = defaultdict(int)

    total_target = sum(
        TARGET_COUNTS.values()
    )

    total_saved = 0

    print("\nTarget counts:")

    for generator_id, target in TARGET_COUNTS.items():

        print(
            f"{GENERATOR_NAMES[generator_id]}: {target}"
        )

    print(
        f"\nTotal target: {total_target}"
    )

    # Write metadata progressively too.
    with open(
        CSV_PATH,
        "w",
        newline="",
        encoding="utf-8"
    ) as csv_file:

        writer = csv.writer(csv_file)

        writer.writerow([
            "image_path",
            "label",
            "generator"
        ])

        for sample in dataset:

            generator_id = int(
                sample["Label_B"]
            )

            if generator_id not in TARGET_COUNTS:
                continue

            if (
                collected[generator_id]
                >= TARGET_COUNTS[generator_id]
            ):
                continue

            label = int(
                sample["Label_A"]
            )

            generator_name = (
                GENERATOR_NAMES[generator_id]
            )

            image = sample["Image"].convert(
                "RGB"
            )

            index = collected[generator_id]

            filename = (
                f"{generator_name}_{index:05d}.jpg"
            )

            relative_path = os.path.join(
                "images",
                generator_name,
                filename
            )

            absolute_path = os.path.join(
                OUTPUT_ROOT,
                relative_path
            )

            image.save(
                absolute_path,
                format="JPEG",
                quality=95
            )

            writer.writerow([
                relative_path,
                label,
                generator_name
            ])

            # Immediately discard image reference
            del image

            collected[generator_id] += 1
            total_saved += 1

            if total_saved % 250 == 0:

                print(
                    f"\nSaved {total_saved}/{total_target}"
                )

                for gid in TARGET_COUNTS:

                    print(
                        f"  {GENERATOR_NAMES[gid]}: "
                        f"{collected[gid]}/"
                        f"{TARGET_COUNTS[gid]}"
                    )

                # Ensure metadata is written progressively
                csv_file.flush()

            finished = all(
                collected[gid]
                >= TARGET_COUNTS[gid]
                for gid in TARGET_COUNTS
            )

            if finished:
                break

    print("\n==============================")
    print("COLLECTION COMPLETE")
    print("==============================")

    for generator_id in TARGET_COUNTS:

        print(
            f"{GENERATOR_NAMES[generator_id]}: "
            f"{collected[generator_id]} / "
            f"{TARGET_COUNTS[generator_id]}"
        )

    print(
        f"\nTotal saved: {total_saved}"
    )

    print(
        f"Metadata: {CSV_PATH}"
    )

    print(
        f"Images: {IMAGE_ROOT}"
    )

    if total_saved == total_target:

        print(
            "\nModern supplement created successfully."
        )

    else:

        print(
            "\nWARNING: Dataset collection was incomplete."
        )


if __name__ == "__main__":
    main()