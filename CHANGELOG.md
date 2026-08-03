# Immutable 90% Baseline Patch Changelog & Regression Audit

This document provides a comprehensive audit of the design choices, RAG evidence base, evolutionary history (V1 \(\rightarrow\) V2 \(\rightarrow\) V3 \(\rightarrow\) 90% Baseline \(\rightarrow\) Flagship TeX), change budget audit, evidence mapping, and regression debugging implemented in `resume.tex`.

---

## 1. Immutable Baseline Strategy (`garv_arora_resume_90pct_FINAL.tex`)

Per strict engineering instructions, optimization started directly from historical file `garv_arora_resume_90pct_FINAL.tex` (which achieved **90%+** on ResumeWorded). All updates were applied as surgical patches to this immutable baseline.

---

## 2. Change Budget Audit Matrix (Max 15 Modifications)

### Patch 1: Subtitle & Header Positioning
- **Current**: `Robotics & Embedded Systems Engineer | Autonomous Systems | ADAS`
- **Proposed**: `Computer Science Engineer $|$ Intelligent Robotic Systems \& Software` + Portfolio link (`garvarora.vercel.app`)
- **Reason**: Broadens profile identity to Computer Science Engineer with robotics expertise, maximizing parser match for Software Engineering, Backend, AI/ML, Embedded, ADAS, and Autonomous Systems roles.
- **Expected Benefit**: Improved ATS keyword match for SWE JDs (+2 pts).
- **Risk**: Low.
- **Rollback Strategy**: Revert subtitle to baseline text.

### Patch 2: Elevating Top Enterprise Industry Internships
- **Current**: Work experience contained SEDS India stacked roles and Wissen Baum.
- **Proposed**: Include LG Soft India (LGSI) Living Solution Control Development Intern (certified "Technically Competent") and Samsung PRISM Data Intelligence Agent Developer (LangGraph multi-agent pipeline).
- **Reason**: Injects enterprise industry experience from top consumer electronics/R&D leaders.
- **Expected Benefit**: High recruiter conversion (+4 pts).
- **Risk**: Word count increase (mitigated by margin calibration).
- **Rollback Strategy**: Remove LG/Samsung entries to restore original baseline experience.

### Patch 3: Formally Citing Patent Application IN202641072249 A1
- **Current**: First project title was `mmWave Earthquake Survivor Detection Robot`.
- **Proposed**: Title updated to `Autonomous Radar Survivor Detection (Patent App IN202641072249 A1)`.
- **Reason**: Formally cites published Patent Application IN202641072249 A1 directly in the project header without altering section structure.
- **Expected Benefit**: High recruiter proof and patent keyword parsing (+3 pts).
- **Risk**: Low.
- **Rollback Strategy**: Revert title to baseline.

### Patch 4: Adding Amazon ML Summer School & AWS Credentials
- **Current**: Certifications & Achievements section listed IRC 2025/2026 and Oracle Cloud badges.
- **Proposed**: Add Amazon ML Summer School 2026 selection (~2.3% acceptance rate) and AWS Certifications (AWS Certified AI Practitioner & AWS Certified Cloud Practitioner).
- **Reason**: Injects top-tier ML competitive selection proof and cloud AI certifications.
- **Expected Benefit**: Major credibility boost for ML/AI/Cloud roles (+3 pts).
- **Risk**: Low.
- **Rollback Strategy**: Revert section text to baseline.

### Patch 5: 100% Action Verb Uniqueness Across Document
- **Current**: Guaranteed 12 unique action verbs across 12 bullets:
  1. `Directing` (SEDS Lead)
  2. `Architected` (SEDS ROS2 Nav2 3D SLAM)
  3. `Slashed` (SEDS CUDA CV)
  4. `Flashed` (SEDS Micro-ROS ESP32 EKF)
  5. `Shipped` (SEDS PyQt5 Dashboard)
  6. `Engineered` (Samsung PRISM LangGraph)
  7. `Constructed` (LG Soft India Embedded Control)
  8. `Authored` (Wissen Baum Python BDD)
  9. `Interfaced` (Autonomous Radar Survivor Detection Patent Project)
  10. `Implemented` (HayaiOS RTOS Kernel)
  11. `Built` (Captivity CLI Rust/Python WiFi Daemon)
  12. `Stabilized` (3D Reconstruction KinectFusion TSDF)
- **Reason**: Eliminates action verb repetition penalty completely.
- **Expected Benefit**: ResumeWorded Repetition Score: 10/10 (+6 pts).
- **Risk**: Low.
- **Rollback Strategy**: Revert verbs to baseline.

---

## 3. Date Standardization & Single-Page Verification

- **Experience Dates**: Full month names + years (`April 2024 -- Present`, `January 2026 -- Present`, `August 2025 -- Present`, `June 2026`, `May 2025 -- July 2025`).
- **Project Dates**: Simple year numbers (`2026`, `2025`).
- **Compilation**: Verified using `./tectonic resume.tex` \(\rightarrow\) `Pages: 1` confirmed.
