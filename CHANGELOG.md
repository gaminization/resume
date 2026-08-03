# Flagship Resume Proportional Entry Spacing & IRDC Achievement Changelog

This document provides a comprehensive audit of the design choices, RAG evidence base, evolutionary history (V1 \(\rightarrow\) V2 \(\rightarrow\) V3 \(\rightarrow\) Commit 8 90 Score Baseline \(\rightarrow\) Proportional Entry Spacing & IRDC Achievement Calibration), evidence mapping, and precision fixes implemented in `resume.tex`.

---

## 1. Proportional Entry Spacing Fix

Calibrated the vertical list hierarchy for smooth visual scanning:

- **Proportional Subheading List Spacing**: Configured `itemsep=2.0pt` in `\resumeSubHeadingListStart`, establishing clean, balanced vertical gaps between different companies in Work Experience (LGSI \(\rightarrow\) Samsung PRISM \(\rightarrow\) Wissen Baum \(\rightarrow\) SEDS India) and different project headers (`teleop-cursor` \(\rightarrow\) `Captivity CLI` \(\rightarrow\) `3D Reconstruction`).
- **Balanced Visual Hierarchy**: Maintains readable separation between entries while avoiding blown-out whitespace gaps.

---

## 2. IRDC 2024 Achievement Addition

- **International Rover Design Challenge (IRDC 2024)**: Added `15th Globally (IRDC 2024)` to the Achievements & Awards section:
  `Rover Competitions (IRC & IRDC): Ranked 13th Globally (IRC 2025), 17th Globally (IRC 2026), and 15th Globally (IRDC 2024) with Team Vyadh (SEDS VIT).`

---

## 3. 90-Score Baseline Structure Preserved

- **Word Count**: **606 total words (~575 body words)**, hitting 10/10 Brevity.
- **Single-Page Verification**: Compiled with `./tectonic resume.tex` \(\rightarrow\) **`Pages: 1`** confirmed (`pdfinfo resume.pdf | grep Pages`).
