# import os
# import sys

# import matplotlib.pyplot as plt
# import streamlit as st
# from huggingface_hub import hf_hub_download
# from PIL import Image

# sys.path.append(os.path.abspath("."))

# from src.inference.analyze_image import analyze_image
# from src.reporting.report_generator import generate_report

# st.set_page_config(
#     page_title="RealTrace AI | Forensic Verification",
#     page_icon="🔍",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )

# HF_REPO_ID = "Durgjeet/RealTrace-AI"

# MODEL_OPTIONS = {
#     "Baseline CNN": "baseline_best.pt",
#     "ResNet18": "resnet18_best.pt",
#     "EfficientNet-B0 Original": "efficientnet_b0_best.pt",
#     "EfficientNet-B0 Generalized": "efficientnet_b0_generalized.pt",
#     "EfficientNet-B0 Robust (Recommended)": "efficientnet_b0_robust.pt",
# }


# @st.cache_resource
# def get_checkpoint(filename: str) -> str:
#     return hf_hub_download(
#         repo_id=HF_REPO_ID,
#         filename=filename,
#     )


# def inject_styles() -> None:
#     st.markdown(
#         """
#         <style>
#         @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

#         :root {
#             --bg: #15171c;
#             --panel: #1f232b;
#             --panel-2: #262b34;
#             --line: #353b46;
#             --line-strong: #454c5a;
#             --text: #e6e9ef;
#             --muted: #9aa5b8;
#             --blue: #d4a72c;
#             --blue-soft: #2b2618;
#             --teal: #34d399;
#             --teal-soft: #122a24;
#             --red: #f87171;
#             --red-soft: #2a1818;
#             --amber-line: #5a4a25;
#             --amber-bg: #23201a;
#         }

#         .stApp {
#             background: var(--bg);
#             color: var(--text);
#             font-family: 'DM Sans', sans-serif;
#         }

#         [data-testid="stHeader"] {
#             background: transparent;
#         }

#         .block-container {
#             max-width: 1380px;
#             padding: 2.5rem 3rem 4rem;
#         }

#         h1, h2, h3, h4 {
#             font-family: 'Space Grotesk', sans-serif !important;
#             letter-spacing: -.03em;
#             color: var(--text) !important;
#         }

#         h1 {
#             font-size: 2.5rem !important;
#             margin-bottom: .15rem !important;
#         }

#         h2 {
#             font-size: 1.35rem !important;
#             margin: 0 !important;
#         }

#         h3 {
#             font-size: 1.05rem !important;
#         }

#         p, label, .stCaption {
#             color: var(--muted);
#         }

#         [data-testid="stSidebar"] {
#             background: #1a1d23;
#             border-right: 1px solid var(--line);
#         }

#         [data-testid="stSidebar"] > div:first-child {
#             padding: 2rem 1.25rem;
#         }

#         .brand {
#             font-family: 'Space Grotesk', sans-serif;
#             font-weight: 700;
#             font-size: 1.3rem;
#             color: var(--text);
#             display: flex;
#             align-items: center;
#         }

#         .brand-mark {
#             display: inline-flex;
#             width: 30px;
#             height: 30px;
#             align-items: center;
#             justify-content: center;
#             border: 1px solid var(--blue);
#             background: var(--blue-soft);
#             border-radius: 9px;
#             color: var(--blue);
#             margin-right: 10px;
#             font-weight: 700;
#             font-size: .95rem;
#         }

#         .brand-sub {
#             color: var(--muted);
#             font-size: .78rem;
#             margin-top: .45rem;
#             line-height: 1.5;
#         }

#         .sidebar-label {
#             color: #7a8aa1;
#             text-transform: uppercase;
#             letter-spacing: .12em;
#             font-size: .68rem;
#             font-weight: 700;
#             margin: 1.8rem 0 .55rem;
#         }

#         .pipeline {
#             color: var(--muted);
#             font-size: .83rem;
#             line-height: 1.95;
#         }

#         .pipeline .step-no {
#             display: inline-block;
#             width: 22px;
#             color: var(--blue);
#             font-weight: 700;
#         }

#         .pipeline b {
#             color: #c4ccd9;
#             font-weight: 500;
#         }

#         .sidebar-note {
#             border: 1px solid var(--line);
#             background: var(--panel-2);
#             border-radius: 12px;
#             padding: .8rem .9rem;
#             color: var(--muted);
#             font-size: .78rem;
#             line-height: 1.55;
#         }

#         .eyebrow {
#             color: var(--blue);
#             font-size: .72rem;
#             font-weight: 700;
#             letter-spacing: .14em;
#             text-transform: uppercase;
#             margin-bottom: .55rem;
#         }

#         .subtitle {
#             font-size: 1.02rem;
#             color: #b6c0d0;
#             margin: .35rem 0 0;
#         }

#         .subtitle-2 {
#             font-size: .9rem;
#             color: var(--muted);
#             margin: .35rem 0 0;
#         }

#         .status {
#             display: inline-flex;
#             align-items: center;
#             gap: 8px;
#             padding: 7px 13px;
#             border: 1px solid #5a4a25;
#             border-radius: 999px;
#             color: var(--blue);
#             background: var(--blue-soft);
#             font-size: .8rem;
#             font-weight: 600;
#             white-space: nowrap;
#         }

#         .status-dot {
#             width: 7px;
#             height: 7px;
#             border-radius: 50%;
#             background: var(--teal);
#             box-shadow: 0 0 0 4px rgba(52,211,153,.15);
#         }

#         .hero {
#             display: flex;
#             align-items: flex-end;
#             justify-content: space-between;
#             gap: 2rem;
#             margin-bottom: 2rem;
#             padding-bottom: 1.5rem;
#             border-bottom: 1px solid var(--line);
#         }

#         .card {
#             background: var(--panel);
#             border: 1px solid var(--line);
#             border-radius: 16px;
#             padding: 1.25rem 1.35rem;
#             margin-bottom: 1rem;
#             box-shadow: 0 1px 2px rgba(0,0,0,.25);
#         }

#         .card-title {
#             color: var(--text);
#             font-family: 'Space Grotesk', sans-serif;
#             font-weight: 600;
#             font-size: 1.02rem;
#             margin-bottom: .25rem;
#         }

#         .card-copy {
#             color: var(--muted);
#             font-size: .87rem;
#             line-height: 1.55;
#         }

#         .metric-card {
#             background: var(--panel);
#             border: 1px solid var(--line);
#             border-radius: 14px;
#             padding: 1rem 1.05rem;
#             min-height: 104px;
#             margin-bottom: .75rem;
#             box-shadow: 0 1px 2px rgba(0,0,0,.2);
#         }

#         .metric-label {
#             color: var(--muted);
#             font-size: .72rem;
#             text-transform: uppercase;
#             letter-spacing: .09em;
#             font-weight: 600;
#         }

#         .metric-value {
#             color: var(--text);
#             font-family: 'Space Grotesk', sans-serif;
#             font-size: 1.4rem;
#             font-weight: 700;
#             margin-top: .45rem;
#             overflow-wrap: anywhere;
#         }

#         .real {
#             color: var(--teal) !important;
#         }

#         .generated {
#             color: var(--red) !important;
#         }

#         .pill {
#             display: inline-flex;
#             align-items: center;
#             gap: 7px;
#             margin-top: .5rem;
#             padding: 5px 11px;
#             border-radius: 999px;
#             font-size: .74rem;
#             font-weight: 700;
#             letter-spacing: .04em;
#         }

#         .pill.real {
#             background: var(--teal-soft);
#             border: 1px solid #1f4a3f;
#         }

#         .pill.generated {
#             background: var(--red-soft);
#             border: 1px solid #4a2828;
#         }

