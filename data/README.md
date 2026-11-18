# RealTrace AI

**A Generalizable Forensic Intelligence Framework for Authenticity Verification of AI-Generated Visual Content**

RealTrace AI is a deep-learning and digital-forensics framework for classifying images as REAL or AI_GENERATED while evaluating cross-generator generalization, robustness, explainability, and frequency-domain characteristics.

## Features

- Binary Real vs AI-generated classification
- Baseline CNN
- ResNet18
- EfficientNet-B0
- Generalization-focused EfficientNet-B0
- Grad-CAM explainability
- FFT magnitude analysis
- DCT magnitude analysis
- Robustness evaluation
- Cross-generator testing
- Streamlit forensic dashboard
- Downloadable PDF forensic report

## Project Structure

https://github.com/DurgjeetKataria/RealTrace-AI.git
RealTrace-AI/
├── app/
│   └── app.py
│
├── src/
│   ├── data/
│   ├── models/
│   ├── training/
│   ├── evaluation/
│   ├── inference/
│   ├── explainability/
│   ├── forensics/
│   └── reporting/
│
├── experiments/
├── scripts/
├── checkpoints/
├── requirements.txt
├── .gitignore
└── README.md

## License

For academic and research use. Dataset and pretrained-model licenses remain subject to their respective original licenses.