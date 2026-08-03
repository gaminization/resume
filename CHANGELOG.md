# Flagship Resume Engineering & Evolutionary Changelog

This document provides a comprehensive audit of the design choices, RAG evidence base, evolutionary history (V1 \(\rightarrow\) V2 \(\rightarrow\) V3 \(\rightarrow\) Flagship TeX), peer resume analysis, and score fixes implemented in `resume.tex`.

---

## 1. RAG Evidence Base & Traceability Audit

Every line in `resume.tex` is directly traceable to verified primary source documents in the workspace:

- **Patent Published (App IN202641072249 A1)**: Traceable to `my_docs/Patent Publish.pdf` (FMCW 24GHz mmWave radar, ultrasonic array, IMU dead-reckoning, ESP32, dynamic confidence grid decay formula \(C = \max(0, C - \beta \Delta t)\)).
- **Amazon ML Summer School 2026**: Traceable to `my_docs/main` (Selected in Top 3,000 out of 1,30,000+ applicants across India, ~2.3% acceptance rate).
- **International Rover Challenge (IRC)**: Traceable to `my_docs/main` and `my_docs/vyadh` (13th Global Rank 2025, 17th Global Rank 2026 with Team Vyadh @ SEDS VIT).
- **LG Soft India (LGSI)**: Traceable to `my_docs/LG_Certificate.pdf` (Living Solution Development – Living Solution Control Development, HS/ES India Lab, 06/2026 -- 06/2026, officially certified as "Technically Competent").
- **Samsung PRISM**: Traceable to `my_docs/samprism` and `my_docs/PRISM_Worklet_Data Intelligence Agent_Phase 1.pptx` (Multi-agent LangGraph pipeline, FastAPI, Redis, PostgreSQL, Qdrant, spaCy NLP, Presidio PII anonymization, SPDX license enforcement, BERTopic, MinHash LSH deduplication, MemorySaver HITL review pause).
- **Wissen Baum Engineering Solutions**: Traceable to `my_docs/Wissenbaum_Report` (Software Automation Intern, May 2025 -- July 2025, Python BDD testing with Gherkin/Behave, pytest, Playwright, Cypress, GitLab CI 40% speedup from ~10m to ~6m, 80%+ manual testing reduction).
- **SEDS India (SEDS VIT)**: Traceable to `my_docs/vyadh` (R&D Lead Jan 2026--Present directing 2 teams across Team Vyadh & Team Ardra; Autonomous Systems Developer Apr 2024--Jan 2026 architecting ROS2 Nav2 RTAB-Map 3D Visual SLAM on Intel RealSense D455 cutting manual teleop by 70%, CUDA YOLOv8 V4L2 zero-copy cutting CV latency by 60% & boosting QPS 4x, Micro-ROS ESP32 EKF fusion cutting drift by 40%, PyQt5 telemetry dashboard).
- **Projects & PyPI Packages**:
  - `teleop-cursor`: Traceable to `my_docs/teleop-cursor` & PyPI package `pypi.org/project/teleop-cursor` (ROS 2 desktop mouse teleoperation node, 10 Hz callback frequency).
  - `HayaiOS`: Traceable to `my_docs/projects` (Bare-metal RTOS kernel in C & ARM Assembly on ARM Cortex-M4, <50 assembly instruction context switch, 1 ms tick, IPC mutexes/semaphores, register HAL).
  - `Captivity CLI`: Traceable to `my_docs/captivity` & PyPI package `pypi.org/project/captivity-cli` (Rust + Python captive portal login daemon, <50ms HTTP 204 probing, systemd background service, D-Bus NetworkManager monitoring, keyring encryption, TCP socket IPC).
  - `3D Reconstruction`: Traceable to `my_docs/projects` (RealSense D455 depth + 6-DOF IMU complementary filter for KinectFusion TSDF reconstruction, 50% tracking failure reduction).

---

## 2. Resume Evolution Audit (V1 \(\rightarrow\) V2 \(\rightarrow\) V3 \(\rightarrow\) Flagship TeX)

