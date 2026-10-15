# 🛡️ Project HeritageShield
**Digital Artifact Forensics & Epigraphy Restoration Pipeline**
<img width="1285" height="656" alt="Screenshot 2026-03-25 225142" src="https://github.com/user-attachments/assets/dbdad97a-25c0-4e7a-b207-e49628ba8656" />

## Overview!

Project HeritageShield is a dual-core computer vision web application designed to safeguard regional historical artifacts. It provides a unified pipeline to detect hyper-realistic Generative AI forgeries (Midjourney, DALL-E) of architectural sites, while simultaneously offering digital restoration tools to extract and read heavily weathered, authentic stone inscriptions.

## Core Features
### Phase 1: Algorithmic Forgery Detection
* **EXIF Fingerprinting:** Scans hidden metadata for generative software signatures or intentional stripping.
* **Error Level Analysis (ELA):** Maps 8x8 JPEG macroblock compression to detect spliced anomalies.
* **Spatial Variance Telemetry:** Extracts high-frequency spatial noise to calculate physical entropy. Identifies the mathematical smoothing inherent in AI pixel prediction to output an Authenticity Confidence Score.

### Phase 2: Digital Epigraphy Restoration
* **CLAHE Enhancement:** Utilizes Contrast Limited Adaptive Histogram Equalization to boost micro-shadows in shallow carvings.
* **Bilateral Filtering:** Non-linear edge preservation smooths geological erosion without degrading carved groove depth.
* **Adaptive Gaussian Thresholding:** Isolates structural topology to render faded inscriptions as clean, readable documents.
<img width="914" height="542" alt="Screenshot 2026-03-25 225038" src="https://github.com/user-attachments/assets/b69b3f69-7e3b-4689-9838-0b5a0df78967" />

## Tech Stack
* **Backend:** Python, FastAPI, Uvicorn
* **Computer Vision Math:** OpenCV (`cv2`), NumPy
* **Image Processing:** Pillow (`PIL`)
* **Interface:** HTML/CSS (Jinja2 concepts via FastAPI responses)

## Installation & Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/HeritageShield.git
   cd HeritageShield
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: .\venv\Scripts\activate
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ignite the Local Server:**
   ```bash
   uvicorn app:app --reload
   ```

5. **Access the Dashboard:** 
   Open a web browser and navigate to `http://localhost:8000`.

## Generating Reports
Upload an image of a historical artifact or structural site. The system will automatically process the evidence through all forensic modules and generate a comprehensive, printable PDF report containing visual maps and statistical telemetry.

## Deploy to Vercel with GitHub Actions
The GitHub Actions workflow runs the dependency, compilation, and FastAPI import checks on pushes and pull requests. A successful push to `main` deploys the app to Vercel with the Vercel CLI. The Vercel project uses `app.py` as its FastAPI entrypoint and `vercel.json` sets a 60-second function duration.

1. Sign in to Vercel and create a project for this GitHub repository. Use the repository root as the project root. If Vercel's Git integration is enabled, disable automatic Git deployments so the GitHub Actions workflow is the only deploy trigger.
2. Install the Vercel CLI (`npm install --global vercel`) and link this repository to the project with `vercel link`. The generated `.vercel/project.json` contains the `orgId` and `projectId` values needed by the workflow; `.vercel/` is git-ignored.
3. Create a Vercel access token in Vercel account settings.
4. In GitHub, open **Settings → Secrets and variables → Actions** and add repository secrets named `VERCEL_TOKEN`, `VERCEL_ORG_ID`, and `VERCEL_PROJECT_ID` with the corresponding values.
5. Push or merge a change to `main`. GitHub Actions runs checks, then deploys to Vercel. Find the public URL in the deployment output or Vercel dashboard.

The workflow expects the production branch to be named `main`. Image uploads and derived previews are processed in temporary storage and embedded in the report response; the app does not retain uploaded evidence. Vercel Functions have request-size and execution-time limits, so very large images or long analyses may need a dedicated compute service and persistent object storage.
