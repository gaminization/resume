# What Top-Company Resumes Actually Look Like — Research Report

**Scope & honesty note:** I don't have access to private individual resumes — they aren't public data, and pulling real people's personal documents wouldn't be something I could verify anyway. What I *did* do is research each company's own hiring guides, recruiter interviews, ATS keyword data, and real anonymized/shared example resumes (from people who posted them publicly after getting offers) to reverse-engineer what a resume needs to contain to clear each company's screen. This report is organized by company/cluster, with a synthesis at the end.

---

## 1. Anthropic (Claude)

- Recruiters explicitly say: **don't pad — dense, signal-rich resumes are strongly preferred** over long ones.
- Despite the "AI lab" branding, an analysis of ~1,680 LinkedIn profiles of current Anthropic engineers found the most common resume skills are traditional infra/software engineering, not just ML: **Python, Java, C++, JavaScript, SQL, Linux, distributed systems, AWS**. Training pipelines, inference serving, security, billing, observability, and disaster recovery all show up as often as "model training."
- Most engineers did **not** come from OpenAI/DeepMind — hires are pulled broadly from big tech and infra-heavy companies.
- Concrete resume signals that work: links to **GitHub, arXiv preprints, or interpretability writing** (they say these "will be read"); explicit mention of **PyTorch, JAX, CUDA, Triton**, large-scale data pipeline experience.
- Anthropic explicitly invites candidates to use Claude to *polish* (not generate) resume drafts — they want your real experience communicated well, not AI-invented experience.
- Culture-fit signal: genuine engagement with AI safety (papers read, blog posts, alignment-relevant side projects) is called out as a differentiator.

## 2. OpenAI (ChatGPT)

- States plainly it is **"not credential-driven"** — resume screen looks for demonstrated high-potential ramp-up, not just pedigree.
- Resume tips from their own interview guide: **emphasize impact and scale** (systems affecting millions of users, large data volumes, complex distributed systems), and **be concise** — recruiters spend very little time per resume.
- For AI/ML-adjacent roles: **lead with production AI work** — shipped LLM features, RAG pipelines, agent frameworks — over notebook-only model training.
- Common rejection reason cited: treating the OpenAI application like a generic big-tech one, without any stated perspective on AI safety/responsible deployment; also "sloppy code" signals in take-homes.
- Values assessed explicitly in-loop: mission alignment, humility, collaboration, communication.

## 3. Google / Meta / Amazon / Apple / Netflix (FAANG, treated as one cluster since patterns converge)

