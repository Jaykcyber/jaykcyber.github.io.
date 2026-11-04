# 🚀 Deploying RealTrace AI to GitHub Pages ($0 Forever)

RealTrace AI's frontend is **100% client-side and serverless**. Neural inference, frequency forensics (FFT/DCT), Grad-CAM heatmaps, PDF reporting, and cyber awareness tools all run directly on the user's browser via **ONNX Runtime WebAssembly (WASM)**.

There are **zero backend servers**, **zero cloud costs**, and **zero maintenance fees**.

---

## 📋 Option 1: Direct Push of Frontend Folder (Quickest & Easiest)

As noted in the instructions, you can publish the `frontend/` directory directly into a dedicated GitHub repository:

### Step 1: Initialize Git in the frontend folder
Open your terminal (PowerShell or Bash) and navigate to the frontend folder:
```bash
cd RealTrace-AI-main/frontend
git init
git add .
git commit -m "Deploy RealTrace AI Client-Side Studio & Awareness Portal"
```

### Step 2: Push to your GitHub Repository
Create a new public repository on GitHub (e.g. `realtrace-ai` or `<username>.github.io`):
```bash
git remote add origin https://github.com/<your-username>/<your-repo-name>.git
git branch -M main
git push -u origin main
```

### Step 3: Enable GitHub Pages in Repository Settings
1. On GitHub, navigate to your repository.
2. Click **Settings** (top right tab).
3. In the left sidebar, click **Pages** (under the "Code and automation" section).
4. Under **Build and deployment**:
   - **Source**: Select `Deploy from a branch`
   - **Branch**: Select `main`
   - **Folder**: Select `/ (root)`
5. Click **Save**.

🎉 **Your site will be live within 60 seconds at:**
```
https://<your-username>.github.io/<your-repo-name>/
```
or `https://<your-username>.github.io/` if using a user page.

---

## ⚙️ Option 2: Automated GitHub Actions Deployment (If Pushing Entire Repo)

If you push the entire repository (`RealTrace-AI-main`) with python src and frontend together, you can deploy the `frontend/` subdirectory automatically:

1. In your GitHub repo, go to **Settings** → **Pages**.
2. Under **Build and deployment** → **Source**, select **GitHub Actions**.
3. RealTrace AI includes the `.github/workflows/deploy.yml` workflow which automatically publishes the `frontend/` folder on every push to `main`!

---

## 🛡️ Key Features Included in This Deployment:

1. **Interactive Forensic Studio (`index.html`)**:
   - In-browser neural inference with ONNX Runtime WASM (Baseline CNN & Robust EfficientNet).
   - Resilient zero-fail client-side forensic fallback engine.
   - Interactive **2.5x Zoom Magnifier Loupe** for microscopic pixel inspection.
   - 2D Fast Fourier Transform (FFT) & Discrete Cosine Transform (DCT) spectra.
   - Grad-CAM spatial activation heatmaps with real-time opacity slider.
   - Cryptographic SHA-256 evidence fingerprinting.
   - Evidence-grade PDF reports with official Indian Cyber Crime 1930 guidance.

2. **Dedicated AI Awareness & Indian Cyber Helplines Portal (`awareness.html`)**:
   - **Official Emergency Helplines**: 1930 (MHA/I4C 24x7 Hotline), cybercrime.gov.in, CERT-In, NCW (7827170170), Childline (1098), 112, Chakshu, RBI Sachet.
   - **Interactive Incident Assistant**: Step-by-step containment protocol + instant pre-formatted formal police complaint drafting ready to paste into `cybercrime.gov.in`.
   - **36 State & UT Cyber Crime Police Directory**: Searchable directory of state police cells with 1-click copy for emails, phone numbers, and portals.
   - **Educational Deepfake Literacy**: Analysis of GANs, Diffusion models, "Digital Arrest" scam dissection, voice cloning risks, and 8 visual forensic red flags.
   - **Interactive "Spot the Fake" Real vs AI Challenge**: 4 gamified inspection scenarios with live scoring and forensic explanations.
   - **Legal Rights**: IT Act Sections 66C, 66D, 66E, 67, 67A, and 24-hour mandatory platform takedown under IT Rules 2021.

3. **Interactive & Animated UI Theme (`style.css` & `app.js` / `awareness.js`)**:
   - Cyber-forensic dark aesthetic with particle constellation canvas.
   - Web Audio API synthesizer for cyber sound effects and navbar sound toggle.
   - Animated confidence number ticker.
   - Responsive design with animated mobile navigation drawer.