#         .section {
#             margin-top: 2.1rem;
#             margin-bottom: .8rem;
#             display: flex;
#             align-items: center;
#             justify-content: space-between;
#             gap: 1rem;
#         }

#         .section-note {
#             color: var(--muted);
#             font-size: .8rem;
#         }

#         .stButton > button,
#         .stButton > button p,
#         .stButton > button span,
#         .stDownloadButton > button,
#         .stDownloadButton > button p,
#         .stDownloadButton > button span {
#             color: #ffffff !important;
#         }

#         .stButton > button {
#             border-radius: 10px;
#             border: 1px solid var(--blue);
#             background: var(--blue);
#             color: #ffffff !important;
#             font-weight: 700;
#             min-height: 44px;
#         }

#         .stButton > button:hover {
#             border-color: #b8921f;
#             background: #b8921f;
#             color: #ffffff !important;
#         }

#         .stDownloadButton > button {
#             border-radius: 10px;
#             border: 1px solid var(--blue);
#             background: var(--blue);
#             color: #ffffff !important;
#             font-weight: 700;
#             min-height: 44px;
#         }

#         .stDownloadButton > button:hover {
#             border-color: #b8921f;
#             background: #b8921f;
#             color: #ffffff !important;
#         }

#         [data-testid="stFileUploader"] {
#             background: var(--panel-2);
#             border: 1px dashed var(--line-strong);
#             border-radius: 12px;
#             padding: .5rem;
#         }

#         [data-testid="stMetric"] {
#             background: var(--panel);
#             border: 1px solid var(--line);
#             padding: 1rem;
#             border-radius: 12px;
#         }

#         [data-testid="stMetricLabel"] {
#             color: var(--muted);
#         }

#         [data-testid="stMetricValue"] {
#             color: var(--text);
#         }

#         [data-testid="stImage"] img {
#             border-radius: 14px;
#             border: 1px solid var(--line);
#         }

#         .disclaimer {
#             border: 1px solid var(--amber-line);
#             background: var(--amber-bg);
#             border-radius: 14px;
#             padding: 1rem 1.15rem;
#             color: #d8c89a;
#             font-size: .86rem;
#             line-height: 1.65;
#         }

#         .footer {
#             border-top: 1px solid var(--line);
#             margin-top: 2.5rem;
#             padding-top: 1rem;
#             color: #6b7689;
#             font-size: .75rem;
#         }

#         .stSelectbox > div > div {
#             background-color: var(--panel-2);
#             border-color: var(--line);
#             color: var(--text);
#         }

#         .stSelectbox svg {
#             color: var(--muted);
#         }

#         .stProgress > div > div {
#             background-color: transparent;
#         }

#         .stProgress > div {
#             background-color: var(--line);
#         }

#         .stProgress,
#         .stProgress p,
#         .stProgress span,
#         [data-testid="stProgress"] {
#             color: #ffffff !important;
#         }

#         div[data-testid="stAlert"] {
#             background-color: var(--panel-2);
#             color: var(--text);
#         }

#         .stSpinner > div {
#             color: var(--blue);
#         }

#         @media (max-width: 900px) {
#             .block-container {
#                 padding: 1.5rem 1rem 3rem;
#             }

#             .hero {
#                 display: block;
#             }

#             .hero .status {
#                 margin-top: 1rem;
#             }

#             h1 {
#                 font-size: 2rem !important;
#             }
#         }
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )


# def metric_card(label: str, value, class_name: str = "") -> None:
#     st.markdown(
#         f"""
#         <div class="metric-card">
#             <div class="metric-label">{label}</div>
#             <div class="metric-value {class_name}">{value}</div>
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )


# def section(title: str, note: str = "") -> None:
#     st.markdown(
#         f"""
#         <div class="section">
#             <h2>{title}</h2>
#             <div class="section-note">{note}</div>
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )


# def card_open(title: str, copy: str = "") -> None:
#     st.markdown(
#         f"""
#         <div class="card">
#             <div class="card-title">{title}</div>
#             <div class="card-copy">{copy}</div>
#         """,
#         unsafe_allow_html=True,
#     )


# def card_close() -> None:
#     st.markdown("</div>", unsafe_allow_html=True)


# def render_sidebar() -> str:
#     with st.sidebar:
#         st.markdown(
#             '<div class="brand"><span class="brand-mark">R</span>RealTrace AI</div>'
#             '<div class="brand-sub">Generalizable forensic intelligence framework for authenticity '
#             "verification of AI-generated visual content.</div>",
#             unsafe_allow_html=True,
#         )

#         st.markdown(
#             '<div class="sidebar-label">Detection Configuration</div>',
#             unsafe_allow_html=True,
#         )

#         selected = st.selectbox(
#             "Select Detection Model",
#             list(MODEL_OPTIONS.keys()),
#             index=4,
#         )

#         st.caption(
#             f"Checkpoint: `{MODEL_OPTIONS[selected]}`"
#         )

#         st.markdown(
#             '<div class="sidebar-label">Analysis Pipeline</div>',
#             unsafe_allow_html=True,
#         )

#         st.markdown(
#             """
#             <div class="pipeline">
#                 <span class="step-no">01</span><b>Visual classification</b><br/>
#                 <span class="step-no">02</span><b>Confidence analysis</b><br/>
#                 <span class="step-no">03</span><b>Grad-CAM explanation</b><br/>
#                 <span class="step-no">04</span><b>FFT analysis</b><br/>
#                 <span class="step-no">05</span><b>DCT analysis</b><br/>
#                 <span class="step-no">06</span><b>Forensic report</b>
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )

#         st.markdown(
#             '<div class="sidebar-label">System Note</div>',
#             unsafe_allow_html=True,
#         )

#         st.markdown(
#             '<div class="sidebar-note">Model-based analysis for research and demonstration purposes. '
#             "Results should be interpreted with scientific caution.</div>",
#             unsafe_allow_html=True,
#         )

#     return selected


# def render_header() -> None:
#     st.markdown(
#         """
#         <div class="hero">
#             <div>
#                 <div class="eyebrow">Digital forensics workstation</div>
#                 <h1>RealTrace AI</h1>
#                 <p class="subtitle">AI-Generated Visual Content Authenticity Verification</p>
#                 <p class="subtitle-2">Deep-learning classification with explainable AI and frequency-domain forensic analysis.</p>
#             </div>
#             <div class="status">
#                 <span class="status-dot"></span>
#                 Forensic Analysis System
#             </div>
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )


# def render_result_card(
#     result: dict,
#     selected_model: str,
#     prediction_class: str,
# ) -> None:
#     section(
#         "Classification Result",
#         "Model output",
#     )

#     c1, c2, c3 = st.columns(3)

#     with c1:
#         st.markdown(
#             f"""
#             <div class="metric-card">
#                 <div class="metric-label">Prediction</div>
#                 <div class="metric-value {prediction_class}">
#                     {result["prediction"]}
#                 </div>
#                 <div class="pill {prediction_class}">
#                     {"Classified as authentic capture" if prediction_class == "real" else "Classified as AI-generated"}
#                 </div>
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )

#     with c2:
#         metric_card(
#             "Model confidence",
#             f'{result["confidence"] * 100:.2f}%',
#         )

#     with c3:
#         metric_card(
#             "Selected model",
#             selected_model,
#         )


# def render_probability_section(
#     result: dict,
# ) -> None:
#     section(
#         "Prediction Probabilities",
#         "Softmax output",
#     )

#     p1, p2 = st.columns(2)

#     with p1:
#         card_open(
#             "Real Probability",
#             "Likelihood assigned to the authentic-capture class.",
#         )

