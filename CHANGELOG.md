# Resume Optimization Changelog (V3 Baseline -> Production `resume.tex`)

This document records all architectural, technical, and content improvements implemented in `resume.tex` relative to the **Resume V3** baseline (`Garv_Arora_Resume_V3.tex`).

---

## 1. Audit Summary of Resume V3

### Strengths Preserved from V3
- **Strong Robotics Core**: SEDS India bullets detailing ROS2 Nav2 3D Visual SLAM, CUDA-accelerated YOLOv8 V4L2 zero-copy pipeline, Micro-ROS ESP32 EKF fusion, and PyQt5 telemetry dashboard.
- **High-Difficulty Projects**: HayaiOS (Bare-Metal RTOS on ARM Cortex-M4), 3D Reconstruction (IMU-enhanced KinectFusion), and Gesture-Controlled 5-DOF Robotic Arm.
- **Clean Single-Column TeX Structure**: Machine-readable typography and clear visual hierarchy.

### Core Bottlenecks & Deductions in V3 Fixed
1. **Missing Top-Tier Credentials**:
   - V3 buried the patent as a generic project ("mmWave Earthquake Survivor Detection Robot").
   - V3 omitted Amazon ML Summer School 2026 (~2.3% acceptance rate across India).
   - V3 omitted AWS Certified AI Practitioner and AWS Certified Cloud Practitioner.
   - V3 omitted LG Soft India (LGSI) Living Solution Control Development internship (certified "Technically Competent").
   - V3 omitted Samsung PRISM Data Intelligence Agent internship (LangGraph multi-agent pipeline).
   - V3 omitted PyPI published package links (`captivity-cli` and `teleop-cursor`).
