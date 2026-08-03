# The Complete ATS Optimization Report — Every Technical and Content Rule That Matters

**A note on sources and confidence:** ATS optimization is a space full of confident-sounding, poorly-sourced statistics (the "75% of resumes are rejected by ATS" claim gets repeated everywhere with no consistent citation, and one ATS-tool vendor itself has publicly called it fabricated, tracing it to a defunct 2013 startup). I've flagged stats like this rather than repeating them as fact. The structural/technical parsing rules below, by contrast, are consistent across nearly every independent source I found — including tools that ran actual test resumes through real ATS platforms — so I'm more confident in those.

There is no single public "highest ATS scoring resume in the world" — ATS scores are proprietary, per-tool, and per-job-description (a resume scores differently against every different job posting). What does exist, and what this report is built from: **engineering-level breakdowns of how five major ATS platforms actually parse documents**, real test data comparing formats side by side, and platform-specific parsing quirks.

---

## Part 1: How an ATS actually processes your resume (the pipeline)

Every major ATS — whether built in-house at Workday or licensed from a parsing vendor like Sovren, Affinda, or RChilli — runs the same five-stage pipeline:

1. **Text extraction** — reads raw bytes from your PDF/DOCX/RTF and produces a linear character stream.
2. **Tokenization** — breaks that stream into words/phrases.
3. **Sectioning** — identifies which chunk of text is "Experience," which is "Education," etc.
4. **Named entity recognition (NER)** — extracts ~30 structured fields: name, email, phone, location, LinkedIn, each job's title/company/dates, each degree's school/major/year, skills, certifications.
5. **Structured output** — the extracted JSON feeds the recruiter's searchable database and auto-fills the application form.

**Every failure in the rules below is really a failure at one of these five stages** — usually stage 3 or 4. One detailed engineering test found that even a clean, well-formatted resume only achieves **~87% field-level parsing accuracy on average** (versus ~96% for a human reading the same document) — meaning roughly 1 in 8 fields breaks even under good conditions. This is worth internalizing: perfect parsing isn't achievable even with a flawless resume, which is exactly why the formatting rules below exist — to minimize the damage, not eliminate it.

---

## Part 2: The technical/structural rules (these determine if your data survives parsing at all)

These matter **before** keyword optimization even becomes relevant — a perfectly keyword-matched resume that parses into garbage is worse off than a plainer resume that parses cleanly.

### File format: PDF vs. DOCX
This is the most contested point across sources, and the honest answer is **"it depends on the platform, so default to the safer option when you don't know."**
- **Workday, Greenhouse, Lever**: parse text-selectable PDFs about as cleanly as DOCX in their current (2026) versions.
- **Taleo (Oracle)**: consistently flagged across every source as the **weakest at PDF parsing** — DOCX is the safer choice specifically for Taleo-run employers.
- **iCIMS**: historically DOCX-preferred; recent versions handle simple PDFs better but still less reliably than DOCX for complex layouts.
- **One controlled test**: single-column .docx files extracted **97.4%** of seeded fields on average across Workday/Greenhouse/Lever; two-column PDFs of the *same content* extracted only **71.2%** — and the gap was worst on Work Experience, where two-column PDFs lost an average of 1.8 role records per resume to column interleaving.
- **Universal rule regardless of format**: never submit a PDF exported from Canva, Figma, or a scanned/image-based source — these produce zero machine-readable text and will fail extraction completely. Test this yourself: open your PDF and try to highlight a sentence with your cursor. If you can't select the text, an ATS can't read it either.
- **Bottom line**: if you know the platform, tailor to it. If you don't, **DOCX is the universally safer default** — it degrades least across the widest range of ATS generations, and it's what most of the harder-line sources converge on as the "when in doubt" answer.

### Layout
- **Single column only.** Every source agrees on this without exception. Parsers read left-to-right, top-to-bottom, line by line. A two-column layout gets read *across* both columns simultaneously rather than down each one separately — job titles get mixed with skills, dates get orphaned from roles. Lever was specifically noted to "silently drop the sidebar" entirely in one test.
- **No tables.** Same failure mode as columns — this is the single most commonly cited "instant score killer" across every source.
- **No text boxes.** Content inside a text box is frequently skipped entirely rather than misread — some parsers don't process text-box content at all.
- **No headers/footers for anything important.** Several sources explicitly warn: contact info placed in a document header or footer "may be skipped entirely" by the parser. Put your name, phone, and email in the main body at the top of the page, not in a Word header field — this is one of the most commonly missed rules because it looks identical to a human reader either way.
- **No graphics, icons, photos, or skill-rating bars.** These either get dropped silently or, worse, get OCR'd into garbage characters that pollute your parsed text.