#         st.progress(
#             float(result["real_probability"]),
#             text=f'{result["real_probability"] * 100:.2f}%',
#         )

#         card_close()

#     with p2:
#         card_open(
#             "AI-Generated Probability",
#             "Likelihood assigned to the AI-generated class.",
#         )

#         st.progress(
#             float(result["ai_probability"]),
#             text=f'{result["ai_probability"] * 100:.2f}%',
#         )

#         card_close()

#     st.info(
#         "Model confidence represents the model's certainty in its classification. "
#         "It is not the probability that the image is genuinely authentic. "
#         "Images from unseen generators may be misclassified with high confidence."
#     )


# def render_gradcam_section(
#     result: dict,
# ) -> None:
#     section(
#         "Explainable AI — Grad-CAM",
#         "Class-activation overlay",
#     )

#     st.image(
#         result["gradcam_overlay"],
#         caption="Regions contributing strongly to the model prediction",
#         use_container_width=True,
#     )

#     st.info(
#         "Grad-CAM indicates image regions that contributed strongly to the model's prediction. "
#         "A highlighted region is not definitive proof that the region itself is fake."
#     )


# def render_frequency_section(
#     result: dict,
# ) -> None:
#     section(
#         "Frequency-Domain Forensics",
#         "Spectral representations",
#     )

#     f1, f2 = st.columns(2)

#     with f1:
#         card_open(
#             "FFT Magnitude Spectrum",
#             "Frequency representation generated using the Fast Fourier Transform.",
#         )

#         fft_fig = plt.figure(
#             figsize=(6, 5)
#         )

#         plt.imshow(
#             result["fft"],
#             cmap="gray",
#         )

#         plt.axis("off")
#         plt.tight_layout()

#         st.pyplot(
#             fft_fig
#         )

#         plt.close(
#             fft_fig
#         )

#         card_close()

#     with f2:
#         card_open(
#             "DCT Magnitude Spectrum",
#             "Spatial-frequency representation generated using the Discrete Cosine Transform.",
#         )

#         dct_fig = plt.figure(
#             figsize=(6, 5)
#         )

#         plt.imshow(
#             result["dct"],
#             cmap="gray",
#         )

#         plt.axis("off")
#         plt.tight_layout()

#         st.pyplot(
#             dct_fig
#         )

#         plt.close(
#             dct_fig
#         )

#         card_close()


# def render_summary_section(
#     result: dict,
#     selected_model: str,
#     prediction_class: str,
# ) -> None:
#     section(
#         "Analysis Summary",
#         "Values returned by the inference pipeline",
#     )

#     s1, s2, s3 = st.columns(3)

#     with s1:
#         metric_card(
#             "Selected model",
#             selected_model,
#         )

#         metric_card(
#             "Internal model name",
#             result["model_name"],
#         )

#     with s2:
#         metric_card(
#             "Predicted class",
#             result["prediction"],
#             prediction_class,
#         )

#         metric_card(
#             "Model confidence",
#             f'{result["confidence"] * 100:.2f}%',
#         )

#     with s3:
#         metric_card(
#             "Real probability",
#             f'{result["real_probability"] * 100:.2f}%',
#         )

#         metric_card(
#             "AI-generated probability",
#             f'{result["ai_probability"] * 100:.2f}%',
#         )


# def render_report_section(
#     image: Image.Image,
#     result: dict,
# ) -> None:
#     section(
#         "Forensic Analysis Report",
#         "PDF export",
#     )

#     card_open(
#         "Downloadable report",
#         "Download a PDF containing the classification result, "
#         "explainability visualization, and frequency-domain analysis.",
#     )

#     report = generate_report(
#         image,
#         result,
#     )

#     st.download_button(
#         "Download Forensic Analysis Report",
#         data=report.getvalue(),
#         file_name="RealTrace_AI_Forensic_Report.pdf",
#         mime="application/pdf",
#     )

#     card_close()


# def render_disclaimer() -> None:
#     st.markdown(
#         """
#         <div class="disclaimer">
#             <b>Scientific disclaimer</b><br/>
#             RealTrace AI provides model-based forensic analysis.
#             The classification, confidence score, Grad-CAM visualization
#             and frequency-domain representations should not be treated as
#             definitive forensic proof. Results may be less reliable for
#             AI generators or image distributions not represented during
#             model training.
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )


# def render_footer() -> None:
#     st.markdown(
#         '<div class="footer">'
#         "RealTrace AI · University final-year project demonstration · "
#         "Explainable, evidence-aware visual verification"
#         "</div>",
#         unsafe_allow_html=True,
#     )


# inject_styles()

# selected_model = render_sidebar()

# checkpoint_filename = MODEL_OPTIONS[
#     selected_model
# ]

# try:
#     checkpoint_path = get_checkpoint(
#         checkpoint_filename
#     )
# except Exception as error:
#     st.error(
#         f"Failed to download model checkpoint: {error}"
#     )
#     st.stop()

# render_header()

# section(
#     "Image Evidence",
#     "JPG · JPEG · PNG · WEBP",
# )

# card_open(
#     "Upload an image for examination",
#     "Evidence is analyzed only after you initiate the forensic workflow.",
# )

# uploaded_file = st.file_uploader(
#     "Upload image evidence",
#     type=[
#         "jpg",
#         "jpeg",
#         "png",
#         "webp",
#     ],
#     label_visibility="collapsed",
# )

# card_close()

# if uploaded_file is not None:
#     try:
#         image = Image.open(
#             uploaded_file
#         ).convert(
#             "RGB"
#         )

#         left, right = st.columns(
#             [1.45, 1],
#             gap="large",
#         )

#         with left:
#             st.image(
#                 image,
#                 caption="Evidence preview",
#                 use_container_width=True,
#             )

#         with right:
#             st.markdown(
#                 '<div class="card-title">Evidence metadata</div>',
#                 unsafe_allow_html=True,
#             )

#             metric_card(
#                 "File name",
#                 uploaded_file.name,
#             )

#             metric_card(
#                 "Dimensions",
#                 f"{image.width} × {image.height} px",
#             )

#             metric_card(
#                 "Format",
#                 uploaded_file.type or "RGB image",
#             )

#             analyze = st.button(
#                 "Analyze Image",
#                 type="primary",
#                 use_container_width=True,
#             )

#         if analyze:
#             with st.spinner(
#                 "Running forensic analysis..."
#             ):
#                 result = analyze_image(
#                     image,
#                     checkpoint_path,
#                 )

#             st.success(
#                 "Analysis completed successfully."
#             )

#             prediction_class = (
#                 "real"
#                 if str(
#                     result["prediction"]
#                 ).upper() == "REAL"
#                 else "generated"
#             )

#             render_result_card(
#                 result,
#                 selected_model,
#                 prediction_class,
#             )

#             render_probability_section(
#                 result,
#             )

#             render_gradcam_section(
#                 result,
#             )

#             render_frequency_section(
#                 result,
#             )

#             render_summary_section(
#                 result,
#                 selected_model,
#                 prediction_class,
#             )

#             render_report_section(
#                 image,
#                 result,
#             )

#             render_disclaimer()

#     except Exception as error:
#         st.error(
#             f"Analysis failed: {error}"
#         )
# render_footer()



#ABOVE IS THE ORIGINAL PROJECT UI 



import io
import os
import sys

import matplotlib.pyplot as plt
import streamlit as st
from huggingface_hub import hf_hub_download
from PIL import Image

sys.path.append(os.path.abspath("."))

from src.inference.analyze_image import analyze_image
from src.reporting.report_generator import generate_report

st.set_page_config(
    page_title="RealTrace AI | Forensic Verification",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded",
)

