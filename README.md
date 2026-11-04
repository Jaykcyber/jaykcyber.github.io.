# 🔍 RealTrace AI

### A Generalizable Forensic Intelligence Framework for Authenticity Verification of AI-Generated Visual Content

[🌐 **View Project**](https://realtrace-ai.streamlit.app/)

---

## 📌 Overview

**RealTrace AI** is an AI-powered forensic intelligence framework designed to analyze visual content and determine whether an image is **real or AI-generated**.

The project focuses not only on image classification but also on **generalization, robustness, explainability, and digital forensic analysis**.

RealTrace AI combines deep-learning-based detection with **cross-generator evaluation, degradation robustness testing, Grad-CAM explainability, FFT/DCT frequency-domain analysis, and automated forensic reporting** through an interactive Streamlit web application.

> **Note:** RealTrace AI is intended as a forensic decision-support system. Its predictions and visualizations should be treated as supporting evidence rather than definitive proof of image authenticity.

---

## 🌐 Live Application

The deployed RealTrace AI application can be accessed here:

### [🚀 View RealTrace AI](https://realtrace-ai.streamlit.app/)

Users can upload an image and receive:

- Real vs AI-generated prediction
- Model confidence score
- Real and AI-generated probabilities
- Grad-CAM visualization
- FFT frequency-domain visualization
- DCT frequency-domain visualization
- Downloadable forensic PDF report

---

## ✨ Key Features

### 🤖 AI-Generated Image Detection

RealTrace AI performs binary classification between:

- **REAL**
- **AI_GENERATED**

Multiple deep-learning architectures are implemented and evaluated.

### 🧠 Multiple Detection Models

The project includes:

- Baseline CNN
- ResNet18
- EfficientNet-B0
- Generalization-focused EfficientNet-B0

This allows comparison between a custom convolutional baseline and pretrained transfer-learning architectures.

### 🔄 Cross-Generator Generalization

The framework evaluates whether a detector trained using images from known generators can identify AI-generated images produced by generators that were not included during training.

A held-out generator evaluation strategy is used to study this behavior.

### 🛡️ Robustness Evaluation

RealTrace AI evaluates detector performance after common image transformations and degradations, including:

- JPEG compression
- Image resizing
- Gaussian noise
- Gaussian blur

This helps determine whether detection performance remains stable when images are modified.

### 🔬 Frequency-Domain Forensics

RealTrace AI provides two frequency-domain representations:

**Fast Fourier Transform (FFT)**  
Used to visualize the spatial-frequency characteristics of the uploaded image.

**Discrete Cosine Transform (DCT)**  
Used to inspect frequency-domain characteristics commonly relevant to image processing and compression analysis.

These representations are provided as **forensic visualizations** and are not treated as definitive evidence that an image is AI-generated.

### 🔥 Grad-CAM Explainability

Grad-CAM is integrated to visualize regions that contributed strongly to the model's prediction.

> Grad-CAM indicates image regions that contributed strongly to the model prediction. Highlighted regions should not be interpreted as definitive proof that a particular region is fake.

### 📄 Automated Forensic Report

Users can download a PDF report containing:

- Classification result
- Confidence score
- Model information
- Real probability
- AI-generated probability
- Original image
- Grad-CAM visualization
- FFT visualization
- DCT visualization
- Forensic interpretation disclaimer

---

## 🏗️ System Architecture

```text
                       ┌─────────────────────┐
                       │    Input Image      │
                       └──────────┬──────────┘
                                  │
                                  ▼
                       ┌─────────────────────┐
                       │   Preprocessing     │
                       │ Resize / Normalize  │
                       └──────────┬──────────┘
                                  │
                                  ▼
                ┌────────────────────────────────┐
                │    Deep Learning Detector      │
                │                                │
                │ Baseline CNN                   │
                │ ResNet18                       │
                │ EfficientNet-B0                │
                └───────────────┬────────────────┘
                                │
                    ┌───────────┼───────────┐
                    │           │           │
                    ▼           ▼           ▼
              Prediction     Grad-CAM    Forensics
              Confidence                  FFT / DCT
                    │           │           │
                    └───────────┼───────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │   Streamlit UI      │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │ Forensic PDF Report │
                     └─────────────────────┘
```

---

## 🧰 Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Deep Learning | PyTorch |
| Computer Vision | TorchVision |
| User Interface | Streamlit |
| Dataset Processing | Hugging Face Datasets |
| Image Processing | Pillow |
| Numerical Processing | NumPy |
| Frequency Analysis | SciPy |
| Machine Learning Metrics | Scikit-learn |
| Data Processing | Pandas |
| Explainable AI | Grad-CAM |
| Report Generation | ReportLab |
| Version Control | Git & GitHub |
| GPU Acceleration | NVIDIA CUDA |
| Deployment | Streamlit Community Cloud |

---

## 📊 Dataset

The primary dataset used in the project is **Tiny-GenImage**.

It contains real images and AI-generated images originating from multiple generative-model families.

Generators represented include:

- ADM
- BigGAN
- GLIDE
- Midjourney
- Stable Diffusion 1.4
- Stable Diffusion 1.5
- VQDM
- Wukong

For unseen-generator evaluation, **Wukong is held out from training** and used as an unseen generator during testing.

A supplementary modern-generator dataset is also used for generalization experiments, containing images from sources including:

- SDXL
- Stable Diffusion 3
- DALL-E 3
- Midjourney v6

Large datasets are **not stored directly in this GitHub repository**.

---

## 📈 Evaluation Metrics

RealTrace AI evaluates model performance using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

The project performs several categories of evaluation:

### Seen-Generator Evaluation

Tests performance on generator distributions represented during model development.

### Unseen-Generator Evaluation

Tests the ability of the detector to generalize to a held-out AI generator.

### Cross-Generator Evaluation

Measures performance separately across different AI image generators.

### Robustness Evaluation

Measures model behavior after image degradations such as JPEG compression, resizing, Gaussian noise, and Gaussian blur.

---

## 📁 Project Structure

```text
RealTrace-AI/
│
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
│   ├── training/
│   ├── evaluation/
│   ├── cross_generator/
│   └── robustness/
│
├── checkpoints/
├── scripts/
├── reports/
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd RealTrace-AI
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with the URL of this repository.

---

## 2. Create a Virtual Environment

### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Model Checkpoints

Trained model checkpoints are not committed directly to the repository when their size makes standard Git storage impractical.

Make sure the required checkpoint is available inside:

```text
checkpoints/
```

The application may use checkpoints such as:

```text
baseline_best.pt
resnet18_best.pt
efficientnet_b0_best.pt
efficientnet_b0_generalized.pt
```

---

# ▶️ Running RealTrace AI

Start the Streamlit application from the project root:

```bash
streamlit run app/app.py
```

Streamlit will provide a local address, typically:

```text
http://localhost:8501
```

Open it in your browser to use RealTrace AI.

---

## 🖥️ Application Workflow

```text
Upload Image
     ↓
Select Detection Model
     ↓
Analyze Image
     ↓
Real / AI-Generated Prediction
     ↓
Confidence & Probabilities
     ↓
Grad-CAM Explanation
     ↓
FFT + DCT Forensic Analysis
     ↓
Download PDF Forensic Report
```

---

## ⚠️ Limitations

AI-generated image detection remains an evolving research problem.

RealTrace AI may encounter difficulties when analyzing:

- Images from previously unseen generators
- Highly photorealistic AI-generated images
- Images heavily modified after generation
- Images from newer generation models
- Images whose distributions differ substantially from the training data

A high confidence score does **not** guarantee that a prediction is correct.

RealTrace AI therefore presents model predictions, Grad-CAM, FFT, and DCT information as **supporting forensic evidence rather than definitive proof of authenticity**.

---

## 🎓 Project Information

**Project Title:**  
RealTrace AI: A Generalizable Forensic Intelligence Framework for Authenticity Verification of AI-Generated Visual Content

**Domain:**  
Artificial Intelligence / Machine Learning / Computer Vision / Digital Forensics / Cybersecurity / Image Processing

**Project Type:**  
B.Tech Computer Science Engineering ( CyberSecurity )Final-Year Project

---

## 👥 Team Members

RealTrace AI was developed as a B.Tech Computer Science Engineering (Cybersecurity) Final-Year Project by:

| Team Member |
|---|
| **Durgjeet Kataria** |
| **Jay Kumar** |
| **Ankur Tetarwal** |
| **Gaurav Singh Solanki** |

## 🔮 Future Scope

Potential future improvements include:

- Training with additional modern image generators
- Stronger cross-generator generalization
- Additional degradation-aware training
- Compound image degradation evaluation
- Global structural feature learning
- Improved confidence calibration
- Expanded forensic analysis
- Video and deepfake detection
- Larger real-world benchmark evaluation

---

## 🌐 Deployment

The project is deployed using **Streamlit Community Cloud**.

### [🚀 View Live Project](https://realtrace-ai.streamlit.app/)

---

## 📜 Disclaimer

RealTrace AI is developed for **academic, research, and digital-forensics experimentation**.

Predictions generated by the system should not be treated as conclusive evidence regarding the authenticity or origin of an image.

Grad-CAM indicates regions that contributed strongly to the model's prediction. FFT and DCT representations provide frequency-domain information. None of these outputs individually constitute definitive forensic proof.

---

## ⭐ RealTrace AI

If you find this project useful, consider giving the repository a ⭐.

### [🌐 View Project](https://realtrace-ai.streamlit.app/)
