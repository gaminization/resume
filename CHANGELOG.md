# Flagship Resume Release & Repository Structure Changelog

This document provides a comprehensive audit of design choices, RAG evidence base, repository architecture, and precision fixes implemented in `resume.tex`.

---

## 1. Professional Repository Restructuring

Restructured repository layout into an enterprise-grade hierarchy:
- **`resume.tex` & `resume.pdf`**: Kept clean in the root directory alongside `tectonic`, `LICENSE`, `README.md`, and `CHANGELOG.md`.
- **`docs/`**: Centralized verification mapping (`Evidence_Mapping.md`), ATS optimization reports (`Resume_Optimization_Report.md`), markdown resume source (`Garv_Arora_Resume_Master.md`), user credentials (`my_docs/`), and peer reviews (`reviews/`).
- **`archive/`**: Organized legacy baselines (`90score.tex`), historical resumes (`older_resumes/`), and reference templates (`jakes_template/`, `others_resumes/`).
- **`scripts/`**: Moved PDF build utilities (`generate_pdf.py`).

---

## 2. Project & Section Updates

- **Gesture-Controlled 5-DOF Robotic Arm**: Included in place of `teleop-cursor` (MPU6050 IMU, flex sensors, <50ms response latency, 94% gesture classification accuracy).
- **Reverse Chronological Project Sorting**: Ordered Projects section by date: `Captivity CLI` (2026), `Gesture-Controlled 5-DOF Robotic Arm` (2025), and `3D Reconstruction -- IMU-Enhanced KinectFusion` (2025).
- **Patents & Publications Header**: Renamed section header to `Patents & Publications`.
- **TEDx Speaker Achievement**: Added `TEDx Speaker` achievement to Achievements & Awards section.

---

## 3. Air-Padded Zero-Collision Line Spacing & Section Padding

- **Eliminated Overlapping Titles**: Re-calibrated `\resumeProjectHeading`, `\resumeSubheading`, and `\resumeItem` vertical offsets so multiline bullets no longer collide into heading titles below them.
- **Section Spacing Ratio**: Fine-tuned `\titleformat{\section}` top offset to `-14pt` and list bottom offsets to `-3pt` / `-1pt` to pull the complete resume into a crisp 1-page document.

---

## 4. High-Scoring Baseline Verification

- **Word Count**: **634 total words (~600 body words)**, hitting optimal Brevity.
- **Single-Page Verification**: Compiled with `./tectonic resume.tex` \(\rightarrow\) **`Pages: 1`** confirmed (`pdfinfo resume.pdf | grep Pages`).
