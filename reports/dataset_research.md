# RealTrace AI — Dataset Research

## Primary Dataset

GenImage

Official repository:
https://github.com/GenImage-Dataset/GenImage

Official project website:
https://genimage-dataset.github.io/

## Why GenImage?

GenImage is selected as the primary dataset because it provides:

- More than one million real/AI image pairs
- Multiple AI image generators
- Diffusion-based generators
- GAN-based generators
- Generator-specific subsets
- Cross-generator evaluation
- Degraded-image evaluation
- Real images corresponding to ImageNet categories

## Generators Identified

- Midjourney
- Stable Diffusion V1.4
- Stable Diffusion V1.5
- ADM
- GLIDE
- Wukong
- VQDM
- BigGAN

## Secondary Candidate

CIFAKE

CIFAKE contains real CIFAR-10 images and AI-generated images produced using Stable Diffusion 1.4.

It is useful for:

- initial experimentation
- baseline development
- debugging
- comparison

However, CIFAKE is not sufficient as the primary dataset because it does not provide the same multi-generator structure required for our generalization experiments.

## Dataset Strategy

GenImage will be the primary dataset.

CIFAKE may be used as an auxiliary dataset if required by the experiments.

## Experimental Requirements

The final project must support:

1. Standard train/validation/test evaluation
2. Cross-generator evaluation
3. Held-out generator evaluation
4. Unseen-generator evaluation
5. JPEG compression testing
6. Resizing testing
7. Noise/degradation testing
8. Frequency-domain analysis

## Important Dataset Rule

Do not randomly mix all generators into a single dataset and call the resulting test set an unseen-generator test.

Generator identity must be preserved.

## Dataset License

GenImage is provided under CC BY-NC-SA 4.0 with additional dataset terms.

The dataset is intended for non-commercial academic/research use.

The applicable dataset terms must be checked before redistribution or deployment.

## Current Decision

Primary dataset: GenImage

Secondary/auxiliary dataset: CIFAKE

Dataset acquisition: NOT STARTED

Dataset preprocessing: NOT STARTED

Experimental split: NOT FINALIZED