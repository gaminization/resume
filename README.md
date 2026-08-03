# Garv Arora - Flagship LaTeX Resume Package

This repository contains the flagship production LaTeX source (`resume.tex`), compiled single-page PDF (`resume.pdf`), verification attestation matrix (`docs/Evidence_Mapping.md`), and comprehensive engineering report (`docs/Resume_Optimization_Report.md`) for **Garv Arora**, engineered with air-padded zero-collision vertical line spacing, Gesture-Controlled 5-DOF Robotic Arm project inclusion, TEDx Speaker achievement, reverse-chronologically sorted projects, single-page fit (`Pages: 1`), and optimized for high interview conversion across **Software Engineering (SWE), Robotics, Autonomous Systems, Embedded Systems, Computer Vision, ADAS, and AI/ML Engineering**.

---

## Repository Structure

```
resume/
├── resume.tex                       # Core production LaTeX source
├── resume.pdf                       # Compiled production single-page PDF (Pages: 1)
├── tectonic                         # Portable TeX compilation engine
├── LICENSE                          # MIT License
├── README.md                        # Primary repository documentation
├── CHANGELOG.md                     # Engineering & design revision changelog
│
├── docs/                            # Documentation & verification hub
│   ├── Evidence_Mapping.md          # Claim-by-claim attestation matrix
│   ├── Resume_Optimization_Report.md# Comprehensive ATS & recruiter evaluation report
│   ├── Garv_Arora_Resume_Master.md  # Plaintext markdown resume source
│   ├── my_docs/                     # Verification credentials & source files
│   └── reviews/                     # Peer review feedback & scorecards
│
├── archive/                         # Legacy versions & historical baselines
│   ├── 90score.tex                  # Historical 90-score baseline reference
│   ├── older_resumes/               # Historical resume iterations & chat logs
│   ├── jakes_template/              # Original Jake's Resume template reference
│   └── others_resumes/              # Benchmark reference resumes
│
└── scripts/                         # Build tools & alternative generators
    └── generate_pdf.py              # Alternative HTML/Weasyprint PDF generator
```

---

## Plaintext Hyperlink Configuration

Hyperlinks are configured using:
```latex
\usepackage[hidelinks]{hyperref}
\urlstyle{same}
```
This guarantees:
1. All links (`linkedin.com/in/gaminization`, `github.com/gaminization`, `garvarora.vercel.app`, PyPI links, AWS/Oracle verification links) are fully **clickable** in digital PDFs.
2. Link text displays the **actual URL or handle** in plain text.
3. Links render without colored text or visible boxes, remaining visually identical to plain text when printed on paper.

---

## How to Compile

To compile the single-page PDF locally using the included Tectonic engine:

```bash
./tectonic resume.tex
```

*or via standard TeX Live / pdfLaTeX:*

```bash
pdflatex resume.tex
```

---

## License

Distributed under the [MIT License](LICENSE).