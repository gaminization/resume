# Garv Arora - Flagship LaTeX Resume Package

This repository contains the flagship production LaTeX source (`resume.tex`), compiled single-page PDF (`resume.pdf`), and official evidence attestation mapping (`Evidence_Mapping.md`) for **Garv Arora**, engineered from the official Jake's Resume LaTeX foundation and optimized for high interview conversion across **Software Engineering (SWE), Robotics, Autonomous Systems, Embedded Systems, Computer Vision, ADAS, and AI/ML Engineering**.

---

## Deliverable Files

- **`resume.tex`**: Production LaTeX source code built on Jake's template foundation with strict reverse-chronological date ordering, independent section structure, and plaintext hyperref configuration.
- **`resume.pdf`**: Single-page compiled PDF document (`Pages: 1` confirmed).
- **`Evidence_Mapping.md`**: Complete claim-by-claim attestation matrix linking every resume statement to official certificate URLs, patent publication numbers, PyPI pages, GitHub repositories, and local `my_docs/` verification files.
- **`README.md`**: Compilation, package, and customization documentation.
- **`CHANGELOG.md`**: Complete RAG evidence audit, peer resume comparative analysis, and evolutionary changelog from V1 \(\rightarrow\) V2 \(\rightarrow\) V3 \(\rightarrow\) Commit 4 Flagship TeX.

---

## Plaintext Hyperlink Configuration

Hyperlinks are configured using:
```latex
\usepackage[hidelinks]{hyperref}
\urlstyle{same}
```
This guarantees:
1. All links (`linkedin.com/in/gaminization`, `github.com/gaminization`, `garvarora.vercel.app`, PyPI links, AWS/Oracle verification links) are fully **clickable** in digital PDFs.
2. Link text displays the **actual URL or handle** in plain text.
3. Links render without colored text or visible boxes, remaining visually identical to plain text when printed on paper.

---

## How to Compile

```bash
./tectonic resume.tex
```
*or*
```bash
pdflatex resume.tex
```