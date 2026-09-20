# Faed Ahmed Arnob — Academic & Industry Research Portfolio

A modern, responsive, accessible personal portfolio website built with pure **HTML5, Vanilla CSS, and JavaScript**. Designed for instant, zero-build deployment to **GitHub Pages**.

---

## 🚀 Live Preview Locally
Simply double-click `index.html` to open it in any web browser (Chrome, Edge, Safari, Firefox), or run a lightweight local server:

```powershell
# In PowerShell / Terminal:
cd "c:\Users\faeda\Storage\Faed Docs\Jobs\portfolio"
python -m http.server 8000
```
Then visit [http://localhost:8000](http://localhost:8000) in your browser.

---

## 🌐 Deploying to GitHub Pages (Step-by-Step)

### Option A: Deploy to Your Root Domain `https://faedarnob.github.io/` (Recommended)

1. Go to [GitHub.com/new](https://github.com/new) and create a **Public** repository named exactly:
   ```
   faedarnob.github.io
   ```
   *(Make sure the repository name matches your username: `faedarnob.github.io`)*

2. In your terminal / PowerShell, initialize and push these files:
   ```powershell
   cd "c:\Users\faeda\Storage\Faed Docs\Jobs\portfolio"
   git init -b main
   git config user.name "Faed Ahmed Arnob"
   git config user.email "faed.arnob60@gmail.com"
   git add .
   git commit -m "Initial commit: Faed Ahmed Arnob Research Portfolio and Academic CV"
   git remote add origin https://github.com/faedarnob/faedarnob.github.io.git
   git push -u origin main
   ```

3. **That's it!** GitHub Pages will automatically build and publish your site at:
   👉 **`https://faedarnob.github.io/`**

---

### Option B: Deploy to a Project Repository (e.g., `https://faedarnob.github.io/portfolio/`)

If you prefer keeping the repository name as `portfolio`:
1. Create a repository named `portfolio` on GitHub.
2. Push your files:
   ```powershell
   cd "c:\Users\faeda\Storage\Faed Docs\Jobs\portfolio"
   git init -b main
   git config user.name "Faed Ahmed Arnob"
   git config user.email "faed.arnob60@gmail.com"
   git add .
   git commit -m "Initial commit: Faed Ahmed Arnob Research Portfolio"
   git remote add origin https://github.com/faedarnob/portfolio.git
   git push -u origin main
   ```
3. In GitHub, go to **Settings** > **Pages** > Under **Branch**, select `main` and `/ (root)` > Click **Save**.
4. Your site will be live at `https://faedarnob.github.io/portfolio/`.

---

## 📁 Repository Structure

```
portfolio/
├── index.html                   # Main single-page application & SEO metadata
├── styles.css                   # Responsive design system, dark & light themes, glassmorphism
├── script.js                    # Interactive theme toggle, category filters, BibTeX & email copy
├── README.md                    # Deployment guide and documentation
└── assets/
    ├── Faed_Ahmed_Arnob_Academic_CV.pdf   # Direct download PDF of academic CV
    └── images/
        ├── avatar.jpg                    # Profile portrait
        ├── crash_heatmap_manhattan.png   # Manhattan crash risk research figure
        ├── expected_crashes_panel.png    # Infrastructure-ADAS panel figure
        ├── lidar_pipeline.svg            # Trajectory-aligned LiDAR & VLM diagram
        ├── arise_diagram.svg             # ARise multimodal sensing diagram
        ├── traffic_edge.svg              # Edge YOLO traffic enforcement diagram
        └── favicon.svg                   # Monogram brand icon
```

---

## 🎨 Key Features & Highlights
- **Dual Audience Framing:** Structured to impress both **autonomous vehicle / robotics industry recruiters** (Waymo, Cruise, Zoox, Tesla) and **academic conference committees** (TRB, IEEE, ASCE).
- **Persistent Dark/Light Mode:** Seamlessly toggles between sleek deep-space dark mode and crisp academic light mode, remembering the user's preference via `localStorage`.
- **Dynamic Research & Publication Filtering:** Filter by domain (3D LiDAR, Safety AI, Human Sensing) and publication type (Conference, Journal, Poster).
- **One-Click Utilities:** Copy BibTeX citations, copy email address, and direct CV download with animated toast confirmations.
- **Print-to-CV Ready:** Features a dedicated print stylesheet (`@media print`) so pressing `Ctrl+P` produces an ATS-friendly, clean resume document.
