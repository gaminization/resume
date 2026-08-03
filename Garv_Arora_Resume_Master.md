# GARV ARORA
+91 88008-12254 | garvarora0205@gmail.com | [linkedin.com/in/gaminization](https://linkedin.com/in/gaminization) | [github.com/gaminization](https://github.com/gaminization) | [garvarora.vercel.app](https://garvarora.vercel.app)

**Robotics & Systems Engineer** | Autonomous Systems · ROS2 · C/C++ · Python · Embedded RTOS · Computer Vision · AI Infrastructure

---

## EDUCATION

**Vellore Institute of Technology (VIT)** — Vellore, India  
*Bachelor of Technology in Computer Science & Engineering (Specialization: IoT)* | **CGPA: 8.36 / 10.0**  
*Aug 2023 – July 2027*

---

## PATENTS & KEY HONORS

- **Patent Published (App No: IN202641072249 A1)**: *Autonomous Radar-Guided Survivor Detection and Navigation System* — Invented mmWave radar (24GHz FMCW) + ultrasonic sensor fusion on ESP32 dual-core 240MHz MCU; formulated dynamic confidence grid decay \(C = \max(0, C - \beta \Delta t)\) to detect breathing signatures through debris without SLAM/LiDAR. *(June 2026)*
- **Amazon ML Summer School 2026**: Selected among Top 3,000 students out of 1,30,000+ applicants across India (~2.3% selection rate).
- **International Rover Challenge (IRC)**: Ranked **13th Globally (2025)** and **17th Globally (2026)** with Team Vyadh (SEDS VIT).
- **TEDx Speaker**: Delivered talk on *"Gender Stereotyping — Does It Still Exist?"* at TEDxGEMSInternationalSchool.

---

## WORK EXPERIENCE

### SEDS India (SEDS VIT) — Vellore, India  
*Research & Development Lead* | *Jan 2026 – Present*  
- Promoted to R&D Lead directing 2 national space robotics competition teams (50+ engineers) across Team Vyadh (IRC) and Team Ardra (ISDC); conducted architecture reviews and hardware debugging, resolving 10+ critical pre-competition issues.

*Autonomous Systems Developer* | *Apr 2024 – Jan 2026*  
- Architected ROS2 Nav2 & RTAB-Map 3D Visual SLAM pipeline on Intel RealSense D455, generating real-time elevation maps and slashing manual teleoperation time by 70% during autonomous competition traversals.
- Slashed CV pipeline latency by ~60% and boosted throughput 4x using CUDA GPU kernels, YOLOv8, ArUco/AprilTag tracking, and Linux V4L2 zero-copy buffer tuning across 4 simultaneous camera streams.
- Flashed Micro-ROS firmware onto ESP32 microcontrollers for distributed sensor polling, fusing wheel encoders and 6-DOF IMU with an Extended Kalman Filter (EKF) to cut odometry drift by ~40% (sub-10 cm positioning accuracy).
- Shipped PyQt5 mission dashboard with real-time telemetry visualization, parameter tuning, and FSM-based autonomous mission execution.

### Samsung PRISM — Remote / Industry Collaboration  
*Data Intelligence Agent Developer (Internship)* | *Aug 2025 – Present*  
- Developed a multi-agent LangGraph pipeline (FastAPI, Redis, PostgreSQL, Qdrant) automating discovery, screening, and 20-stage analysis of HuggingFace/Kaggle dataset corpora for LLM training optimization.
- Integrated spaCy structural NLP, Presidio PII anonymization, SPDX license policy, BERTopic clustering, and MinHash LSH deduplication; implemented a MemorySaver Human-in-the-Loop review pause state.

### LG Soft India (LGSI) — HS/ES India Lab — Bengaluru, India  
*Living Solution Control Development Intern* | *June 2026 – June 2026*  
- Engineered C/C++ embedded control logic and state machine handlers for living solution control modules, verifying execution timing on target hardware; work certified as "Technically Competent" by LGSI HR/Engineering management.

### Wissen Baum Engineering Solutions LLP — Pune, India  
*Software Automation Intern* | *May 2025 – July 2025*  
- Built a Python BDD test automation framework using Gherkin/Behave, pytest, Playwright, and Cypress, parallelizing GitLab CI jobs to cut pipeline runtime from ~10m to ~6m (40% speedup) and reducing manual testing effort by 80%+.

---

## SELECTED PROJECTS

**HayaiOS — Preemptive Bare-Metal RTOS Kernel** | *C, ARM Assembly, ARM Cortex-M4*  
- Implemented preemptive scheduler (1 ms tick) with context switching in <50 ARM assembly instructions, mutex/semaphore IPC primitives, and a hardware abstraction layer (HAL) isolating register-level I/O on ARM Cortex-M4.

**Captivity CLI** | *Rust, Python, Linux D-Bus, systemd, Socket IPC* | [PyPI: captivity-cli](https://pypi.org/project/captivity-cli/)  
- Built autonomous captive portal WiFi login daemon featuring <50ms HTTP 204 probing, systemd background integration, D-Bus NetworkManager monitoring, keyring credential encryption, and dual Python-Rust TCP socket IPC.

**3D Reconstruction — IMU-Enhanced KinectFusion** | *C++, OpenCV, Intel RealSense SDK*  
- Stabilized KinectFusion TSDF reconstruction by fusing RealSense D455 depth and 6-DOF IMU data via complementary filter, reducing tracking failures by ~50% across fast-motion trajectories.

**teleop-cursor** | *ROS 2, Python, rclpy, geometry_msgs/Twist* | [PyPI: teleop-cursor](https://pypi.org/project/teleop-cursor/)  
- Developed zero-hardware mouse cursor teleoperation node for ROS 2, converting screen displacement vectors into smooth linear/angular velocity commands (`geometry_msgs/Twist`) at 10 Hz callback frequency for TurtleBot3/Gazebo simulation.

---

## TECHNICAL SKILLS

- **Languages**: C, C++, Python, Rust, ARM Assembly, Java, JavaScript, SQL, Bash, Verilog
- **Robotics & Autonomous Systems**: ROS2 (Nav2, MoveIt2), RTAB-Map (3D SLAM), Micro-ROS, EKF/UKF, PID & MPC Control, Sensor Fusion, mmWave Radar, Point Cloud Processing
- **Perception & Machine Learning**: OpenCV, YOLOv8, MediaPipe, Intel RealSense SDK, PyTorch, TensorFlow, scikit-learn, CUDA, HuggingFace Transformers
- **Embedded & Infrastructure**: ARM Cortex-M, ESP32, FreeRTOS, I2C/SPI/UART, Bare-Metal C/Assembly, Linux Kernel/D-Bus, Docker, Git, GitLab CI/CD, AWS
- **Backend & AI Architecture**: LangGraph, FastAPI, Redis, PostgreSQL, Qdrant, REST APIs
