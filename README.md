# Garv Arora - LaTeX Resume Package

This repository contains the production-ready LaTeX source (`resume.tex`) and compiled PDF (`resume.pdf`) for **Garv Arora's** resume, optimized for high ATS compatibility and maximum human recruiter interview conversion across Robotics, Systems Engineering, Embedded Systems, Computer Vision, ML Engineering, and Software Engineering roles.

---

## Output Files

- **`resume.tex`**: Production LaTeX source code. Clean, modular, well-commented, and 100% single-page calibrated.
- **`resume.pdf`**: Compiled single-page PDF document.
- **`CHANGELOG.md`**: Complete audit and line-by-line documentation of improvements made relative to Resume V3 baseline.

---

## Requirements & Packages

The resume uses minimal, standard TeX dependencies for maximum portability across TeX Live, MiKTeX, Overleaf, and Tectonic:

- `article` document class (`10pt`, `letterpaper`)
- `geometry` (top/bottom `0.24in`, left/right `0.35in`)
- `titlesec` (clean section headings with subtle rules)
- `hyperref` (with `[hidelinks]` and `\urlstyle{same}`)
- `enumitem` (tight, custom-indented list formatting)
- `tabularx` & `fullpage`
- `color` & `babel`

---

## How to Compile

### Option 1: Using Tectonic (Standalone CLI — Recommended)
```bash
./tectonic resume.tex
```

### Option 2: Using pdflatex / xelatex (TeX Live or MiKTeX)
```bash
pdflatex resume.tex
```
*or*
```bash
xelatex resume.tex
```

### Option 3: Overleaf
1. Create a new blank project on [Overleaf](https://www.overleaf.com/).
2. Upload `resume.tex`.
3. Select `pdfLaTeX` or `XeLaTeX` as the compiler and click **Recompile**.

---

## Hyperlink Behavior

Hyperlinks are configured via:
```latex
\usepackage[hidelinks]{hyperref}
\urlstyle{same}
```
This ensures:
1. All URLs (`linkedin.com/in/gaminization`, `github.com/gaminization`, `garvarora.vercel.app`, PyPI links) are fully **clickable** in digital PDFs.
2. Link text displays the **actual URL / username** instead of colored text like "LinkedIn" or "GitHub".
3. Links render in plain, uncolored text with **zero colored boxes or underlines**, ensuring visual identity with plain text when printed on paper.

---

## Customization Instructions

- **Adjusting Spacing**: Modify the vertical space adjustments (`\vspace{-8pt}`) or list margins in `resume.tex` if adding or removing bullets to maintain a strict 1-page fit.
- **Updating Metrics**: Exact metrics are provided across all entries. To update dates or CGPA, modify the corresponding `\resumeSubheading` arguments.