### Fonts
- Stick to **system-embedded fonts**: Calibri, Arial, Georgia, Cambria, Helvetica. Custom/downloaded fonts force a fallback rendering that can break what the parser actually sees, even though it looks fine to you on your own machine.
- **10–12 point** for body text is the universal safe range.

### Section headers
- Use **standard, literal labels**: "Work Experience" / "Professional Experience" / "Employment History," "Education," "Skills," "Certifications." Every source names this as a hard rule.
- Creative headers ("My Journey," "Where I've Been") are explicitly called out as causing entire sections to go unrecorded — the parser has no idea what category that content belongs to, so it may not store it at all.

### Dates
- **Use one consistent format throughout** — MM/YYYY is the most commonly recommended standard. Mixed date formats within the same document reduce the parser's confidence in your timeline and can distort how your total years of experience gets calculated.

### Bullet points
- Simple round or square bullets only. Avoid decorative bullet characters, icon bullets, or custom Unicode symbols — these can render as broken characters or get stripped.

### Hyperlinks
- Modern ATS (Workday, Greenhouse, Lever) generally parse embedded hyperlinks in DOCX/PDF fine as of 2026. The **safer universal practice regardless**: make sure the *visible text* of any link is meaningful on its own (e.g., the actual domain, or a clearly labeled credential name) so that even if a hyperlink gets stripped, the plain text underneath still communicates the real information.

---

## Part 3: Keyword optimization (what actually drives the score, once parsing succeeds)

- **99.7% of recruiters use keyword filters** in their ATS, per one cited industry report — keyword matching is not optional or secondary, it's the primary scoring mechanism in nearly every system.
- **ATS often can't recognize synonyms.** If the job description says "Adobe Creative Suite" and your resume says "Adobe Creative Cloud," some systems won't register that as a match even though a human would immediately understand they're the same thing. **Mirror the job posting's exact terminology** wherever it's truthful to do so.
- **Placement zones matter, not just presence.** Keywords are weighted more heavily when they appear in: (1) the professional summary, (2) the skills section, (3) the first bullet under each job title. A keyword buried at the end of your fifth bullet under a role from three jobs ago carries less weight than the same keyword in your summary line.
- **Spell out acronyms at least once, paired with the acronym**: "Search Engine Optimization (SEO)," "Certified Public Accountant (CPA)." This covers both an ATS that only matches the spelled-out term and one that only matches the acronym.
- **There is a real sweet spot, and 100% match is a red flag, not a goal.** Multiple sources converge on roughly the same band: below ~50% keyword match = likely screened out for missing critical terms; **65–80% match = the actual target zone**; above that, several tools explicitly warn you're now at risk of **over-optimization being flagged as manipulation** by the same modern systems built to detect keyword stuffing. A resume "gamed" to hit 100% keyword density on a scoring tool often reads as unnatural to the human who reads it next, and some 2026-era ATS have started penalizing that pattern directly rather than rewarding it.
- **Recommended volume**: roughly 15–25 relevant keywords per resume, aiming for that 65–80% coverage of the specific job description you're applying to — which also means **the keyword list changes per application**, not a fixed universal list on one static resume.

---

## Part 4: The dead trick — white/hidden text keyword stuffing

This deserves its own section because it's still actively recommended in some corners of the internet despite being obsolete advice. The trick: paste the full job description in white or zero-opacity text somewhere on the page so the ATS "sees" a perfect keyword match a human reviewer never notices.

**This is now actively detected and penalized, not just ineffective.** Workday, Greenhouse, and Lever are specifically named as having detection for zero-opacity or white-on-white text as of 2026 — and being flagged can attach a **fraud indicator to your candidate record**, not just a low score. Separately, any hiring manager who previews or prints your resume will see the hidden text directly and reject the application on sight. This tactic has gone from "risky" in 2022 to actively counterproductive in 2026.

---

## Part 5: Content-quality rules that double as ATS signals

These sit at the boundary between "technical ATS rule" and "just good resume writing" — they matter to both the algorithm and the human who reads it next:

