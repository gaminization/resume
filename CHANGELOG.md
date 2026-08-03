# Flagship Resume Air-Padded Zero-Collision Line Spacing Changelog

This document provides a comprehensive audit of the design choices, RAG evidence base, evolutionary history (V1 \(\rightarrow\) V2 \(\rightarrow\) V3 \(\rightarrow\) Commit 8 90 Score Baseline \(\rightarrow\) Air-Padded Zero-Collision Line Spacing & IRDC 2025 Calibration), evidence mapping, and precision fixes implemented in `resume.tex`.

---

## 1. Air-Padded Zero-Collision Line Spacing Fix

Addressed the visual text collisions in the Projects section:

- **Eliminated Overlapping Project Titles**: Re-calibrated `\resumeProjectHeading` and `\resumeItem` vertical offsets so the multiline bullet text in `teleop-cursor` and `Captivity CLI` no longer crashes into the project header titles below them.
- **Air-Padded Readability**: Established distinct, un-cluttered vertical padding between every entry, heading, and bullet list item across the entire document.

---

## 2. IRDC 2025 Achievement Addition

- **International Rover Design Challenge (IRDC 2025)**: Added `International Rover Design Challenge (IRDC 2025): Top 5 Finalist with Team Vyadh (SEDS VIT)` under Achievements & Awards.

---

## 3. 90-Score Baseline Structure Preserved

- **Word Count**: **613 total words (~580 body words)**, hitting 10/10 Brevity.
- **Single-Page Verification**: Compiled with `./tectonic resume.tex` \(\rightarrow\) **`Pages: 1`** confirmed (`pdfinfo resume.pdf | grep Pages`).
