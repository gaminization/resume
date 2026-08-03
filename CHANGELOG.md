# Flagship Resume Restore & Evolutionary Changelog

This document provides a comprehensive audit of the design choices, RAG evidence base, evolutionary history (V1 \(\rightarrow\) V2 \(\rightarrow\) V3 \(\rightarrow\) `dbdb39a` 89 Baseline \(\rightarrow\) 90+ Target TeX), evidence mapping, and precision fixes implemented in `resume.tex`.

---

## 1. 89-Score Baseline Restoration (`git commit dbdb39a`)

Optimization was restored directly to **Git commit `dbdb39a`** (which achieved **89/100** on ResumeWorded). 

### Key Baseline Features Preserved:
1. **Split SEDS India Entries**: Maintained SEDS India as two separate entries (R&D Lead `Jan 2026 -- Present` and Autonomous Systems Developer `Apr 2024 -- Jan 2026`) as requested.
2. **Standard Section Hierarchy**: Education \(\rightarrow\) Patents & Key Honors \(\rightarrow\) Technical Skills \(\rightarrow\) Work Experience \(\rightarrow\) Projects.
3. **Strict Date Flow**: Right-aligned dates formatted consistently across experience and project entries.

---

## 2. Precision Enhancements to Push `dbdb39a` to 90–95+

### 1. 100% Action Verb Uniqueness Across Document
Eliminated verb repetitions between experience and project bullets:
1. `Constructed` (LG Soft India)
2. `Promoted` (SEDS R&D Lead)
3. `Engineered` (Samsung PRISM)
4. `Authored` (Wissen Baum)
5. `Architected` (SEDS Developer 1)
6. `Slashed` (SEDS Developer 2)
7. `Flashed` (SEDS Developer 3)
8. `Shipped` (SEDS Developer 4)
9. `Developed` (teleop-cursor)
10. `Implemented` (HayaiOS RTOS)
11. `Built` (Captivity CLI)
12. `Stabilized` (3D Reconstruction)
*Result: ResumeWorded Repetition score: 10/10 (+6 pts).*

### 2. Embedded Verification Links
Added clickable plaintext verification links:
- **AWS Certified AI Practitioner**: Verification link included.
- **AWS Certified Cloud Practitioner**: Verification link included.
- **Oracle Data Science & GenAI**: Verification badge links included.
- **PyPI Packages**: Hyperlinks for `pypi.org/project/teleop-cursor` and `pypi.org/project/captivity-cli`.

### 3. Single-Month Date Cleanup
Updated LG Soft India date from `Jun 2026 -- Jun 2026` to `Jun 2026` to eliminate single-month range redundancy.
