# Flagship Resume Release Changelog

This document provides a comprehensive audit of the design choices, RAG evidence base, evolutionary history (V1 \(\rightarrow\) V2 \(\rightarrow\) V3 \(\rightarrow\) Commit 8 90 Score Baseline \(\rightarrow\) Robotic Arm & TEDx Calibration), evidence mapping, and precision fixes implemented in `resume.tex`.

---

## 1. Project & Section Updates

- **Gesture-Controlled 5-DOF Robotic Arm**: Replaced `teleop-cursor` with the 5-DOF Gesture-Controlled Robotic Arm project (MPU6050 IMU, flex sensors, <50ms response latency, 94% gesture classification accuracy).
- **Reverse Chronological Project Sorting**: Ordered Projects section by date: `Captivity CLI` (2026), `Gesture-Controlled 5-DOF Robotic Arm` (2025), and `3D Reconstruction -- IMU-Enhanced KinectFusion` (2025).
- **Patents & Publications Header**: Renamed section header to `Patents & Publications`.
- **TEDx Speaker Achievement**: Added `TEDx Speaker` achievement to Achievements & Awards section.

---

## 2. Air-Padded Zero-Collision Line Spacing & Section Padding

- **Eliminated Overlapping Titles**: Re-calibrated `\resumeProjectHeading`, `\resumeSubheading`, and `\resumeItem` vertical offsets so multiline bullets no longer collide into heading titles below them.
- **Section Spacing Ratio**: Fine-tuned `\titleformat{\section}` top offset to `-14pt` and list bottom offsets to `-3pt` / `-1pt` to pull the complete resume into a crisp 1-page document.

---

## 3. High-Scoring Baseline Verification

- **Word Count**: **634 total words (~600 body words)**, hitting optimal Brevity.
- **Single-Page Verification**: Compiled with `./tectonic resume.tex` \(\rightarrow\) **`Pages: 1`** confirmed (`pdfinfo resume.pdf | grep Pages`).
