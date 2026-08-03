# Flagship Resume Engineering & Evolutionary Changelog

This document provides a comprehensive audit of the design choices, RAG evidence base, evolutionary history (V1 \(\rightarrow\) V2 \(\rightarrow\) V3 \(\rightarrow\) Flagship TeX), peer resume analysis, evidence mapping, and score fixes implemented in `resume.tex`.

---

## 1. RAG Evidence Base & Attestation Mapping

Every line in `resume.tex` is directly traceable to verified primary source documents in the workspace. An official **[Evidence_Mapping.md](file:///home/gaminizer/Projects/resume/Evidence_Mapping.md)** document has been generated, detailing:

- **Patent Published (App IN202641072249 A1)**: Traceable to `my_docs/Patent Publish.pdf` (FMCW 24GHz mmWave radar, ultrasonic array, IMU dead-reckoning, ESP32, dynamic confidence grid decay formula \(C = \max(0, C - \beta \Delta t)\)).
- **Amazon ML Summer School 2026**: Traceable to `my_docs/main` (Selected in Top 3,000 out of 1,30,000+ applicants across India, ~2.3% acceptance rate).
- **International Rover Challenge (IRC)**: Traceable to `my_docs/vyadh`, `my_docs/main` (13th Global Rank 2025, 17th Global Rank 2026 with Team Vyadh @ SEDS VIT).
- **LG Soft India (LGSI)**: Traceable to `my_docs/LG_Certificate.pdf` (Living Solution Development – Living Solution Control Development, HS/ES India Lab, 06/2026 -- 06/2026, officially certified as "Technically Competent").
- **Samsung PRISM**: Traceable to `my_docs/samprism` and `my_docs/PRISM_Worklet_Data Intelligence Agent_Phase 1.pptx` (Multi-agent LangGraph pipeline, FastAPI, Redis, PostgreSQL, Qdrant, spaCy NLP, Presidio PII anonymization, SPDX license enforcement, BERTopic, MinHash LSH deduplication, MemorySaver HITL review pause).
- **Wissen Baum Engineering Solutions**: Traceable to `my_docs/Wissenbaum_Report` (Software Automation Intern, May 2025 -- July 2025, Python BDD testing with Gherkin/Behave, pytest, Playwright, Cypress, GitLab CI 40% speedup from ~10m to ~6m, 80%+ manual testing reduction).
- **AWS & Oracle Certifications**: Traceable to `my_docs/AWS Certified AI Practitioner certificate.pdf`, `my_docs/AWS Certified Cloud Practitioner certificate.pdf`, and `my_docs/main` (Official AWS Certmetrics Verification URLs and Oracle Badge Links).
- **PyPI Packages**:
  - `teleop-cursor`: PyPI package [`pypi.org/project/teleop-cursor`](https://pypi.org/project/teleop-cursor/) & GitHub repository.
  - `Captivity CLI`: PyPI package [`pypi.org/project/captivity-cli`](https://pypi.org/project/captivity-cli/) & GitHub repository.

---

## 2. Independent Section Structure Compliance

`resume.tex` enforces completely independent, unmerged top-level sections as requested:

1. **Education**
2. **Work Experience**
3. **Projects**
4. **Patents**
5. **Achievements & Awards**
6. **Certifications**
7. **Technical Skills**

---

## 3. SEDS India Role Consolidation Optimization

Rather than splitting SEDS India into two separate corporate-style entries that duplicate headers and create date overlap penalties, SEDS India has been consolidated into a single high-density organization entry:
```latex
\resumeSubheading
  {SEDS India (SEDS VIT)}{Vellore, India}
  {Research \& Development Lead \textnormal{\textit{(Promoted from Developer)}}}{Apr 2024 -- Present}
```
- **Vertical Space Saved**: ~4 lines of vertical space reclaimed.
- **Date Penalty Resolved**: Eliminates concurrent date overlap flagged in ResumeWorded Commit 3 review.
- **Career Growth Signaled**: Clearly highlights rapid promotion from Autonomous Systems Developer to R&D Lead managing 50+ engineers across 2 national teams (Team Vyadh & Team Ardra).

---

## 4. Hyperlink Configuration & ATS Compatibility

Configured via:
```latex
\usepackage[hidelinks]{hyperref}
\urlstyle{same}
```
All URLs display plain uncolored text that is fully clickable in PDF digital viewers while rendering visually identical to standard text when printed.