- **V1 \(\rightarrow\) V2**: V1 suffered from unquantified duty bullets ("worked on computer vision", "helped with team"), generic section titles, and low ATS scores (~52-56%). V2 introduced STAR/XYZ metrics (70% teleoperation cut, 60% CV latency cut, 40% odometry drift cut), strong action verbs, and clear categorical skill grouping.
- **V2 \(\rightarrow\) V3**: V3 introduced stacked role formatting for SEDS India (R&D Lead Jan 2026--Present and Autonomous Systems Dev Apr 2024--Jan 2026), added mmWave survivor bot, HayaiOS RTOS, 3D Reconstruction, and Wissen Baum automation internship.
- **V3 Bottlenecks & Deductions Fixed in Flagship TeX**:
  1. *Elevated Patent IN202641072249 A1*: V3 buried the patent as a generic project without Application Number. Flagship TeX elevates it to a top-line section: **Patent Published (App IN202641072249 A1)**.
  2. *Elevated Amazon ML Summer School (Top 3k/1.3L)*: Completely missing in V3; added as a top-line national competitive credential.
  3. *Added Enterprise Experience*: Added LG Soft India (certified "Technically Competent") and Samsung PRISM (LangGraph multi-agent pipeline).
  4. *Added PyPI Links*: Explicitly linked published PyPI packages (`captivity-cli` and `teleop-cursor`).
  5. *Fixed Date Ordering & Consistency (Score 4/10 on ResumeWorded commit 2)*: Resolved date out-of-order deductions by ordering all Work Experience entries (`Jun 2026`, `Jan 2026`, `Aug 2025`, `May 2025`, `Apr 2024`) and Projects (`Feb 2026`, `Jan 2026`, `Nov 2025`, `Aug 2025`) in **strict reverse chronological order** with uniform Month Year formatting.

---

## 3. Peer Resume Analysis (`other's resume/`)

From auditing peer resumes (Rishit Mohan, Ruhi Doshi, Aditya, Rakshith, Medha):
- **Positive Patterns Adopted**:
  - Top-line presentation of key honors and certifications before work experience to establish immediate recruiter credibility.
  - Grouping skills into 4-5 core domain categories.
  - Inline bold technology tags for projects (`\textbf{Project Name} $|$ \emph{Tech Stack}`).
  - Clean inline school education display (B.Tech CGPA alongside Class X and XII percentages).
- **Weaknesses Avoided**:
  - Avoided listing generic software tools (MS Word, MS Excel, VirtualBox, Scratch).
  - Avoided multi-page sprawl for early-career profiles.
  - Avoided unquantified duty-focused bullet points.

---

## 4. Jake's Resume Foundation & Enhancements

Built on `jake's template/resume/resume.tex` with key modifications:
1. **Custom Spacing Calibration**: Adjusted geometry margins to `top=0.30in, bottom=0.30in, left=0.38in, right=0.38in` and `\titleformat{\section}` vertical space (`\vspace{-7pt}`) to guarantee a strict 1-page fit without text crowding.
2. **Plaintext Hyperlink Configuration**:
   ```latex
   \usepackage[hidelinks]{hyperref}
   \urlstyle{same}
   ```
   Configured `hyperref` so all URLs display plain uncolored text that is fully clickable in PDF and visually identical to plain text when printed.

---

## 5. Positioning Strategy: CS Engineer Specializing in Intelligent Robotic Systems

The candidate is positioned as a **Computer Science Engineer specializing in Intelligent Robotic Systems & Software**. This communicates deep cross-disciplinary mastery across:
- **Software Engineering & Systems**: Linux D-Bus, systemd, Socket IPC, Python, C++, Rust, Multi-threading.
- **Robotics & Autonomous Systems**: ROS2 (Nav2, MoveIt2), RTAB-Map 3D Visual SLAM, Micro-ROS, EKF fusion, mmWave Radar.
- **Perception & Machine Learning**: CUDA, OpenCV, YOLOv8, PyTorch, RealSense SDK.
- **Embedded & Firmware**: ARM Cortex-M4 bare-metal C/Assembly, ESP32, FreeRTOS, HAL, I2C/SPI/UART.
- **Backend & AI Architecture**: LangGraph, FastAPI, Redis, PostgreSQL, Qdrant vector memory.

This positioning ensures maximum interview conversion across Software Engineering, Robotics, Autonomous Systems, Embedded Systems, Computer Vision, ADAS, and AI/ML roles.
