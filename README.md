# 🛡️ RealTrace AI

### An Institutional Cyber-Forensic Intelligence Framework & Real-Time Threat Detection Portal

> **Engineering College Ajmer Rajasthan** • Department of Computer Science & Engineering (Cybersecurity)  
> *Developed in alignment with Ministry of Electronics & IT (MeitY), C-DAC, and ISEA cybersecurity awareness initiatives.*

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live%20Portal-success?logo=github)](https://durgjeet.github.io/RealTrace-AI/)
[![ONNX Runtime Web](https://img.shields.io/badge/ONNX%20Runtime-WASM%201.14-blue?logo=onnx)](https://onnxruntime.ai/)
[![Client-Side Privacy](https://img.shields.io/badge/Privacy-100%25%20In--Browser-brightgreen?logo=shield)](detection.html)
[![National Helpline](https://img.shields.io/badge/Helpline-1930%20Golden%20Hour-red?logo=phone)](reporting.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)

---

## 📌 Project Overview

**RealTrace AI** is an advanced, dual-tier cyber-forensic intelligence platform designed to combat the rising wave of synthetic media threats, AI deepfakes, phishing scams, and digital extortion across India. 

The framework pairs **state-of-the-art deep learning models (Baseline CNN, EfficientNet-B0 Robust)** with an **institutional real-time cyber defense portal** inspired by CyberGuard. It empowers citizens, law enforcement, and digital forensic investigators to verify media authenticity, detect phishing and malicious links, report cybercrime to the national **1930** helpline, and search official nodal cyber police cells across all 36 Indian States and Union Territories.

### 🌟 Key Pillars

1. **100% In-Browser Edge Forensics**: Neural network inference runs completely on the user's browser via **ONNX Runtime Web (WASM)**. Zero images or user data are ever uploaded to an external server, guaranteeing strict evidentiary privacy.
2. **Multi-Domain Threat Defense**: Unifies AI image/video deepfake verification, SMS phishing classification, malicious URL inspection, and video manipulation analysis into a single consolidated suite.
3. **Public Cyber Literacy & Incident Assistance**: Features interactive cybersecurity quizzes with verifiable certificates, demographic cyber hygiene guidelines, real-world case studies, and an automated Indian cybercrime police complaint drafting engine.

---

## 🌐 The RealTrace AI Web Portal Suite

The web application is structured for direct, zero-configuration hosting on **GitHub Pages** (root `/`), featuring a unified crimson and navy institutional design:

```
RealTrace AI Suite
 │
 ├── 🏠 index.html          ── Flagship Home Portal (Carousel, Scam Ticker, Workflow)
 ├── 🔍 detection.html      ── Real-Time Threat & Deepfake Detection Suite
 ├── 📚 awareness.html      ── Cyber Hygiene, Quizzes, Certificates & 36 State Police Directory
 ├── 🚨 reporting.html      ── National 1930 Helpline, Golden Hour Protocol & FIR Drafting
 ├── 📊 dashboard.html      ── User Security Center & Threat Monitoring
 └── 🔐 login.html          ── Session Portal & Identity Verification (auth.js)
```

### 1. 🏠 Institutional Home (`index.html`)
* **Government & College Branding**: Features official crests for *Engineering College Ajmer*, C-DAC, and ISEA, with an active system monitor badge.
* **4-Banner Auto Carousel**: Interactive showcase highlighting neural verification, scam prevention, and national helplines.
* **Live Breaking Scam Ticker**: Real-time news ticker alerting users to emerging threats (e.g., Digital Arrest scams, courier APK trojans, AI voice clone extortion).
* **4-Stage Forensic Pipeline Visualizer**: Ingest $\rightarrow$ Convolutional Inference $\rightarrow$ Spectral Explainability $\rightarrow$ Certified PDF Dossier.
* **Emergency Helpline Bar**: Direct one-touch connection to **1930** (National Cyber Crime Reporting Helpline).

### 2. 🔍 Real-Time Detection Suite (`detection.html`)
A multi-layered AI detection hub containing 5 real-time tools:

* **Tool #1: AI Deepfake & Synthetic Media Forensic Studio (RealTrace AI Core)**:
  * **Dual-Model Inference Selector**:
    * **Baseline CNN (1.5 MB)**: Instant in-memory reference model (loads in $\sim$0.5s).
    * **EfficientNet-B0 Robust (16.0 MB)**: Trained with perturbation augmentations (JPEG compression, Gaussian noise, blur, resize) for resilient cross-generator generalization.
  * **One-Click Preloaded Test Samples**: Test instantly without uploading files using sample DSLR camera photos, Midjourney v6 fakes, or SDXL generative images.
  * **Grad-CAM Activation Heatmaps**: Microscopic convolutional feature activations visualized with adjustable alpha opacity and an interactive loupe magnifying lens.
  * **2D Frequency Domain Spectra**:
    * **2D Fast Fourier Transform (FFT)**: Highlights periodic spatial frequency discrepancies caused by generative upsampling layers.
    * **2D Discrete Cosine Transform (DCT)**: Visualizes energy distribution and high-frequency compression decay.
  * **Cryptographic Session Integrity**: Generates SHA-256 evidence digests, resolution metadata, and client-side timestamps.
  * **Certified PDF Export**: One-click generation of court- and incident-ready forensic dossiers via jsPDF.
* **Tool #2: SMS & Message Phishing Scanner**: Analyzes SMS/WhatsApp messages for urgency triggers, lottery lures, bank fraud keywords, and malicious links.
* **Tool #3: URL & Link Safety Scanner**: Deep inspection of domain strings, IP spoofing, suspicious TLDs, and SSL legitimacy.
* **Tool #4: Video Deepfake & Manipulation Analyzer (Demo Suite)**: Multi-frame temporal consistency scanner — extracts facial keyframes, evaluates inter-frame warping, blink rate biometrics, and lip-sync alignment.
* **Live Threat Alerts & Feed**: Real-time incident logs and threat advisories.

### 3. 📚 Cyber Awareness & State Police Directory (`awareness.html`)
* **Scam Stories**: Interactive case breakdowns of modern cyber fraud (Digital Arrest, Work-from-Home task scams, Electricity bill APK traps, Customs courier fraud).
* **Demographic Safety Manuals**: Dedicated cyber hygiene protocols for Kids, Teenagers, Adults, and Senior Citizens.
* **Interactive Cybersecurity Quizzes**: Beginner, Intermediate, and Advanced evaluation modules with dynamic scoring, instant explanations, and downloadable **Certificates of Achievement**.
* **36 States & UTs Cyber Police Directory**: Instant searchable registry of State Cyber Crime Police Stations, nodal officers, 24x7 phone numbers, addresses, and official state grievance portals across India.

### 4. 🚨 Incident Reporting & 1930 Protocol (`reporting.html`)
* **Golden Hour Guidance**: Step-by-step instructions for financial fraud recovery within the critical first 2 to 4 hours.
* **Formal Complaint Templates**: Downloadable guidelines for drafting bank freeze requests and formal police complaint letters.
* **Central Grievance Portals**: Direct routing to `cybercrime.gov.in`, `sancharsaathi.gov.in` (Chakshu), RBI Banking Ombudsman, and SEBI SCORES.

### 4. 🔐 Security Dashboard & Authentication (`dashboard.html`, `login.html`)
* Client-side session management ([`auth.js`](auth.js)) supporting user registration, personalized security metrics, and quiz score tracking.

---

## 🏗️ Technical Architecture

```text
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │                       REALTRACE AI ARCHITECTURE                             │
 └─────────────────────────────────────────────────────────────────────────────┘
                                       │
            ┌──────────────────────────┴──────────────────────────┐
            ▼                                                     ▼
┌──────────────────────────────┐              ┌──────────────────────────────┐
│   CLIENT-SIDE WEB SUITE      │              │    PYTORCH RESEARCH CORE     │
│   (HTML5, CSS3, ES6, WASM)   │              │     (Python, CUDA, Models)   │
├──────────────────────────────┤              ├──────────────────────────────┤
│ • ONNX Runtime Web (WASM)    │              │ • Baseline 4-Block CNN       │
│ • Dual Models (.onnx)        │              │ • Transfer ResNet18          │
│ • HTML5 Canvas 2D FFT & DCT  │              │ • EfficientNet-B0 Robust     │
│ • Interactive Grad-CAM Loupe │              │ • Held-Out Generator Tests   │
│ • jsPDF Report Dossier Engine│              │ • Perturbation Augmentations │
│ • Web Audio Synthesizer      │              │ • Streamlit Desktop UI       │
│ • 36 State Police Directory  │              │ • Training Checkpoints (.pt) │
└──────────────────────────────┘              └──────────────────────────────┘
            │                                                     │
            ▼                                                     ▼
┌──────────────────────────────┐              ┌──────────────────────────────┐
│  GitHub Pages Deployment     │              │  Streamlit Cloud / Local CLI │
│  ($0 Serverless Hosting)     │              │  (Deep Research Evaluation)  │
└──────────────────────────────┘              └──────────────────────────────┘
```

---

## 🔬 Deep Learning & Forensic Methodology

### 1. Supported Model Checkpoints
* **Baseline CNN** (`models/baseline.onnx` — 1.55 MB): A custom 4-stage convolutional neural network designed for rapid client-side edge inference ($\sim$30–50 ms).
* **EfficientNet-B0 Robust** (`models/efficientnet_b0_robust.onnx` — 16.03 MB): Pretrained on ImageNet and fine-tuned on multi-generator datasets with perturbation-resilient data augmentation (Gaussian noise, Gaussian blur, random JPEG quality compression $Q \in [40, 95]$, and random rescaling).

### 2. Multi-Generator Training & Testing Data
The research models are trained and benchmarked against generative models from multiple algorithmic families:
* **Diffusion Models**: Stable Diffusion v1.4, Stable Diffusion v1.5, SDXL, Glide, Wukong.
* **Autoregressive & GAN Models**: Midjourney, BigGAN, ADM, VQDM.
* **Unseen Generalization Benchmark**: **Wukong** was strictly held out from training splits to evaluate zero-shot detector generalization against unknown generative architectures.

### 3. Dual-Domain Explainability
* **Spatial Feature Attribution (Grad-CAM)**: Computes gradients of the target score with respect to the final convolutional feature maps, projecting an intensity heatmap onto suspect artifacts (unnatural skin textures, boundary seams, anatomically warped hands).
* **Frequency-Domain Artifact Detection (FFT & DCT)**: AI generative upsampling layers (transposed convolutions, latent bicubic interpolations) frequently introduce periodic grid artifacts in the 2D frequency spectrum. RealTrace AI renders both FFT magnitude and DCT energy spectra in real time.

---

## 📁 Repository Directory Structure

```text
RealTrace-AI/
│
├── .github/workflows/deploy.yml   # GitHub Actions workflow for root Pages deployment
├── .gitignore                     # Git ignore rules
├── .nojekyll                      # Prevents Jekyll from omitting model files
├── README.md                      # Comprehensive project documentation
├── requirements.txt               # Python ML & Streamlit dependencies
├── style.css                      # Unified CyberGuard + RealTrace stylesheet
│
├── index.html                     # Flagship institutional home portal
├── detection.html                 # 5-tool real-time detection & deepfake studio
├── awareness.html                 # Cyber awareness, quizzes & 36 State Police directory
├── reporting.html                 # 1930 emergency reporting workflow & guides
├── dashboard.html                 # User security dashboard
├── login.html                     # Authentication & registration portal
│
├── app.js                         # In-browser ONNX inference, Grad-CAM, FFT/DCT & jsPDF
├── auth.js                        # Client-side session and credentials manager
├── awareness.js                   # 36 States & UTs Police directory search logic
│
├── images/                        # Banners & institutional crests (College, C-DAC, ISEA)
│   ├── COLLEGE.jpg                # Engineering College Ajmer crest
│   ├── cdac_logo.jpg              # C-DAC official logo
│   ├── isea_logo.jpg              # ISEA official logo
│   ├── banner1.jpg                # Carousel Banner 1
│   ├── banner2.jpg                # Carousel Banner 2
│   ├── banner3.jpg                # Carousel Banner 3
│   └── banner4.jpg                # Carousel Banner 4
│
├── models/                        # In-browser neural models (ONNX format)
│   ├── baseline.onnx              # Baseline CNN (1.55 MB)
│   └── efficientnet_b0_robust.onnx# Robust Multi-Generator Detector (16.03 MB)
│
├── app/                           # Alternative Python Streamlit UI
│   └── app.py                     # Streamlit web app script
│
├── data/                          # Dataset schemas & external test images
│   ├── dataset_schema.csv
│   └── external_test/
│
├── experiments/                   # Evaluation results, robustness logs & training curves
│   ├── cross_generator/
│   ├── evaluation/
│   ├── robustness/
│   └── training/
│
├── reports/                       # Forensic research audit notes
│   ├── dataset_decision.md
│   └── dataset_research.md
│
└── src/                           # Python deep learning source code
    ├── data/                      # Dataset loaders & split generators
    ├── models/                    # PyTorch model definitions & factory
    ├── training/                  # Model training & fine-tuning routines
    ├── evaluation/                # Cross-generator & robustness evaluators
    ├── explainability/            # Grad-CAM PyTorch utilities
    ├── forensics/                 # Frequency-domain spectral transforms
    └── reporting/                 # ReportLab PDF generator
```

---

## 🚀 Deployment Instructions

### Option 1: GitHub Pages (100% Free, $0 Serverless Hosting)

Because all HTML, CSS, JS, images, and ONNX models sit directly at the root, the entire portal is ready for GitHub Pages:

1. **Push this repository to GitHub**:
   ```bash
   # Add your GitHub repository as remote
   git remote add origin https://github.com/<your-username>/<your-repo-name>.git

   # Rename branch to main if needed
   git branch -M main

   # Push all files to GitHub
   git push -u origin main
   ```

2. **Enable GitHub Pages**:
   * On GitHub, open your repository $\rightarrow$ Click **Settings**.
   * In the left sidebar, click **Pages**.
   * Under **Build and deployment** $\rightarrow$ **Source**:
     * Select **Deploy from a branch**.
     * Branch: `main` (or `master`), Folder: `/ (root)`.
   * Click **Save**.

3. **Visit Your Live Portal**:
   * Your site will be live in $\sim$30 seconds at:  
     `https://<your-username>.github.io/<your-repo-name>/`

> **Note on Model Files**: The `.nojekyll` file at the root ensures GitHub Pages serves the `.onnx` binary files and all image subdirectories without restriction.

---

### Option 2: Local Python Streamlit Application

If you wish to run the PyTorch research backend locally:

1. **Clone and create a virtual environment**:
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd RealTrace-AI
   python -m venv .venv
   ```

2. **Activate the virtual environment**:
   * **Windows**:
     ```powershell
     .venv\Scripts\activate
     ```
   * **Linux / macOS**:
     ```bash
     source .venv/bin/activate
     ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch Streamlit**:
   ```bash
   streamlit run app/app.py
   ```
   Open `http://localhost:8501` in your browser.

---

## 🧰 Technology Stack

| Layer | Component | Technologies |
| :--- | :--- | :--- |
| **Frontend Portal** | Institutional Web Suite | HTML5, CSS3 Variables, ES6 JavaScript, Google Fonts (Space Grotesk, Inter, JetBrains Mono, Rajdhani) |
| **In-Browser ML** | Neural Inference & Explainability | ONNX Runtime Web (WASM / WebGL), HTML5 Canvas 2D FFT & DCT, jsPDF |
| **Icons & Media** | Visual Assets | Lucide Icons, Institutional High-Res Badges, Responsive HTML5 Audio API |
| **Research Backend** | Deep Learning & Training | Python 3.10+, PyTorch, TorchVision, NumPy, SciPy, Pillow, Scikit-Learn |
| **Evaluation** | Cross-Generator Benchmarks | Tiny-GenImage, Hugging Face Hub, Pandas, Matplotlib, Seaborn |
| **CI/CD & Hosting** | Deployment | GitHub Pages (`.nojekyll`), GitHub Actions (`deploy.yml`), Streamlit Cloud |

---

## 🎓 Academic & Team Information

**Project Title:**  
*RealTrace AI: An Institutional Cyber-Forensic Intelligence Framework & Real-Time Threat Detection Portal*

**Institution:**  
*Engineering College Ajmer Rajasthan*  
*Department of Computer Science & Engineering (Cybersecurity)*

### 👥 Team Members

| Name | Role / Specialization |
| :--- | :--- |
| **Durgjeet Kataria** | Lead Architecture & Deep Learning Models |
| **Jay Kumar** | Web Platform Architecture, UI/UX & Client-Side Forensics |
| **Ankur Tetarwal** | Dataset Engineering & Cross-Generator Evaluation |
| **Gaurav Singh Solanki** | Threat Research, Degradation Testing & Forensic Analysis |

---

## ⚠️ Scientific & Legal Disclaimer

* **Decision-Support Scope**: RealTrace AI operates as an analytical decision-support tool. Model predictions, Grad-CAM overlays, and frequency spectrum representations provide probabilistic forensic indicators and should be evaluated alongside contextual evidence.
* **Official Indian Cyber Reporting**: In the event of cyber fraud, financial scams, or identity impersonation in India, immediately dial **1930** (Toll-Free 24x7) or file a formal complaint at the official Ministry of Home Affairs portal: [**cybercrime.gov.in**](https://cybercrime.gov.in).

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