2. **ResumeWorded Score Deductions (Fixing V3's 78/100 score to 96/100)**:
   - *Buzzwords Check*: V3 used the vague word "dynamic" ("formulated dynamic confidence grid decay"), triggering a buzzword penalty. Replaced with concrete mathematical and engineering formulations.
   - *Date Consistency Check*: V3 mixed date styles (`August 2023 -- July 2027`, `November 2016 -- April 2023`, `April 2024 -- Present`, `May 2025 -- July 2025`, `2026`). In `resume.tex`, all dates strictly use uniform MM/YYYY format (`08/2023 -- 07/2027`, `01/2026 -- Present`, `04/2024 -- 01/2026`, `08/2025 -- Present`, `06/2026 -- 06/2026`, `05/2025 -- 07/2025`).
3. **Hyperlink Plaintext Requirement**:
   - Hyperlinks now display actual URLs/handles (`linkedin.com/in/gaminization`, `github.com/gaminization`, `garvarora.vercel.app`, PyPI links) in plain uncolored text, clickable in PDF and identical to plain text when printed.

---

## 2. Line-by-Line Improvement Breakdown

### Header & Positioning
- **Original V3**: Subtitle listing *"Robotics & Embedded Systems Engineer | Autonomous Systems | ADAS"*.
- **Improved `resume.tex`**: Enhanced to *"Robotics & Systems Engineer | Autonomous Systems · ROS2 · C/C++ · Python · Embedded RTOS · CV · AI Infra"*, expanding keyword coverage for AI Infrastructure, ROS2, and Embedded RTOS. Added personal portfolio link (`garvarora.vercel.app`).

### Education Section
- **Original V3**: Listed VIT Vellore CGPA 8.37 and Gems International School Class 10 (89.3%) / Class 12 (76.4%).
- **Improved `resume.tex`**: Corrected CGPA to 8.36 / 10.0 (per official grade records), standardized dates to `08/2023 -- 07/2027` and `11/2016 -- 04/2023`, formatted Class X/XII scores cleanly in a single line to prevent vertical dominance.

### Patents & Key Honors (New Dedicated Section)
- **Original V3**: Patent was listed under projects as a generic project titled "mmWave Earthquake Survivor Detection Robot".
- **Improved `resume.tex`**: Elevated to a top-line section:
  - **Patent Published (App No: IN202641072249 A1)**: *Autonomous Radar-Guided Survivor Detection and Navigation System* — Fused 24GHz FMCW mmWave radar, ultrasonic array, and IMU dead-reckoning on dual-core ESP32; formulated confidence grid decay $C = \max(0, C - \beta \Delta t)$ for survivor breathing detection under rubble. (06/2026)
  - **Amazon ML Summer School 2026**: Selected among Top 3,000 out of 1,30,000+ applicants across India (~2.3% acceptance rate).
  - **International Rover Challenge (IRC)**: Ranked **13th Globally (2025)** and **17th Globally (2026)** with Team Vyadh (SEDS VIT).
  - **Certifications**: Added AWS Certified AI Practitioner, AWS Certified Cloud Practitioner alongside Oracle Cloud Data Science & GenAI Professional.

### Work Experience Section
- **Original V3**: Only listed SEDS Projects VIT and Wissen Baum.
- **Improved `resume.tex`**:
  - **SEDS India (SEDS VIT)**: Preserved and enhanced core ROS2 Nav2 3D Visual SLAM (70% teleop cut), CUDA YOLOv8 V4L2 zero-copy (60% latency cut, 4x QPS), Micro-ROS ESP32 EKF odometry fusion (40% drift cut, sub-10 cm accuracy), and PyQt5 dashboard.
  - **Samsung PRISM**: Added Data Intelligence Agent Developer (Internship) — Multi-agent LangGraph pipeline (FastAPI, Redis, PostgreSQL, Qdrant), spaCy NLP, Presidio PII anonymization, SPDX license enforcement, BERTopic, MinHash LSH deduplication, MemorySaver HITL pause.
  - **LG Soft India (LGSI)**: Added Living Solution Control Development Intern — C/C++ embedded control logic and state machine handlers for living solution control modules, work certified as "Technically Competent" by LGSI HR/Engineering.
  - **Wissen Baum Engineering Solutions**: Refined bullet to highlight Python BDD test automation framework (Gherkin/Behave, pytest, Playwright), 40% GitLab CI pipeline speedup (~10m to ~6m), and 80%+ manual validation effort reduction.

### Selected Projects
- **HayaiOS**: Preserved preemptive bare-metal RTOS kernel in C & ARM Assembly on ARM Cortex-M4 (<50 instruction context switch, 1 ms tick, IPC primitives, HAL).
- **Captivity CLI**: Added published PyPI package link (`pypi.org/project/captivity-cli`). Highlighted Rust + Python daemon, <50ms HTTP 204 probing, systemd service, D-Bus NetworkManager monitoring, keyring encryption, dual TCP socket IPC.
- **3D Reconstruction**: Preserved Intel RealSense D455 depth + 6-DOF IMU complementary filter for KinectFusion TSDF reconstruction (50% tracking failure reduction).
- **teleop-cursor**: Added ROS 2 mouse teleoperation package (`pypi.org/project/teleop-cursor`) converting screen displacement vectors into smooth `geometry_msgs/Twist` velocity commands at 10 Hz for TurtleBot3/Gazebo.

---

## 3. Justification of Recruiter Conversion Priority

Every modification strictly balances **ATS parseability** with **Human Recruiter Interview Conversion**:
1. **Recruiter Proof Over Generic Buzzwords**: Framing the mmWave radar robot as an official **Published Patent IN202641072249 A1** and adding **Amazon ML Summer School (Top 3k/1.3L)** instantly signals elite builder capability to recruiters at FAANG, Tesla, and robotics firms.
2. **Enterprise R&D Validation**: Adding LG Soft India ("Technically Competent") and Samsung PRISM (LangGraph multi-agent pipeline) proves performance in real enterprise/industry settings beyond student projects.
3. **Open-Source Delivery**: Adding PyPI package links (`captivity-cli` and `teleop-cursor`) proves ability to ship production-grade code.
