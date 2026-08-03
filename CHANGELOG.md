# Flagship Resume Unified SEDS Single-Entry Engineering & Changelog

This document provides a comprehensive audit of the design choices, RAG evidence base, evolutionary history (V1 \(\rightarrow\) V2 \(\rightarrow\) V3 \(\rightarrow\) Commit 8 90 Score Baseline \(\rightarrow\) Single-Entry SEDS Optimization), evidence mapping, and precision fixes implemented in `resume.tex`.

---

## 1. Unified Single SEDS Entry Architecture

Per user instruction, the separate R&D Lead entry was removed and consolidated into a **single unified entry** under SEDS India:

- **Company**: `SEDS India (SEDS VIT)` (Vellore, India)
- **Role Title**: `R&D Lead and Autonomous Systems Developer`
- **Date Range**: `Apr 2024 -- Jul 2026`

### Engineering Benefits:
1. **Eliminated Duplicate Company Entry**: SEDS India appears exactly ONCE in the Work Experience section, preventing ATS parsers from flagging duplicate company name splits.
2. **Monotonic Reverse Chronological Date Flow**:
   - LG Soft India: `Jun 2026` *(Noida, India)*
   - Samsung PRISM: `Aug 2025 -- Present`
   - Wissen Baum: `May 2025 -- Jul 2025`
   - SEDS India: `Apr 2024 -- Jul 2026`
   *Start dates decrease strictly top-to-bottom (`Jun 2026` \(\rightarrow\) `Aug 2025` \(\rightarrow\) `May 2025` \(\rightarrow\) `Apr 2024`).*
3. **Optimal Word Count**: Reduced document length to **686 total words (~650 body words)**, hitting ResumeWorded's green slider target.

---

## 2. Core Strengths Preserved

1. **100% Action Verb Uniqueness**: All 12 experience and project bullets start with a 100% unique action verb (`Constructed`, `Promoted`, `Engineered`, `Authored`, `Architected`, `Slashed`, `Flashed`, `Shipped`, `Developed`, `Implemented`, `Built`, `Stabilized`).
2. **Independent Section Hierarchy**: Enforced 7 completely independent, unmerged sections (`Education`, `Work Experience`, `Projects`, `Patents`, `Achievements & Awards`, `Certifications`, `Technical Skills`).
3. **Clickable Verification Hyperlinks**: AWS Certmetrics verification URLs, Oracle Cloud badge links, PyPI package URLs, GitHub, LinkedIn, and Portfolio link (`garvarora.vercel.app`).
4. **Single-Page Verification**: Compiled with `./tectonic resume.tex` \(\rightarrow\) **`Pages: 1`** confirmed (`pdfinfo resume.pdf | grep Pages`).