HF_REPO_ID = "Durgjeet/RealTrace-AI"

MODEL_OPTIONS = {
    "Baseline CNN": "baseline_best.pt",
    "ResNet18": "resnet18_best.pt",
    "EfficientNet-B0 Original": "efficientnet_b0_best.pt",
    "EfficientNet-B0 Generalized": "efficientnet_b0_generalized.pt",
    "EfficientNet-B0 Robust (Recommended)": "efficientnet_b0_robust.pt",
}

PIPELINE = [
    "Visual classification",
    "Confidence analysis",
    "Grad-CAM explanation",
    "FFT analysis",
    "DCT analysis",
    "Forensic report",
]


@st.cache_resource
def get_checkpoint(filename: str) -> str:
    return hf_hub_download(repo_id=HF_REPO_ID, filename=filename)


CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
:root{
  --bg:#07070b; --glass:rgba(255,255,255,.035); --line:rgba(255,255,255,.08);
  --text:#f2f1f8; --muted:#8c8aa3; --p:#8b5cf6; --p2:#6d5ef5; --p-soft:rgba(139,92,246,.14);
  --ok:#34d399; --bad:#fb7185;
}
html,body,.stApp{font-family:'Inter',sans-serif;color:var(--text);}
.stApp{
  background:
   radial-gradient(900px 500px at 50% -10%,rgba(109,94,245,.35),transparent 70%),
   radial-gradient(700px 500px at 100% 60%,rgba(139,92,246,.14),transparent 70%),
   var(--bg);
}
[data-testid="stHeader"]{background:transparent;}
.block-container{max-width:1200px;padding:2rem 2.5rem 4rem;}
h1,h2,h3{color:var(--text)!important;letter-spacing:-.025em;font-weight:600!important;}
p,label,.stCaption{color:var(--muted);}