- **Replace duty-statements with the four-part formula**: action verb + method/tool + quantified result + scope. Example given directly by one source: *"Rebuilt the checkout flow in React using A/B-tested variants, lifting conversion from 2.4% to 3.1% across 480K monthly sessions while leading a team of 5 engineers."* Bullets starting with "Responsible for..." or "Helped with..." are named as producing zero usable signal for either the algorithm or a human.
- **Use standard, recognizable job titles.** "Software Engineer," not "Code Ninja" — creative titles reduce both ATS keyword matching and human credibility.
- **Skills section: keep it clean and grouped**, not an undifferentiated wall of every tool you've ever touched — commas or simple bullets, grouped by category (Languages / Tools / Frameworks) where relevant.
- **Only add keywords/skills you can defend in an interview.** Multiple sources are explicit: don't invent proficiency to chase a keyword match — an ATS getting you the interview doesn't help if the first follow-up question exposes the gap.

---

## Part 6: Platform-specific cheat sheet

| Platform | Notable quirk | Practical takeaway |
|---|---|---|
| **Workday** | Enterprise-scale; some setups still parse DOCX more reliably than PDF | Use DOCX if you're unsure which employer variant they're running |
| **Greenhouse** | Recruiter often reads your actual PDF directly, with parsed fields as *supporting* metadata rather than the sole source of truth | Slightly more forgiving — human eyes are more directly in the loop |
| **Lever** | Modern parser, generally reliable with PDF; recruiter review tends to happen earlier in the pipeline | Less purely algorithmic gatekeeping than Workday/Taleo |
| **Taleo (Oracle Recruiting)** | Oldest, strictest platform; **weakest PDF parsing** of the major five | Always prefer DOCX here if you can identify the platform |
| **iCIMS** | Common in retail/healthcare/manufacturing; older engine; table-based layouts "frequently break" | DOCX preferred; avoid any table formatting entirely |
| **SmartRecruiters** | Generally modern, reliable with both formats | Standard single-column DOCX/PDF rules apply |

**How to identify which platform you're applying through**: check the application URL. Workday uses `myworkdayjobs.com`, Greenhouse uses `greenhouse.io` / `boards.greenhouse.io`, Taleo uses `taleo.net`, iCIMS uses `icims.com`. Knowing this tells you which format bias to lean toward.

---

## Part 7: How to actually test your own resume

The most concrete, repeatable test named across multiple sources: **open your resume and view/copy it as plain text** — this approximates what the parser actually extracts, stripped of all visual formatting. If information is missing, scrambled, or out of order in that plain-text view, an ATS will see the same broken version. Beyond that, free scanner tools (Jobscan, ResumeWorded, and several others named across these sources) will give a numeric score and a missing-keyword list against a specific job description — useful as a directional check, not as a certification, since every tool's scoring model is proprietary and slightly different from the real employer's actual ATS.

---

## Cross-source synthesis — the actual priority order

1. **Parseability comes before keywords.** A resume that scores 95% on keyword match but loses half its Work Experience section to a two-column layout is worse off than a plain single-column resume at 70% keyword match. Fix structure first, then optimize content.
2. **DOCX is the safer universal default when you don't know the platform**; PDF is fine and sometimes preferred for known-modern platforms (Greenhouse, Lever, current Workday) — but never a PDF exported from a design tool or a scan.
3. **The keyword target is a band (roughly 65–80%), not a maximum.** Over-optimizing past that point is now actively risky, not just wasteful — modern ATS have started detecting and flagging manipulation patterns directly.
4. **Hidden-text keyword stuffing has crossed from "ineffective" to "actively detected and penalized."** This is worth explicitly unlearning if you picked it up from older advice.
5. **Contact info in headers/footers is one of the most commonly missed, highest-consequence mistakes** — it looks completely normal to a human and can silently vanish from the parsed data.
6. **No score checker's number is the real score.** The real ATS is proprietary to the employer; third-party checkers are directionally useful, not a certification — treat a 70+ on any public tool as "probably fine," not "guaranteed to pass."

*Sources: engineering-level ATS parser breakdowns and controlled parsing tests (Resume Optimizer Pro, ATSHiring, ShashiWorks), Jobscan's published guidance and 2026 State of the Job Search data, multiple independent ATS-checker tools' documented scoring methodology (ResumeAdapter, Zimyo, GoodSpace, Resumly, HireFlow), and named platform documentation (Greenhouse candidate help center). Compiled July 2026 — this space changes fast; re-verify platform-specific quirks periodically since ATS vendors update parsing engines regularly.*
