# Flagship Resume Split SEDS Restore & Engineering Changelog

This document provides a comprehensive audit of the design choices, RAG evidence base, evolutionary history (V1 \(\rightarrow\) V2 \(\rightarrow\) V3 \(\rightarrow\) Commit 8 90 Score Baseline \(\rightarrow\) Commit 9 Fixes), evidence mapping, and precision fixes implemented in `resume.tex`.

---

## 1. Commit 9 Score Drop Debugging & Root Cause Analysis

In Commit 9 review screenshots, merging SEDS India into a single stacked entry caused the ATS score to drop from **90 to 84**.

### Root Cause & Resolution:
1. **Split SEDS India Experience Entries Restored**:
   - Entry 1: `SEDS India (SEDS VIT)` - `Research & Development Lead` (`Jan 2026 -- Jul 2026`)
   - Entry 2: `SEDS India (SEDS VIT)` - `Autonomous Systems Developer` (`Apr 2024 -- Jan 2026`)
   *Restoring split entries restores 90+ score.*

2. **Factual Timeline & Location Updates**:
   - **SEDS R&D Lead Tenure**: Updated to `Jan 2026 -- Jul 2026` (reflecting total tenure completion in July 2026).
   - **LG Soft India Location**: Updated to `Noida, India` (correct R&D lab location).

---

## 2. Preserved 90-Score Core Features

1. **100% Action Verb Uniqueness**: All 12 experience and project bullets start with a 100% unique action verb (`Constructed`, `Promoted`, `Engineered`, `Authored`, `Architected`, `Slashed`, `Flashed`, `Shipped`, `Developed`, `Implemented`, `Built`, `Stabilized`). Repetition Score: **10/10**.
2. **Optimal Word Count**: **701 total words** (~667 body words), hitting ResumeWorded's green brevity sweet spot.
3. **Independent Section Hierarchy**: Enforced 7 completely independent, unmerged sections (`Education`, `Work Experience`, `Projects`, `Patents`, `Achievements & Awards`, `Certifications`, `Technical Skills`).
4. **Clickable Verification Hyperlinks**: AWS Certmetrics verification URLs, Oracle Cloud badge links, PyPI package URLs, GitHub, LinkedIn, and Portfolio link (`garvarora.vercel.app`).
5. **Single-Page Verification**: Compiled with `./tectonic resume.tex` \(\rightarrow\) **`Pages: 1`** confirmed (`pdfinfo resume.pdf | grep Pages`).
