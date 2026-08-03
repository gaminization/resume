# Flagship Resume 90-Score Baseline Spacing & Readability Changelog

This document provides a comprehensive audit of the design choices, RAG evidence base, evolutionary history (V1 \(\rightarrow\) V2 \(\rightarrow\) V3 \(\rightarrow\) Commit 8 90 Score Baseline \(\rightarrow\) Commit cbbe7cb Readability Restoration), evidence mapping, and precision fixes implemented in `resume.tex`.

---

## 1. Restoration of Commit cbbe7cb Baseline Structure (90 Score Target)

Restored the proven high-scoring baseline from commit `cbbe7cb`:

- **Samsung PRISM Dates**: `Apr 2026 -- Oct 2026`
- **Project Dates**: Simplified to single year numbers (`2026`, `2025`), keeping project header lines clean and preventing date parser confusion with work experience.
- **SEDS India Entry**: Single entry titled `Autonomous Systems Developer` (`Apr 2024 -- Jul 2026`) with 4 high-impact technical bullets.
- **Patent Entry**: Clean inline patent publication item `(2026)`.
- **Word Count**: **638 total words (~610 body words)**, hitting 10/10 Brevity.

---

## 2. Spacing & Readability Enhancements

- **Calibrated Geometry Margins**: Set to `[top=0.25in, bottom=0.25in, left=0.35in, right=0.35in]`.
- **Enhanced Item List Spacing**: Increased `itemsep=0.8pt` for bullet lists and section lists, expanding white space gaps for effortless scanning by human recruiters and hiring managers.
- **Single-Page Verification**: Compiled with `./tectonic resume.tex` \(\rightarrow\) **`Pages: 1`** confirmed (`pdfinfo resume.pdf | grep Pages`).
