import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY

def build_pdf(filename):
    # Page setup: Letter size with 0.3 inch margins
    margin = 21.6  # 0.3 in points
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=margin,
        rightMargin=margin,
        topMargin=margin,
        bottomMargin=margin
    )
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    style_name = ParagraphStyle(
        'NameStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=18,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#000000')
    )
    
    style_contact = ParagraphStyle(
        'ContactStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#222222')
    )
    
    style_tagline = ParagraphStyle(
        'TaglineStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#111111')
    )
    
    style_heading = ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12,
        textColor=colors.HexColor('#000000'),
        spaceBefore=4,
        spaceAfter=2
    )
    
    style_body = ParagraphStyle(
        'BodyText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.2,
        leading=10.2,
        alignment=TA_JUSTIFY,
        textColor=colors.HexColor('#111111')
    )
    
    style_bullet = ParagraphStyle(
        'BulletText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.2,
        leading=10.2,
        alignment=TA_JUSTIFY,
        leftIndent=10,
        textColor=colors.HexColor('#111111')
    )

    story = []

    # Header
    story.append(Paragraph("GARV ARORA", style_name))
    story.append(Spacer(1, 2))
    story.append(Paragraph("+91 88008-12254 &bull; garvarora0205@gmail.com &bull; <a href='https://linkedin.com/in/gaminization' color='#0044cc'>linkedin.com/in/gaminization</a> &bull; <a href='https://github.com/gaminization' color='#0044cc'>github.com/gaminization</a> &bull; <a href='https://garvarora.vercel.app' color='#0044cc'>garvarora.vercel.app</a>", style_contact))
    story.append(Spacer(1, 2))
    story.append(Paragraph("<b>Robotics & Systems Engineer</b> &nbsp;|&nbsp; Autonomous Systems &bull; ROS2 &bull; C/C++ &bull; Python &bull; Embedded RTOS &bull; Computer Vision &bull; AI Infrastructure", style_tagline))
    story.append(Spacer(1, 2))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#222222'), spaceBefore=1, spaceAfter=3))

    # Education
    story.append(Paragraph("EDUCATION", style_heading))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#444444'), spaceBefore=0, spaceAfter=2))
    edu_text = "<b>Vellore Institute of Technology (VIT)</b> — Vellore, India <font color='#444444'>|</font> <b>Aug 2023 – July 2027</b><br/><i>Bachelor of Technology in Computer Science & Engineering (Specialization: IoT)</i> <font color='#444444'>|</font> <b>CGPA: 8.36 / 10.0</b>"
    story.append(Paragraph(edu_text, style_body))
    story.append(Spacer(1, 2))

    # Patents & Key Honors
    story.append(Paragraph("PATENTS & KEY HONORS", style_heading))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#444444'), spaceBefore=0, spaceAfter=2))
    patents_honors = [
        "&bull; <b>Patent Published (App No: IN202641072249 A1):</b> <i>Autonomous Radar-Guided Survivor Detection & Navigation System</i> — Fused 24GHz FMCW mmWave radar, ultrasonic array, and IMU dead-reckoning on dual-core ESP32; formulated dynamic confidence grid decay <i>C = max(0, C - &beta;&Delta;t)</i> to detect breathing signatures under rubble without SLAM/LiDAR. <b>(June 2026)</b>",
        "&bull; <b>Amazon ML Summer School 2026:</b> Selected among Top 3,000 students out of 1,30,000+ applicants across India (~2.3% acceptance rate).",
        "&bull; <b>International Rover Challenge (IRC):</b> Ranked <b>13th Globally (2025)</b> and <b>17th Globally (2026)</b> with Team Vyadh (SEDS VIT).",
        "&bull; <b>TEDx Speaker:</b> Delivered talk on <i>\"Gender Stereotyping — Does It Still Exist?\"</i> at TEDxGEMSInternationalSchool."
    ]
    for ph in patents_honors:
        story.append(Paragraph(ph, style_bullet))
        story.append(Spacer(1, 1))

    # Work Experience
    story.append(Paragraph("WORK EXPERIENCE", style_heading))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#444444'), spaceBefore=0, spaceAfter=2))
    
    exp_data = [
        ("SEDS India (SEDS VIT)", "Research & Development Lead", "Jan 2026 – Present", "Vellore, India", [
            "&bull; Promoted to R&D Lead directing 2 national space robotics competition teams (50+ engineers) across Team Vyadh (IRC) and Team Ardra (ISDC); conducted architecture reviews and hardware debugging, resolving 10+ critical issues and securing 13th & 17th Global Ranks."
        ]),
        ("SEDS India (SEDS VIT)", "Autonomous Systems Developer", "Apr 2024 – Jan 2026", "Vellore, India", [
            "&bull; Architected ROS2 Nav2 & RTAB-Map 3D Visual SLAM pipeline on Intel RealSense D455, generating real-time elevation maps and slashing manual teleoperation time by 70% during autonomous competition traversals.",
            "&bull; Slashed CV pipeline latency by ~60% and boosted throughput 4x using CUDA GPU kernels, YOLOv8, ArUco/AprilTag tracking, and Linux V4L2 zero-copy buffer tuning across 4 simultaneous camera streams.",
            "&bull; Flashed Micro-ROS firmware onto ESP32 microcontrollers for distributed sensor polling, fusing wheel encoders and 6-DOF IMU with an Extended Kalman Filter (EKF) to cut odometry drift by ~40% (sub-10 cm positioning accuracy).",
            "&bull; Shipped PyQt5 mission dashboard with real-time telemetry visualization, parameter tuning, and FSM mission execution."
        ]),
        ("Samsung PRISM", "Data Intelligence Agent Developer (Internship)", "Aug 2025 – Present", "Remote", [
            "&bull; Developed a multi-agent LangGraph pipeline (FastAPI, Redis, PostgreSQL, Qdrant) automating discovery, screening, and 20-stage analysis of HuggingFace/Kaggle dataset corpora for LLM training optimization.",
            "&bull; Integrated spaCy structural NLP, Presidio PII anonymization, SPDX license policy, BERTopic clustering, and MinHash LSH deduplication; implemented a MemorySaver Human-in-the-Loop review pause state."
        ]),
        ("LG Soft India (LGSI) — HS/ES Lab", "Living Solution Control Development Intern", "June 2026 – June 2026", "Bengaluru, India", [
            "&bull; Engineered C/C++ embedded control logic and state machine handlers for living solution control modules, verifying execution timing on target hardware; work certified as \"Technically Competent\" by LGSI HR/Engineering management."
        ]),
        ("Wissen Baum Engineering Solutions LLP", "Software Automation Intern", "May 2025 – July 2025", "Pune, India", [
            "&bull; Built Python BDD test automation framework using Gherkin/Behave, pytest, Playwright, and Cypress, parallelizing GitLab CI jobs to cut pipeline execution time from ~10m to ~6m (40% speedup) and reducing manual testing effort by 80%+."
        ])
    ]

    for comp, role, date, loc, bullets in exp_data:
        head_text = f"<b>{comp}</b> — <i>{role}</i> <font color='#444444'>|</font> <b>{date}</b>"
        story.append(Paragraph(head_text, style_body))
        for b in bullets:
            story.append(Paragraph(b, style_bullet))
            story.append(Spacer(1, 1))

    # Selected Projects
    story.append(Paragraph("SELECTED PROJECTS", style_heading))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#444444'), spaceBefore=0, spaceAfter=2))
    
    projects = [
        ("HayaiOS — Preemptive Bare-Metal RTOS Kernel", "C, ARM Assembly, ARM Cortex-M4", "", "Implemented preemptive scheduler (1 ms tick) with context switching in <50 ARM assembly instructions, mutex/semaphore IPC primitives, and a hardware abstraction layer (HAL) isolating register-level I/O on ARM Cortex-M4."),
        ("Captivity CLI", "Rust, Python, Linux D-Bus, systemd, Socket IPC", "<a href='https://pypi.org/project/captivity-cli/' color='#0044cc'>PyPI: captivity-cli</a>", "Built autonomous captive portal WiFi login daemon featuring <50ms HTTP 204 probing, systemd background integration, D-Bus NetworkManager monitoring, keyring credential encryption, and dual Python-Rust TCP socket IPC."),
        ("3D Reconstruction — IMU-Enhanced KinectFusion", "C++, OpenCV, Intel RealSense SDK", "", "Stabilized KinectFusion TSDF reconstruction by fusing RealSense D455 depth and 6-DOF IMU data via complementary filter, reducing tracking failures by ~50% across fast-motion trajectories."),
        ("teleop-cursor", "ROS 2, Python, rclpy, geometry_msgs/Twist", "<a href='https://pypi.org/project/teleop-cursor/' color='#0044cc'>PyPI: teleop-cursor</a>", "Developed zero-hardware mouse cursor teleoperation node for ROS 2, converting screen displacement vectors into smooth linear/angular velocity commands (<i>geometry_msgs/Twist</i>) at 10 Hz callback frequency for TurtleBot3/Gazebo simulation.")
    ]

    for p_name, p_tech, p_link, p_desc in projects:
        link_str = f" | {p_link}" if p_link else ""
        p_head = f"&bull; <b>{p_name}</b> | <i>{p_tech}</i>{link_str}<br/>{p_desc}"
        story.append(Paragraph(p_head, style_bullet))
        story.append(Spacer(1, 1))

    # Technical Skills
    story.append(Paragraph("TECHNICAL SKILLS", style_heading))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#444444'), spaceBefore=0, spaceAfter=2))
    
    skills = [
        "&bull; <b>Languages:</b> C, C++, Python, Rust, ARM Assembly, Java, JavaScript, SQL, Bash, Verilog",
        "&bull; <b>Robotics & Autonomous Systems:</b> ROS2 (Nav2, MoveIt2), RTAB-Map (3D SLAM), Micro-ROS, EKF/UKF, PID & MPC Control, Sensor Fusion, mmWave Radar, Point Cloud Processing",
        "&bull; <b>Perception & Machine Learning:</b> OpenCV, YOLOv8, MediaPipe, Intel RealSense SDK, PyTorch, TensorFlow, scikit-learn, CUDA, HuggingFace Transformers",
        "&bull; <b>Embedded & Infrastructure:</b> ARM Cortex-M, ESP32, FreeRTOS, I2C/SPI/UART, Bare-Metal C/Assembly, Linux Kernel/D-Bus, Docker, Git, GitLab CI/CD, AWS",
        "&bull; <b>Backend & AI Architecture:</b> LangGraph, FastAPI, Redis, PostgreSQL, Qdrant, REST APIs"
    ]
    for s in skills:
        story.append(Paragraph(s, style_body))
        story.append(Spacer(1, 1))

    doc.build(story)

build_pdf("Garv_Arora_Resume_Master_1Page.pdf")
