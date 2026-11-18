# RealTrace AI — Dataset Decision

## Primary Dataset

GenImage

## Secondary Dataset

CIFAKE

## Primary Reason

GenImage provides the multi-generator structure required for the project's generalization and forensic evaluation objectives.

## Required Generator Categories

Diffusion-based:
- Stable Diffusion
- GLIDE
- VQDM
- ADM
- Wukong
- Midjourney

GAN-based:
- BigGAN

## Planned Evaluation

### Standard evaluation
Train/validation/test using the defined dataset split.

### Cross-generator evaluation
Train using selected generators and evaluate on another generator.

### Held-out generator evaluation
Exclude a generator from training and reserve it for evaluation.

### Unseen-generator evaluation
Evaluate on a generator that was not used during model training.

### Robustness evaluation
Apply:
- JPEG compression
- resizing
- noise
- other relevant degradations

## Current Status

Dataset selected.

Actual files have NOT been downloaded yet.

Experimental generator allocation has NOT been finalized.