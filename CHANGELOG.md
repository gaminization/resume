# Flagship Resume Jake's Template Architecture & IRDC 2025 Achievement Changelog

This document provides a comprehensive audit of the design choices, RAG evidence base, evolutionary history (V1 \(\rightarrow\) V2 \(\rightarrow\) V3 \(\rightarrow\) Commit 8 90 Score Baseline \(\rightarrow\) Jake's Resume Template Architecture & IRDC 2025 Calibration), evidence mapping, and precision fixes implemented in `resume.tex`.

---

## 1. IRDC 2025 Achievement Addition

Updated the Achievements & Awards section with the exact wording requested by the user:

- **International Rover Design Challenge (IRDC 2025)**: Added `International Rover Design Challenge (IRDC 2025): Top 5 Finalist with Team Vyadh (SEDS VIT)` as a dedicated bullet item under Achievements & Awards.

---

## 2. Classic Jake's Resume Template Architecture

Restored classic Jake's Resume macro architecture for optimal legibility and ATS parsing:

- **Macro Structure**: Standardized `\resumeSubheading`, `\resumeProjectHeading`, `\resumeItem`, `\resumeSubHeadingListStart`, and `\resumeItemListStart` to match classic Jake's Resume template spacing and tabular alignment.
- **Readability & Formatting**: Crisp contrast, classic margins (`0.25in` top/bottom, `0.35in` left/right), and effortless vertical flow across all sections.

---

## 3. 90-Score Baseline Structure Preserved

- **Word Count**: **613 total words (~580 body words)**, hitting 10/10 Brevity.
- **Single-Page Verification**: Compiled with `./tectonic resume.tex` \(\rightarrow\) **`Pages: 1`** confirmed (`pdfinfo resume.pdf | grep Pages`).