/* sidebar */
[data-testid="stSidebar"]{background:#0a0a10;border-right:1px solid var(--line);}
.brand{display:flex;align-items:center;gap:10px;font-weight:700;font-size:1.2rem;}
.logo{width:30px;height:30px;border-radius:9px;display:grid;place-items:center;
  background:linear-gradient(135deg,var(--p2),var(--p));box-shadow:0 0 20px rgba(139,92,246,.5);font-size:.9rem;}
.side-label{color:var(--muted);font-size:.68rem;letter-spacing:.14em;text-transform:uppercase;font-weight:600;margin:1.6rem 0 .6rem;}
.step{display:flex;align-items:center;gap:10px;padding:.5rem .7rem;border-radius:10px;
  color:#c9c7dd;font-size:.85rem;margin-bottom:4px;border:1px solid transparent;}
.step:hover{background:var(--p-soft);border-color:var(--line);}
.step i{font-style:normal;color:var(--p);font-weight:700;font-size:.72rem;}
.note{border:1px solid var(--line);background:var(--glass);border-radius:12px;padding:.8rem;color:var(--muted);font-size:.78rem;line-height:1.55;}

/* hero */
.hero{text-align:center;padding:2.2rem 0 1.8rem;}
.chip{display:inline-flex;align-items:center;gap:8px;padding:6px 14px;border-radius:999px;
  border:1px solid var(--line);background:var(--glass);color:#cfcde6;font-size:.76rem;font-weight:500;}
.dot{width:7px;height:7px;border-radius:50%;background:var(--ok);box-shadow:0 0 0 4px rgba(52,211,153,.15);}
.hero h1{font-size:3.2rem!important;margin:1rem 0 .4rem!important;
  background:linear-gradient(180deg,#fff,#a79bff);-webkit-background-clip:text;-webkit-text-fill-color:transparent;}
.hero .sub{font-size:1.05rem;color:#c9c7dd;margin:0;}
.hero .sub2{font-size:.9rem;color:var(--muted);margin:.4rem 0 0;}

/* section heading */
.sec{text-align:center;margin:3rem 0 1.4rem;}
.sec h2{font-size:1.7rem!important;margin:.8rem 0 .3rem!important;}
.sec p{font-size:.88rem;margin:0;}

/* glass cards */
[data-testid="stVerticalBlockBorderWrapper"]{
  background:linear-gradient(180deg,rgba(139,92,246,.07),rgba(255,255,255,.02));
  border:1px solid var(--line)!important;border-radius:18px!important;
  box-shadow:0 20px 50px -25px rgba(109,94,245,.45), inset 0 1px 0 rgba(255,255,255,.05);}
.ct{font-weight:600;font-size:1rem;margin-bottom:.2rem;}
.cc{color:var(--muted);font-size:.84rem;line-height:1.55;margin-bottom:.6rem;}
.metric{background:var(--glass);border:1px solid var(--line);border-radius:16px;padding:1rem 1.1rem;
  min-height:104px;margin-bottom:.8rem;position:relative;overflow:hidden;}
.metric:after{content:"";position:absolute;inset:auto -20% -60% -20%;height:80%;
  background:radial-gradient(closest-side,rgba(139,92,246,.28),transparent);}
.ml{color:var(--muted);font-size:.7rem;text-transform:uppercase;letter-spacing:.1em;font-weight:600;}
.mv{font-size:1.5rem;font-weight:700;margin-top:.45rem;overflow-wrap:anywhere;position:relative;z-index:1;}
.real{color:var(--ok)!important;} .generated{color:var(--bad)!important;}
.pill{display:inline-block;margin-top:.5rem;padding:4px 11px;border-radius:999px;font-size:.72rem;font-weight:600;position:relative;z-index:1;}
.pill.real{background:rgba(52,211,153,.1);border:1px solid rgba(52,211,153,.3);}
.pill.generated{background:rgba(251,113,133,.1);border:1px solid rgba(251,113,133,.3);}

/* controls */
.stButton>button,.stDownloadButton>button{
  border:1px solid rgba(255,255,255,.15);border-radius:12px;min-height:46px;font-weight:600;
  background:linear-gradient(180deg,#8b7bff,#6d5ef5);box-shadow:0 8px 28px -8px rgba(109,94,245,.8);}
.stButton>button *,.stDownloadButton>button *{color:#fff!important;}
.stButton>button:hover,.stDownloadButton>button:hover{filter:brightness(1.12);border-color:#fff3;}
[data-testid="stFileUploader"]{background:var(--glass);border:1px dashed rgba(139,92,246,.45);border-radius:14px;padding:.5rem;}
[data-testid="stFileUploader"] section{background:transparent;}
.stSelectbox>div>div{background:var(--glass);border-color:var(--line);}
.stProgress>div{background:rgba(255,255,255,.08);border-radius:99px;}
.stProgress>div>div>div{background:linear-gradient(90deg,var(--p2),#c4b5fd);}
[data-testid="stImage"] img{border-radius:16px;border:1px solid var(--line);}
div[data-testid="stAlert"]{background:var(--glass);border:1px solid var(--line);border-radius:14px;color:var(--text);}
.disclaimer{border:1px solid rgba(251,191,36,.25);background:rgba(251,191,36,.05);border-radius:16px;
  padding:1rem 1.2rem;color:#e4d6a6;font-size:.85rem;line-height:1.65;margin-top:2rem;}
.footer{border-top:1px solid var(--line);margin-top:3rem;padding-top:1rem;text-align:center;color:#6b6985;font-size:.75rem;}
@media(max-width:900px){.block-container{padding:1.2rem 1rem 3rem;}.hero h1{font-size:2.2rem!important;}}
</style>
"""


def html(s: str) -> None:
    st.markdown(s, unsafe_allow_html=True)


def metric_card(label: str, value, cls: str = "") -> None:
    html(f'<div class="metric"><div class="ml">{label}</div><div class="mv {cls}">{value}</div></div>')


def section(title: str, note: str = "", tag: str = "") -> None:
    chip = f'<span class="chip">{tag}</span>' if tag else ""
    html(f'<div class="sec">{chip}<h2>{title}</h2><p>{note}</p></div>')


def card_head(title: str, copy: str = "") -> None:
    html(f'<div class="ct">{title}</div><div class="cc">{copy}</div>')


def render_sidebar() -> str:
    with st.sidebar:
        html(
            '<div class="brand"><span class="logo">R</span>RealTrace AI</div>'
            '<div class="cc" style="margin-top:.6rem">Generalizable forensic intelligence framework '
            "for authenticity verification of AI-generated visual content.</div>"
        )
        html('<div class="side-label">Detection Configuration</div>')
        selected = st.selectbox("Select Detection Model", list(MODEL_OPTIONS.keys()), index=4)
        st.caption(f"Checkpoint: `{MODEL_OPTIONS[selected]}`")
        html('<div class="side-label">Analysis Pipeline</div>')
        html("".join(f'<div class="step"><i>{n:02d}</i>{s}</div>' for n, s in enumerate(PIPELINE, 1)))
        html('<div class="side-label">System Note</div>')
        html(
            '<div class="note">Model-based analysis for research and demonstration purposes. '
            "Results should be interpreted with scientific caution.</div>"
        )
    return selected


def render_header() -> None:
    html(
        """
        <div class="hero">
          <span class="chip"><span class="dot"></span>Digital forensics workstation</span>
          <h1>RealTrace AI</h1>
          <p class="sub">AI-Generated Visual Content Authenticity Verification</p>
          <p class="sub2">Deep-learning classification with explainable AI and frequency-domain forensic analysis.</p>
        </div>
        """
    )


def render_result_card(result: dict, selected_model: str, cls: str) -> None:
    section("Classification Result", "Model output", "Result")
    c1, c2, c3 = st.columns(3)
    with c1:
        label = "Classified as authentic capture" if cls == "real" else "Classified as AI-generated"
        html(
            f'<div class="metric"><div class="ml">Prediction</div>'
            f'<div class="mv {cls}">{result["prediction"]}</div>'
            f'<div class="pill {cls}">{label}</div></div>'
        )
    with c2:
        metric_card("Model confidence", f'{result["confidence"] * 100:.2f}%')
    with c3:
        metric_card("Selected model", selected_model)


def render_probability_section(result: dict) -> None:
    section("Prediction Probabilities", "Softmax output", "Probabilities")
    p1, p2 = st.columns(2)
    with p1:
        with st.container(border=True):
            card_head("Real Probability", "Likelihood assigned to the authentic-capture class.")
            st.progress(float(result["real_probability"]), text=f'{result["real_probability"] * 100:.2f}%')
    with p2:
        with st.container(border=True):
            card_head("AI-Generated Probability", "Likelihood assigned to the AI-generated class.")
            st.progress(float(result["ai_probability"]), text=f'{result["ai_probability"] * 100:.2f}%')
    st.info(
        "Model confidence represents the model's certainty in its classification. "
        "It is not the probability that the image is genuinely authentic. "
        "Images from unseen generators may be misclassified with high confidence."
    )


def render_gradcam_section(result: dict) -> None:
    section("Explainable AI — Grad-CAM", "Class-activation overlay", "Explainability")
    with st.container(border=True):
        st.image(
            result["gradcam_overlay"],
            caption="Regions contributing strongly to the model prediction",
            use_container_width=True,
        )
    st.info(
        "Grad-CAM indicates image regions that contributed strongly to the model's prediction. "
        "A highlighted region is not definitive proof that the region itself is fake."
    )


def spectrum_plot(data) -> None:
    fig = plt.figure(figsize=(6, 5))
    plt.imshow(data, cmap="gray")
    plt.axis("off")
    plt.tight_layout()
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=200, bbox_inches="tight")
    plt.close(fig)
    buf.seek(0)
    st.image(buf, use_container_width=True)


def render_frequency_section(result: dict) -> None:
    section("Frequency-Domain Forensics", "Spectral representations", "Spectral")
    f1, f2 = st.columns(2)
    with f1:
        with st.container(border=True):
            card_head("FFT Magnitude Spectrum", "Frequency representation generated using the Fast Fourier Transform.")
            spectrum_plot(result["fft"])
    with f2:
        with st.container(border=True):
            card_head("DCT Magnitude Spectrum", "Spatial-frequency representation generated using the Discrete Cosine Transform.")
            spectrum_plot(result["dct"])


def render_summary_section(result: dict, selected_model: str, cls: str) -> None:
    section("Analysis Summary", "Values returned by the inference pipeline", "Summary")
    s1, s2, s3 = st.columns(3)
    with s1:
        metric_card("Selected model", selected_model)
        metric_card("Internal model name", result["model_name"])
    with s2:
        metric_card("Predicted class", result["prediction"], cls)
        metric_card("Model confidence", f'{result["confidence"] * 100:.2f}%')
    with s3:
        metric_card("Real probability", f'{result["real_probability"] * 100:.2f}%')
        metric_card("AI-generated probability", f'{result["ai_probability"] * 100:.2f}%')


def render_report_section(image: Image.Image, result: dict) -> None:
    section("Forensic Analysis Report", "PDF export", "Report")
    with st.container(border=True):
        card_head(
            "Downloadable report",
            "Download a PDF containing the classification result, explainability visualization, "
            "and frequency-domain analysis.",
        )
        report = generate_report(image, result)
        st.download_button(
            "Download Forensic Analysis Report",
            data=report.getvalue(),
            file_name="RealTrace_AI_Forensic_Report.pdf",
            mime="application/pdf",
        )


def render_disclaimer() -> None:
    html(
        """
        <div class="disclaimer"><b>Scientific disclaimer</b><br/>
        RealTrace AI provides model-based forensic analysis. The classification, confidence score,
        Grad-CAM visualization and frequency-domain representations should not be treated as
        definitive forensic proof. Results may be less reliable for AI generators or image
        distributions not represented during model training.</div>
        """
    )


def render_footer() -> None:
    html(
        '<div class="footer">RealTrace AI · University final-year project demonstration · '
        "Explainable, evidence-aware visual verification</div>"
    )


# ---------------------------------------------------------------- main
html(CSS)
selected_model = render_sidebar()

try:
    checkpoint_path = get_checkpoint(MODEL_OPTIONS[selected_model])
except Exception as error:
    st.error(f"Failed to download model checkpoint: {error}")
    st.stop()

render_header()
section("Image Evidence", "JPG · JPEG · PNG · WEBP", "Upload")

with st.container(border=True):
    card_head(
        "Upload an image for examination",
        "Evidence is analyzed only after you initiate the forensic workflow.",
    )
    uploaded_file = st.file_uploader(
        "Upload image evidence",
        type=["jpg", "jpeg", "png", "webp"],
        label_visibility="collapsed",
    )

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file).convert("RGB")
        left, right = st.columns([1.45, 1], gap="large")

        with left:
            with st.container(border=True):
                st.image(image, caption="Evidence preview", use_container_width=True)

        with right:
            card_head("Evidence metadata")
            metric_card("File name", uploaded_file.name)
            metric_card("Dimensions", f"{image.width} × {image.height} px")
            metric_card("Format", uploaded_file.type or "RGB image")
            analyze = st.button("Analyze Image", type="primary", use_container_width=True)

        if analyze:
            with st.spinner("Running forensic analysis..."):
                result = analyze_image(image, checkpoint_path)

            st.success("Analysis completed successfully.")
            cls = "real" if str(result["prediction"]).upper() == "REAL" else "generated"

            render_result_card(result, selected_model, cls)
            render_probability_section(result)
            render_gradcam_section(result)
            render_frequency_section(result)
            render_summary_section(result, selected_model, cls)
            render_report_section(image, result)
            render_disclaimer()

    except Exception as error:
        st.error(f"Analysis failed: {error}")

render_footer()






#BELOW IS THE IDK NEW UI MAYBE FORGOT






# import os
# import sys

# import matplotlib.pyplot as plt
# import streamlit as st
# from huggingface_hub import hf_hub_download
# from PIL import Image

# sys.path.append(os.path.abspath("."))

# from src.inference.analyze_image import analyze_image
# from src.reporting.report_generator import generate_report

# st.set_page_config(
#     page_title="RealTrace AI | Forensic Verification",
#     page_icon="🔍",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )


# # Hugging Face repository
# HF_REPO_ID = "Durgjeet/RealTrace-AI"


# # Available detection models
# MODEL_OPTIONS = {
#     "Baseline CNN": "baseline_best.pt",
#     "ResNet18": "resnet18_best.pt",
#     "EfficientNet-B0 Original": "efficientnet_b0_best.pt",
#     "EfficientNet-B0 Generalized": "efficientnet_b0_generalized.pt",
#     "EfficientNet-B0 Robust (Recommended)": "efficientnet_b0_robust.pt",
# }


# # Download model checkpoint from Hugging Face
# @st.cache_resource
# def get_checkpoint(filename: str) -> str:
#     return hf_hub_download(
#         repo_id=HF_REPO_ID,
#         filename=filename,
#     )


# def inject_styles() -> None:
#     st.markdown(
#         """
#         <style>
#         @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

#         :root {
#             --bg: #f5f7fb;
#             --panel: #ffffff;
#             --panel-2: #f8fafc;
#             --line: #e5e7eb;
#             --line-strong: #cbd5e1;
#             --text: #172033;
#             --muted: #64748b;
#             --blue: #4f46e5;
#             --blue-soft: #eef2ff;
#             --teal: #34d399;
#             --teal-soft: #ecfdf5;
#             --red: #f87171;
#             --red-soft: #fef2f2;
#             --amber-line: #fde68a;
#             --amber-bg: #fffbeb;
#         }

#         .stApp {
#             background: var(--bg);
#             color: var(--text);
#             font-family: 'DM Sans', sans-serif;
#         }

#         [data-testid="stHeader"] {
#             background: transparent;
#         }

#         .block-container {
#             max-width: 1380px;
#             padding: 2.25rem 3rem 4rem;
#         }

#         h1, h2, h3, h4 {
#             font-family: 'Space Grotesk', sans-serif !important;
#             letter-spacing: -.03em;
#             color: var(--text) !important;
#         }

#         h1 {
#             font-size: 2.5rem !important;
#             margin-bottom: .15rem !important;
#         }

#         h2 {
#             font-size: 1.35rem !important;
#             margin: 0 !important;
#         }

#         h3 {
#             font-size: 1.05rem !important;
#         }

#         p, label, .stCaption {
#             color: var(--muted);
#         }

#         [data-testid="stSidebar"] {
#             background: #ffffff;
#             border-right: 1px solid var(--line);
#         }

#         [data-testid="stSidebar"] > div:first-child {
#             padding: 2rem 1.25rem;
#         }

#         .brand {
#             font-family: 'Space Grotesk', sans-serif;
#             font-weight: 700;
#             font-size: 1.3rem;
#             color: var(--text);
#             display: flex;
#             align-items: center;
#         }

#         .brand-mark {
#             display: inline-flex;
#             width: 30px;
#             height: 30px;
#             align-items: center;
#             justify-content: center;
#             border: 1px solid var(--blue);
#             background: var(--blue-soft);
#             border-radius: 9px;
#             color: var(--blue);
#             margin-right: 10px;
#             font-weight: 700;
#             font-size: .95rem;
#         }

#         .brand-sub {
#             color: var(--muted);
#             font-size: .78rem;
#             margin-top: .45rem;
#             line-height: 1.5;
#         }

#         .sidebar-label {
#             color: #7a8aa1;
#             text-transform: uppercase;
#             letter-spacing: .12em;
#             font-size: .68rem;
#             font-weight: 700;
#             margin: 1.8rem 0 .55rem;
#         }

#         .pipeline {
#             color: var(--muted);
#             font-size: .83rem;
#             line-height: 1.95;
#         }

#         .pipeline .step-no {
#             display: inline-block;
#             width: 22px;
#             color: var(--blue);
#             font-weight: 700;
#         }

#         .pipeline b {
#             color: #334155;
#             font-weight: 500;
#         }

#         .sidebar-note {
#             border: 1px solid var(--line);
#             background: var(--panel-2);
#             border-radius: 12px;
#             padding: .8rem .9rem;
#             color: var(--muted);
#             font-size: .78rem;
#             line-height: 1.55;
#         }

#         .eyebrow {
#             color: var(--blue);
#             font-size: .72rem;
#             font-weight: 700;
#             letter-spacing: .14em;
#             text-transform: uppercase;
#             margin-bottom: .55rem;
#         }

#         .subtitle {
#             font-size: 1.02rem;
#             color: #475569;
#             margin: .35rem 0 0;
#         }

#         .subtitle-2 {
#             font-size: .9rem;
#             color: var(--muted);
#             margin: .35rem 0 0;
#         }

#         .status {
#             display: inline-flex;
#             align-items: center;
#             gap: 8px;
#             padding: 7px 13px;
#             border: 1px solid #c7d2fe;
#             border-radius: 999px;
#             color: var(--blue);
#             background: var(--blue-soft);
#             font-size: .8rem;
#             font-weight: 600;
#             white-space: nowrap;
#         }

#         .status-dot {
#             width: 7px;
#             height: 7px;
#             border-radius: 50%;
#             background: var(--teal);
#             box-shadow: 0 0 0 4px rgba(52,211,153,.15);
#         }

#         .hero {
#             display: flex;
#             align-items: flex-end;
#             justify-content: space-between;
#             gap: 2rem;
#             margin-bottom: 2rem;
#             padding-bottom: 1.5rem;
#             border-bottom: 1px solid var(--line);
#         }

#         .card {
#             background: var(--panel);
#             border: 1px solid var(--line);
#             border-radius: 18px;
#             padding: 1.35rem 1.45rem;
#             margin-bottom: 1rem;
#             box-shadow: 0 8px 24px rgba(15,23,42,.06);
#         }

#         .card-title {
#             color: var(--text);
#             font-family: 'Space Grotesk', sans-serif;
#             font-weight: 600;
#             font-size: 1.02rem;
#             margin-bottom: .25rem;
#         }

#         .card-copy {
#             color: var(--muted);
#             font-size: .87rem;
#             line-height: 1.55;
#         }

#         .metric-card {
#             background: var(--panel);
#             border: 1px solid var(--line);
#             border-radius: 14px;
#             padding: 1rem 1.05rem;
#             min-height: 104px;
#             margin-bottom: .75rem;
#             box-shadow: 0 4px 14px rgba(15,23,42,.05);
#         }

#         .metric-label {
#             color: var(--muted);
#             font-size: .72rem;
#             text-transform: uppercase;
#             letter-spacing: .09em;
#             font-weight: 600;
#         }

#         .metric-value {
#             color: var(--text);
#             font-family: 'Space Grotesk', sans-serif;
#             font-size: 1.4rem;
#             font-weight: 700;
#             margin-top: .45rem;
#             overflow-wrap: anywhere;
#         }

#         .real {
#             color: var(--teal) !important;
#         }

#         .generated {
#             color: var(--red) !important;
#         }

#         .pill {
#             display: inline-flex;
#             align-items: center;
#             gap: 7px;
#             margin-top: .5rem;
#             padding: 5px 11px;
#             border-radius: 999px;
#             font-size: .74rem;
#             font-weight: 700;
#             letter-spacing: .04em;
#         }

#         .pill.real {
#             background: var(--teal-soft);
#             border: 1px solid #a7f3d0;
#         }

#         .pill.generated {
#             background: var(--red-soft);
#             border: 1px solid #fecaca;
#         }

#         .section {
#             margin-top: 2.1rem;
#             margin-bottom: .8rem;
#             display: flex;
#             align-items: center;
#             justify-content: space-between;
#             gap: 1rem;
#         }

#         .section-note {
#             color: var(--muted);
#             font-size: .8rem;
#         }

#         .stButton > button,
#         .stButton > button p,
#         .stButton > button span,
#         .stDownloadButton > button,
#         .stDownloadButton > button p,
#         .stDownloadButton > button span {
#             color: #ffffff !important;
#         }

#         .stButton > button {
#             border-radius: 10px;
#             border: 1px solid var(--blue);
#             background: var(--blue);
#             color: #ffffff !important;
#             font-weight: 700;
#             min-height: 44px;
#         }

#         .stButton > button:hover {
#             border-color: #4338ca;
#             background: #4338ca;
#             color: #ffffff !important;
#         }

#         .stDownloadButton > button {
#             border-radius: 10px;
#             border: 1px solid var(--blue);
#             background: var(--blue);
#             color: #ffffff !important;
#             font-weight: 700;
#             min-height: 44px;
#         }

#         .stDownloadButton > button:hover {
#             border-color: #4338ca;
#             background: #4338ca;
#             color: #ffffff !important;
#         }

#         [data-testid="stFileUploader"] {
#             background: var(--panel-2);
#             border: 1px dashed var(--line-strong);
#             border-radius: 12px;
#             padding: .5rem;
#         }

#         [data-testid="stMetric"] {
#             background: var(--panel);
#             border: 1px solid var(--line);
#             padding: 1rem;
#             border-radius: 12px;
#         }

#         [data-testid="stMetricLabel"] {
#             color: var(--muted);
#         }

#         [data-testid="stMetricValue"] {
#             color: var(--text);
#         }

#         [data-testid="stImage"] img {
#             border-radius: 14px;
#             border: 1px solid var(--line);
#         }

#         .disclaimer {
#             border: 1px solid var(--amber-line);
#             background: var(--amber-bg);
#             border-radius: 14px;
#             padding: 1rem 1.15rem;
#             color: #92400e;
#             font-size: .86rem;
#             line-height: 1.65;
#         }

#         .footer {
#             border-top: 1px solid var(--line);
#             margin-top: 2.5rem;
#             padding-top: 1rem;
#             color: #94a3b8;
#             font-size: .75rem;
#         }

#         .stSelectbox > div > div {
#             background-color: var(--panel-2);
#             border-color: var(--line);
#             color: var(--text);
#         }

#         .stSelectbox svg {
#             color: var(--muted);
#         }

#         .stProgress > div > div {
#             background-color: transparent;
#         }

#         .stProgress > div {
#             background-color: #e2e8f0;
#         }

#         .stProgress,
#         .stProgress p,
#         .stProgress span,
#         [data-testid="stProgress"] {
#             color: #ffffff !important;
#         }

#         div[data-testid="stAlert"] {
#             background-color: var(--panel-2);
#             color: var(--text);
#         }

#         .stSpinner > div {
#             color: var(--blue);
#         }

#         @media (max-width: 900px) {
#             .block-container {
#                 padding: 1.5rem 1rem 3rem;
#             }

#             .hero {
#                 display: block;
#             }

#             .hero .status {
#                 margin-top: 1rem;
#             }

#             h1 {
#                 font-size: 2rem !important;
#             }
#         }
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )


# def metric_card(label: str, value, class_name: str = "") -> None:
#     st.markdown(
#         f"""
#         <div class="metric-card">
#             <div class="metric-label">{label}</div>
#             <div class="metric-value {class_name}">{value}</div>
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )


# def section(title: str, note: str = "") -> None:
#     st.markdown(
#         f"""
#         <div class="section">
#             <h2>{title}</h2>
#             <div class="section-note">{note}</div>
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )


# def card_open(title: str, copy: str = "") -> None:
#     st.markdown(
#         f"""
#         <div class="card">
#             <div class="card-title">{title}</div>
#             <div class="card-copy">{copy}</div>
#         """,
#         unsafe_allow_html=True,
#     )


# def card_close() -> None:
#     st.markdown("</div>", unsafe_allow_html=True)


# def render_sidebar() -> str:
#     with st.sidebar:
#         st.markdown(
#             '<div class="brand"><span class="brand-mark">R</span>RealTrace AI</div>'
#             '<div class="brand-sub">Generalizable forensic intelligence framework for authenticity '
#             "verification of AI-generated visual content.</div>",
#             unsafe_allow_html=True,
#         )

#         st.markdown(
#             '<div class="sidebar-label">Detection Configuration</div>',
#             unsafe_allow_html=True,
#         )

#         selected = st.selectbox(
#             "Select Detection Model",
#             list(MODEL_OPTIONS.keys()),
#             index=4,
#         )

#         st.caption(
#             f"Checkpoint: `{MODEL_OPTIONS[selected]}`"
#         )

#         st.markdown(
#             '<div class="sidebar-label">Analysis Pipeline</div>',
#             unsafe_allow_html=True,
#         )

#         st.markdown(
#             """
#             <div class="pipeline">
#                 <span class="step-no">01</span><b>Visual classification</b><br/>
#                 <span class="step-no">02</span><b>Confidence analysis</b><br/>
#                 <span class="step-no">03</span><b>Grad-CAM explanation</b><br/>
#                 <span class="step-no">04</span><b>FFT analysis</b><br/>
#                 <span class="step-no">05</span><b>DCT analysis</b><br/>
#                 <span class="step-no">06</span><b>Forensic report</b>
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )

#         st.markdown(
#             '<div class="sidebar-label">System Note</div>',
#             unsafe_allow_html=True,
#         )

#         st.markdown(
#             '<div class="sidebar-note">Model-based analysis for research and demonstration purposes. '
#             "Results should be interpreted with scientific caution.</div>",
#             unsafe_allow_html=True,
#         )

#     return selected


# def render_header() -> None:
#     st.markdown(
#         """
#         <div class="hero">
#             <div>
#                 <div class="eyebrow">Digital forensics workstation</div>
#                 <h1>RealTrace AI</h1>
#                 <p class="subtitle">AI-Generated Visual Content Authenticity Verification</p>
#                 <p class="subtitle-2">Deep-learning classification with explainable AI and frequency-domain forensic analysis.</p>
#             </div>
#             <div class="status">
#                 <span class="status-dot"></span>
#                 Forensic Analysis System
#             </div>
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )


# def render_result_card(
#     result: dict,
#     selected_model: str,
#     prediction_class: str,
# ) -> None:
#     section(
#         "Classification Result",
#         "Model output",
#     )

#     c1, c2, c3 = st.columns(3)

#     with c1:
#         st.markdown(
#             f"""
#             <div class="metric-card">
#                 <div class="metric-label">Prediction</div>
#                 <div class="metric-value {prediction_class}">
#                     {result["prediction"]}
#                 </div>
#                 <div class="pill {prediction_class}">
#                     {"Classified as authentic capture" if prediction_class == "real" else "Classified as AI-generated"}
#                 </div>
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )

#     with c2:
#         metric_card(
#             "Model confidence",
#             f'{result["confidence"] * 100:.2f}%',
#         )

#     with c3:
#         metric_card(
#             "Selected model",
#             selected_model,
#         )


# def render_probability_section(
#     result: dict,
# ) -> None:
#     section(
#         "Prediction Probabilities",
#         "Softmax output",
#     )

#     p1, p2 = st.columns(2)

#     with p1:
#         card_open(
#             "Real Probability",
#             "Likelihood assigned to the authentic-capture class.",
#         )

#         st.progress(
#             float(result["real_probability"]),
#             text=f'{result["real_probability"] * 100:.2f}%',
#         )

#         card_close()

#     with p2:
#         card_open(
#             "AI-Generated Probability",
#             "Likelihood assigned to the AI-generated class.",
#         )

#         st.progress(
#             float(result["ai_probability"]),
#             text=f'{result["ai_probability"] * 100:.2f}%',
#         )

#         card_close()

#     st.info(
#         "Model confidence represents the model's certainty in its classification. "
#         "It is not the probability that the image is genuinely authentic. "
#         "Images from unseen generators may be misclassified with high confidence."
#     )


# def render_gradcam_section(
#     result: dict,
# ) -> None:
#     section(
#         "Explainable AI — Grad-CAM",
#         "Class-activation overlay",
#     )

#     st.image(
#         result["gradcam_overlay"],
#         caption="Regions contributing strongly to the model prediction",
#         use_container_width=True,
#     )

#     st.info(
#         "Grad-CAM indicates image regions that contributed strongly to the model's prediction. "
#         "A highlighted region is not definitive proof that the region itself is fake."
#     )


# def render_frequency_section(
#     result: dict,
# ) -> None:
#     section(
#         "Frequency-Domain Forensics",
#         "Spectral representations",
#     )

#     f1, f2 = st.columns(2)

#     with f1:
#         card_open(
#             "FFT Magnitude Spectrum",
#             "Frequency representation generated using the Fast Fourier Transform.",
#         )

#         fft_fig = plt.figure(
#             figsize=(6, 5)
#         )

#         plt.imshow(
#             result["fft"],
#             cmap="gray",
#         )

#         plt.axis("off")
#         plt.tight_layout()

#         st.pyplot(
#             fft_fig
#         )

#         plt.close(
#             fft_fig
#         )

#         card_close()

#     with f2:
#         card_open(
#             "DCT Magnitude Spectrum",
#             "Spatial-frequency representation generated using the Discrete Cosine Transform.",
#         )

#         dct_fig = plt.figure(
#             figsize=(6, 5)
#         )

#         plt.imshow(
#             result["dct"],
#             cmap="gray",
#         )

#         plt.axis("off")
#         plt.tight_layout()

#         st.pyplot(
#             dct_fig
#         )

#         plt.close(
#             dct_fig
#         )

#         card_close()


# def render_summary_section(
#     result: dict,
#     selected_model: str,
#     prediction_class: str,
# ) -> None:
#     section(
#         "Analysis Summary",
#         "Values returned by the inference pipeline",
#     )

#     s1, s2, s3 = st.columns(3)

#     with s1:
#         metric_card(
#             "Selected model",
#             selected_model,
#         )

#         metric_card(
#             "Internal model name",
#             result["model_name"],
#         )

#     with s2:
#         metric_card(
#             "Predicted class",
#             result["prediction"],
#             prediction_class,
#         )

#         metric_card(
#             "Model confidence",
#             f'{result["confidence"] * 100:.2f}%',
#         )

#     with s3:
#         metric_card(
#             "Real probability",
#             f'{result["real_probability"] * 100:.2f}%',
#         )

#         metric_card(
#             "AI-generated probability",
#             f'{result["ai_probability"] * 100:.2f}%',
#         )


# def render_report_section(
#     image: Image.Image,
#     result: dict,
# ) -> None:
#     section(
#         "Forensic Analysis Report",
#         "PDF export",
#     )

#     card_open(
#         "Downloadable report",
#         "Download a PDF containing the classification result, "
#         "explainability visualization, and frequency-domain analysis.",
#     )

#     report = generate_report(
#         image,
#         result,
#     )

#     st.download_button(
#         "Download Forensic Analysis Report",
#         data=report.getvalue(),
#         file_name="RealTrace_AI_Forensic_Report.pdf",
#         mime="application/pdf",
#     )

#     card_close()


# def render_disclaimer() -> None:
#     st.markdown(
#         """
#         <div class="disclaimer">
#             <b>Scientific disclaimer</b><br/>
#             RealTrace AI provides model-based forensic analysis.
#             The classification, confidence score, Grad-CAM visualization
#             and frequency-domain representations should not be treated as
#             definitive forensic proof. Results may be less reliable for
#             AI generators or image distributions not represented during
#             model training.
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )


# def render_footer() -> None:
#     st.markdown(
#         '<div class="footer">'
#         "RealTrace AI · University final-year project demonstration · "
#         "Explainable, evidence-aware visual verification"
#         "</div>",
#         unsafe_allow_html=True,
#     )


# inject_styles()

# selected_model = render_sidebar()

# checkpoint_filename = MODEL_OPTIONS[
#     selected_model
# ]

# try:
#     checkpoint_path = get_checkpoint(
#         checkpoint_filename
#     )
# except Exception as error:
#     st.error("Failed to download model checkpoint.")
#     st.exception(error)
#     st.stop()

# render_header()

# section(
#     "Image Evidence",
#     "JPG · JPEG · PNG · WEBP",
# )

# card_open(
#     "Upload an image for examination",
#     "Evidence is analyzed only after you initiate the forensic workflow.",
# )

# uploaded_file = st.file_uploader(
#     "Upload image evidence",
#     type=[
#         "jpg",
#         "jpeg",
#         "png",
#         "webp",
#     ],
#     label_visibility="collapsed",
# )

# card_close()

# if uploaded_file is not None:
#     try:
#         image = Image.open(
#             uploaded_file
#         ).convert(
#             "RGB"
#         )

#         left, right = st.columns(
#             [1.45, 1],
#             gap="large",
#         )

#         with left:
#             st.image(
#                 image,
#                 caption="Evidence preview",
#                 use_container_width=True,
#             )

#         with right:
#             st.markdown(
#                 '<div class="card-title">Evidence metadata</div>',
#                 unsafe_allow_html=True,
#             )

#             metric_card(
#                 "File name",
#                 uploaded_file.name,
#             )

#             metric_card(
#                 "Dimensions",
#                 f"{image.width} × {image.height} px",
#             )

#             metric_card(
#                 "Format",
#                 uploaded_file.type or "RGB image",
#             )

#             analyze = st.button(
#                 "Analyze Image",
#                 type="primary",
#                 use_container_width=True,
#             )

#         if analyze:
#             with st.spinner(
#                 "Running forensic analysis..."
#             ):
#                 result = analyze_image(
#                     image,
#                     checkpoint_path,
#                 )

#             st.success(
#                 "Analysis completed successfully."
#             )

#             prediction_class = (
#                 "real"
#                 if str(
#                     result["prediction"]
#                 ).upper() == "REAL"
#                 else "generated"
#             )

#             render_result_card(
#                 result,
#                 selected_model,
#                 prediction_class,
#             )

#             render_probability_section(
#                 result,
#             )

#             render_gradcam_section(
#                 result,
#             )

#             render_frequency_section(
#                 result,
#             )

#             render_summary_section(
#                 result,
#                 selected_model,
#                 prediction_class,
#             )

#             render_report_section(
#                 image,
#                 result,
#             )

#             render_disclaimer()

#     except Exception as error:
#         st.error("Analysis failed. Error details:")
#         st.exception(error)

# render_footer()