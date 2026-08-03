# Flagship Resume Zero-Collision Line Spacing & IRDC 2025 Achievement Changelog

This document provides a comprehensive audit of the design choices, RAG evidence base, evolutionary history (V1 \(\rightarrow\) V2 \(\rightarrow\) V3 \(\rightarrow\) Commit 8 90 Score Baseline \(\rightarrow\) Zero-Collision Line Spacing & IRDC 2025 Calibration), evidence mapping, and precision fixes implemented in `resume.tex`.

---

## 1. Zero-Collision Vertical Line Spacing Fix

Fixed the vertical text collisions present in the previous build:

- **Eliminated Overlapping Lines**: Calibrated `\resumeSubheading`, `\resumeProjectHeading`, `\resumeItem`, `\resumeSubHeadingListEnd`, and `\resumeItemListEnd` to prevent multiline bullet text from physically overlapping onto company and project header lines below them.
- **Crisp & Clean Typography**: Every line of text renders with distinct, un-distorted vertical line height and clear visual padding.

---

## 2. IRDC 2025 Achievement Addition

- **International Rover Design Challenge (IRDC 2025)**: Added `International Rover Design Challenge (IRDC 2025): Top 5 Finalist with Team Vyadh (SEDS VIT)` as a dedicated bullet item under Achievements & Awards.

---

## 3. 90-Score Baseline Structure Preserved

- **Word Count**: **613 total words (~580 body words)**, hitting 10/10 Brevity.
- **Single-Page Verification**: Compiled with `./tectonic resume.tex` \(\rightarrow\) **`Pages: 1`** confirmed (`pdfinfo resume.pdf | grep Pages`).
