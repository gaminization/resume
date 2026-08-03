# Garv Arora - LaTeX Resume Package

This repository contains the flagship production LaTeX source (`resume.tex`) and compiled single-page PDF (`resume.pdf`) for **Garv Arora**, engineered from the official Jake's Resume LaTeX foundation and optimized for high interview conversion across **Software Engineering (SWE), Robotics, Autonomous Systems, Embedded Systems, Computer Vision, ADAS, and AI/ML Engineering**.

---

## Deliverable Files

- **`resume.tex`**: Production LaTeX source code built on Jake's template foundation with enhanced margins, strict reverse-chronological dates, and plaintext hyperref configuration.
- **`resume.pdf`**: Single-page compiled PDF document.
- **`README.md`**: Compilation, package, and customization documentation.
- **`CHANGELOG.md`**: Complete RAG evidence audit, peer resume comparative analysis, and evolutionary changelog from V1 \(\rightarrow\) V2 \(\rightarrow\) V3 \(\rightarrow\) Production.

---

## TeX Requirements & Dependencies

The resume is built with minimal, standard TeX dependencies ensuring 100% compatibility across TeX Live, MiKTeX, Overleaf, and Tectonic:

- `article` document class (`10pt`, `letterpaper`)
- `geometry` (top/bottom `0.30in`, left/right `0.38in`)
- `titlesec` (clean section headings with subtle rules)
- `hyperref` (configured with `[hidelinks]` and `\urlstyle{same}`)
- `enumitem` (tight, custom-indented list formatting)
- `tabularx` & `fullpage`
- `color` & `babel`

---

## How to Compile

### Option 1: Using Tectonic (Recommended CLI)
```bash
./tectonic resume.tex
```

### Option 2: Using pdflatex or xelatex (TeX Live / MiKTeX)
```bash
pdflatex resume.tex
```
*or*
```bash
xelatex resume.tex
```

### Option 3: Overleaf
1. Create a new project on [Overleaf](https://www.overleaf.com/).
2. Upload `resume.tex`.
3. Choose `pdfLaTeX` or `XeLaTeX` as the compiler and click **Recompile**.

---

## Plaintext Hyperlink Configuration

Hyperlinks are configured using:
```latex
\usepackage[hidelinks]{hyperref}
\urlstyle{same}
```
This guarantees:
1. All links (`linkedin.com/in/gaminization`, `github.com/gaminization`, `garvarora.vercel.app`, PyPI links) are fully **clickable** in digital PDFs.
2. Link text displays the **actual URL or handle** in plain text (no "GitHub" or "Portfolio" colored text).
3. Links render without colored text or visible boxes, remaining visually identical to plain text when printed on paper.