- Across all five, the resume's real job is **"let the recruiter slot you at the correct level in seconds."** Google levels L3–L8, Meta E3–E7+, Amazon SDE I–Principal — bullets need to visibly match a specific level's expected scope.
- Universal format rules: **one page** (two only for 10+ years' experience), single column, standard section headers (so ATS parses cleanly), PDF exported from Word/Docs (not a design tool), no images/logos.
- Bullets are expected to carry **scale metrics**: QPS, latency (p99), users affected, $ saved, team size. "Managed a project" reads as a duty, not an achievement — a number is what separates the two.
- At Amazon specifically, resumes are read against the 16 Leadership Principles by a "Bar Raiser" with veto power — bullets ideally map implicitly to specific LPs (Ownership, Dive Deep, Deliver Results, etc.).
- Projects need to be verifiable — links to GitHub repos, with specifics on what you personally built/maintained (not just "contributed to").
- Buzzword-matching against the job description genuinely matters for the ATS pass, but recruiters can tell shallow keyword-stuffing from real fluency — specificity (naming exact frameworks/tools you used and what you built with them) beats generic category words like "programming languages."

## 4. BlackRock

- Analyst/Associate resumes lean quantitative-finance generalist: SQL, Python, VBA, and specific portfolio systems (**Aladdin**, Bloomberg PORT) show up repeatedly in real job postings and are treated as resume keywords.
- Quant Research roles want a **quantitative degree** (math/stats/CS/engineering) plus demonstrable relevant project or research experience — 1–2 years is typical for the analyst tier.
- Their HireVue-style first-round screen is explicitly non-technical/behavioral — but candidates report being expected to "know your resume in and out," i.e., every line must be defensible in detail live.
- A publicly shared "how I got into BlackRock" account from a graduate analyst emphasized: **non-target-school candidates compensate with a relevant Master's from a target school** plus visible internship experience — pedigree still matters more here than in tech, but is not an absolute gate.

## 5. Oracle

- Oracle's own hiring/keyword data shows up frequently as the **enterprise-Java benchmark** other companies compare against: resumes are expected to show depth in Java, SQL, enterprise architecture, and (increasingly) cloud (OCI) and applied AI credentials.
- Enterprise recruiters (per automation/ATS-keyword research) weight **long-term ownership of large systems** and formal certifications (Oracle's own certs carry real internal weight) more than a typical fast-growing startup would.

## 6. ABB / KUKA / Rockwell Automation (industrial automation cluster)

- These three show up together constantly in resume-keyword research because hiring managers explicitly want **named platform experience**, not generic "robotics" — resumes that just say "industrial robots" without naming ABB, KUKA, FANUC, or Yaskawa specifically underperform.
- Recurring keyword clusters that resumes need to hit for ATS + human screens:
  - **PLC/SCADA**: Allen-Bradley/Rockwell (ControlLogix, CompactLogix, Studio 5000), Siemens (S7-1500, TIA Portal), ladder logic, structured text.
  - **Robot programming**: KUKA KRL, teach pendant work, offline programming (WorkVisual for KUKA), motion control, vision-guided systems (e.g., Cognex).
  - **Industrial networking**: EtherNet/IP, Modbus TCP/IP, Profinet, OPC UA.
- The highest-performing example bullets in this space always pair a **named employer/client** (Ford, BMW, Abbott) with a **hard metric**: defect rate reduced from 1.8% → 0.3%, OEE raised 71% → 89%, $3.4M annual savings. Vague "improved efficiency" bullets are called out as the weak pattern.
- Certifications carry unusually high weight here relative to tech: **Certified Automation Professional (CAP)**, dual-vendor robot certifications (e.g., FANUC-certified + KUKA-certified) are treated as real differentiators, not filler.

## 7. Boston Dynamics

- Resume screen weighs **robotics kinematics/dynamics/trajectory-planning coursework or project experience**, C++ (2+ years commonly required), and evidence of "problem-solving on complex projects" specifically — not just coding ability in the abstract.
- Because Boston Dynamics sits at the intersection of hardware + software + applied AI, the strongest resumes show cross-domain project work (e.g., a candidate who's touched both control systems and perception/ML), not narrow specialization.
- Small company (roughly 640 employees) — referrals and direct hands-on project portfolios matter more than at FAANG scale; there's no giant ATS keyword-matching bureaucracy to game the way there is at a bank.

## 8. Tesla

- Tesla runs its **own in-house ATS** (not Greenhouse/Workday), and resume researchers describe it as parsing for a proprietary format — single-column PDF/DOCX with a real text layer and standard headers is explicitly recommended.
- Musk's stated hiring bar, widely referred to as **"evidence of excellence"**: did the candidate build something genuinely impressive, win a hard competition, or solve a hard problem — and can they explain exactly how, in detail. Resumes are expected to read as *proof*, not as job descriptions.
- The clearest documented pattern: **"what you built" beats "what you managed."** A mechanical engineering example given directly by resume researchers: "Managed design projects" is weak; **"Designed and machined aluminum suspension components reducing weight by 15% using CATIA"** is the standard that gets interviews.
- Because of the 2022 in-person mandate, resumes that read as remote-first or "coordination-heavy" (lots of meeting/liaison language) are flagged as a bad signal for their fast-paced, on-site engineering culture.
- Hiring has recently rotated toward **AI, robotics (Optimus), FSD, and controls** — legacy "EV manufacturing" framing alone is now considered a weaker signal than a year or two ago.

## 9. Uber

- Resume expectations mirror general big-tech SWE norms — algorithms/data structures, specific languages/frameworks, and measurable outcomes — but Uber's own postings put unusually heavy weight on **APIs, databases, and system reliability/networking** language, reflecting its marketplace/logistics-at-scale core business.
- Action-verb variety (Built, Optimized, Scaled, Reduced) is called out repeatedly as a differentiator versus resumes that repeat "Responsible for" throughout.

## 10. Adobe

- ATS-first company: recruiters explicitly say **keyword-matching against the job description is a hard gate** before a human ever reads the resume, more so than at some other tech companies.
- Beyond keyword match, Adobe screens want demonstrated **cross-functional collaboration and product-thinking** language layered on top of pure technical skill — reflecting Adobe's product-suite (not pure-infra) business.

## 11. Twitter / X

- Limited public hiring-specific guidance is available post-acquisition/restructuring (much of the older "Twitter engineering resume" advice content is now stale or was pulled down). General FAANG-tier norms (scale metrics, systems ownership, concise one-pager) are the best current proxy — treat this one with the least confidence of the group.

## 12. JPMorgan Chase, Goldman Sachs, Morgan Stanley (investment banking cluster)

- All three recruit against nearly identical criteria: **bachelor's (sometimes master's) in finance/econ/accounting from a target school, GPA 3.2–3.5+**, and — above all — recruiters say the first thing they scan for is **years of directly role-relevant experience**, visible in the first few seconds.
- Real shared resumes that got offers consistently show **named deals** (not just "worked on M&A") — e.g., "$500M M&A transaction, led due diligence and financial modeling," "$200M asset acquisition valuation model."
- Associate-level resumes are expected to show an MBA or closely related master's; analyst-level resumes are bachelor's-only.
- Standard format is stricter and more conservative than tech: **2 pages max**, clean reverse-chronological, minimal design, CFA/other certifications called out explicitly when held.

## 13. Wells Fargo, Citibank (retail/commercial banking + banking tech)

- For **banking-technology roles** (not front-office IB), these show up in the same job postings as JPMorgan's tech org — Java/.NET/C#, enterprise web applications, and (increasingly) Python/Kafka/microservices for trading and payments platforms.
- For **retail/branch banking roles**, resumes weight regulatory-compliance keywords heavily: **BSA, AML, USA PATRIOT Act, OCC rules** — these function as hard ATS filters, similar to how "Secret Clearance" functions at a defense contractor.
- Real examples that performed well quantified operational metrics that read almost like manufacturing KPIs: "97% error-free rate across 3,000+ monthly ACH transactions," "reduced processing time by 20%."

## 14. Lockheed Martin (and the broader defense-prime pattern — also applies to Northrop Grumman, Raytheon, Boeing)

- Uses **Workday** as its ATS. The single highest-leverage placement decision on the whole resume: your **security clearance level** (Secret / Top Secret / TS-SCI / Polygraph) needs to appear as a **plain, unstyled single line directly under your name/contact info**, in the top ~25% of the document — Workday's structured field-matching is reported to key off this placement specifically.
- Beyond clearance, the ATS/recruiters scan for defense-specific vocabulary that a generic tech resume won't naturally contain: **DoD 5000, MBSE, Systems Engineering V-Model, ITAR/EAR, Earned Value Management (EVM), DOORS, Cameo**, plus standard technical stack (C++, Python, MATLAB, Linux, FPGA).
- Culture-fit note repeated across multiple sources: Lockheed hiring managers are explicitly **not** looking for "startup velocity" — resumes that read as extremely fast-iteration/move-fast are considered a mismatch; they want signals of long-term program commitment and safety/integrity orientation.
- U.S.-citizenship and clearance-eligibility framing (clean, consistent explanations of any citizenship/background complications) is treated as part of the resume/application narrative, not just an HR form field.

## 15. Thoughtworks

- Explicitly designs its process (branded "Joy of Interviewing") to **let candidates demonstrate skill beyond the resume itself** — meaning the resume screen is a lower-stakes gate here than at a bank or defense contractor, with more weight shifted to live technical/pairing rounds.
- Still, being a technology consultancy, resumes are expected to show **breadth across client engagements/tech stacks** rather than deep tenure at one company — consulting-style resumes that show 3–5 distinct engagements with different tech stacks and outcomes are the norm.

## 16. Accenture

- Explicitly recommends **one page** for students/early-career, two pages only for 10+ years' experience — stricter than most tech companies.
- Cites their own Harvard Business School co-sponsored study: **88% of employers say qualified candidates get filtered out for not matching exact ATS criteria** — Accenture recruiters directly advise using the *exact wording* from the job posting (e.g., "workshop facilitation experience") rather than a paraphrase.
- Consulting-specific bias confirmed by multiple sources: **brand-name schools and brand-name prior employers still carry real weight** in this industry relative to tech, because they're used as a proxy signal to reassure the client the analyst will be credible in the room. This is explicitly said to matter *more* here than in most other industries in this report.
- Strong action verbs (led, built, drove, reduced) plus a number are called the single biggest lever for improving a mediocre consulting resume.

---

## Cross-Company Synthesis — What Actually Repeats Everywhere

1. **Every single company wants a number attached to every bullet.** "Managed X" / "Responsible for Y" is universally called out as the weak pattern; "$-figure, %, latency, headcount, or scale metric" is universally called out as the strong pattern. This is the single most repeated piece of advice across all 16 companies.
2. **Format converges toward boring-on-purpose.** One page (two only with real seniority), single column, standard fonts, no logos/graphics, real text layer (not an image) for ATS parsing. Every company that publishes explicit guidance says some version of this.
3. **Industry vocabulary is a hard gate before a human ever reads the resume.** This is most extreme at Lockheed Martin (clearance keyword placement), Accenture (exact job-posting phrasing), and the industrial-automation cluster (named robot/PLC brands) — but it's present everywhere in some form.
4. **"Named, verifiable specifics" beat "impressive-sounding generalities" everywhere** — named clients/deals in banking, named robot platforms in automation, named systems/scale in tech, named competitions/inventions at Tesla.
5. **Culture-fit signals differ sharply by company and are worth mirroring:** safety/alignment engagement at Anthropic and OpenAI, "evidence of excellence"/builder mentality at Tesla, long-term program commitment and integrity narrative at Lockheed Martin, brand pedigree at Accenture/Goldman/Morgan Stanley, breadth-of-engagement at Thoughtworks.
6. **Where pedigree (school/employer brand) matters most:** investment banking (Goldman/JPM/Morgan Stanley/BlackRock) and traditional consulting (Accenture) — explicitly confirmed by multiple sources. **Where it matters least:** Anthropic, OpenAI, Tesla, and Boston Dynamics, all of which explicitly say they hire on demonstrated ability over credentials.

---

*Sources: company career-site hiring guides (Anthropic, OpenAI, Accenture, Thoughtworks, Lockheed Martin postings), recruiter-interview aggregator sites (IGotAnOffer, ResumeWorded, ResumeAdapter, CVCompiler), Glassdoor/Built In job posting data, and a third-party LinkedIn-resume analysis of Anthropic engineers. Compiled July 2026 — some figures (comp, headcount) may have shifted since.*
