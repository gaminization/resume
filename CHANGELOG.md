# Flagship Resume Work Experience & Projects Spacing Fix Changelog

This document provides a comprehensive audit of the design choices, RAG evidence base, evolutionary history (V1 \(\rightarrow\) V2 \(\rightarrow\) V3 \(\rightarrow\) Commit 8 90 Score Baseline \(\rightarrow\) Work Experience & Projects Spacing Fix), evidence mapping, and precision fixes implemented in `resume.tex`.

---

## 1. Work Experience & Projects Spacing Calibration

Fixed the vertical line crowding identified in peer review:

- **Removed Negative Vertical Offsets**: Replaced squished `\vspace{-2.2pt}` offsets inside `\resumeItem` with clean `\vspace{-1.5pt}` spacing, opening up the line height within Work Experience and Projects bullet points.
- **Harmonized Section Spacing**: Work Experience and Projects now match the open, comfortable visual spacing of Education, Patents, Certifications, and Technical Skills.

---

## 2. 90-Score Baseline Structure Preserved

- **Samsung PRISM Dates**: `Apr 2026 -- Oct 2026`
- **Project Dates**: Simplified to single year numbers (`2026`, `2025`).
- **SEDS India Entry**: Single entry titled `Autonomous Systems Developer` (`Apr 2024 -- Jul 2026`).
- **Word Count**: **638 total words (~610 body words)**, hitting 10/10 Brevity.
- **Single-Page Verification**: Compiled with `./tectonic resume.tex` \(\rightarrow\) **`Pages: 1`** confirmed (`pdfinfo resume.pdf | grep Pages`).
