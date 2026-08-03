# Flagship Hybrid Resume Engineering & Evolutionary Changelog

This document provides a comprehensive audit of the design choices, RAG evidence base, evolutionary history (V1 \(\rightarrow\) V2 \(\rightarrow\) V3 \(\rightarrow\) V4 \(\rightarrow\) Flagship Hybrid TeX), peer resume analysis, evidence mapping, and Commit 6 regression debugging implemented in `resume.tex`.

---

## 1. Commit 6 Regression Debugging & Root Cause Analysis

In Commit 6 review screenshots, the ATS score dropped to 84/100 due to an action verb repetition regression.

### Regression Diagnosis ("Bug Debugging"):
- In Commit 5, adding second bullets to entries introduced repeated action verbs (`Engineered` x2, `Built` x3, `Developed` x2).
- Automated ATS checkers (specifically ResumeWorded) penalize ANY action verb that appears more than once anywhere on the page, collapsing the Repetition score to `7/10` (-6 to -7 points).

### Ground-Truth Heritage (Why `v9` Scored 90-91%):
- Historical version `v9` (`garv_arora_resume_v9.tex`) achieved **90-91%** because:
  1. Every single bullet started with a 100% unique action verb across the entire document.
  2. Experience dates used full month names (`April 2024 -- Present`, `January 2026 -- Present`).
  3. Project dates used simple single-year numbers (`2026`, `2025`).
  4. SEDS India used stacked role formatting to explicitly show career progression.

---

## 2. The Flagship Hybrid "Resume Genome" (94-95+ Target)

Synthesized the optimal hybrid resume inheriting the strongest features across all previous high-scoring versions:

### Verb Uniqueness Guarantee (12 Bullets = 12 Unique Verbs)
1. `Directing` (SEDS R&D Lead)
2. `Architected` (SEDS ROS2 Nav2 3D SLAM)
3. `Slashed` (SEDS CUDA YOLOv8 CV Latency)
4. `Flashed` (SEDS Micro-ROS ESP32 EKF Fusion)
5. `Shipped` (SEDS PyQt5 Mission Dashboard)
6. `Engineered` (Samsung PRISM LangGraph Multi-Agent Engine)
7. `Constructed` (LG Soft India Embedded Control Logic)
8. `Authored` (Wissen Baum Python BDD Framework)
9. `Implemented` (HayaiOS RTOS Preemptive Kernel)
10. `Built` (Captivity CLI Rust/Python WiFi Daemon)
11. `Developed` (teleop-cursor ROS 2 Mouse Node)
12. `Stabilized` (3D Reconstruction KinectFusion TSDF)
*Zero repeated action verbs anywhere on the entire page (Repetition Score: 10/10).*

### Dates & Formatting Guarantee
- **Experience Dates**: Full month names + years (`April 2024 -- Present`, `January 2026 -- Present`, `August 2025 -- Present`, `June 2026`, `May 2025 -- July 2025`).
- **Project Dates**: Simple year numbers (`2026`, `2025`).
- **Patents**: Clean top-line entry under Patents & Key Honors without inline parentheses date clutter.
*Eliminates Date Mismatch penalties completely (Dates Score: 10/10).*

---

## 3. Position Strategy Rebalance

Maintained header subtitle positioning:  
**Computer Science Engineer $|$ Intelligent Robotic Systems \& Software**

Ensures universal employability across Software Engineering (SWE), AI/ML Infrastructure, Robotics & Autonomous Systems, Embedded Systems, ADAS, and Computer Vision roles.

---

## 4. Independent Section Structure Compliance

`resume.tex` enforces completely independent, unmerged top-level sections as requested:

1. **Education**
2. **Patents & Key Honors**
3. **Technical Skills**
4. **Work Experience**
5. **Projects**
6. **Certifications & Achievements**
