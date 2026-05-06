
## 2026-05-06

Manual literature review expansion centered on the Dubrovin / Gamma conjectures dictionary. Section 2.1 rewritten to (a) split Dubrovin's 1998 conjecture into qualitative and quantitative parts with explicit Stokes-matrix–Gram-matrix identification, (b) define $\widehat{\Gamma}^\pm_X$ via the Hirzebruch construction with the Todd-class square-root identity, (c) state Galkin–Golyshev–Iritani Gamma Conjectures I and II explicitly, and (d) describe the Cotti–Dubrovin–Guzzetti monograph (arXiv:2307.02985, LNM 2356, Springer 2024) reconciliation between Dubrovin's $\widehat{\Gamma}^-$ ansatz and GGI's $\widehat{\Gamma}^+$ form, plus the rigorous verification of the refined conjecture for $\mathbb{P}^{k-1}$ and all Grassmannians $G(r,k)$. Traced Gamma II's load-bearing role across the rest of the lit review: §3.1 now records the KKPY enhanced Hodge atoms with $\widehat{\Gamma}$-corrected integral structures; §4 (NMMP) explicitly notes Halpern-Leistner's "Proposal III is in a sense equivalent to Gamma II"; §4.1 (KRZ) and §4.2 (Wu–Zhang G-NMMP) flag Gamma II as a Setup hypothesis. Added GGI 1404.7521 and CDG 2307.02985 to §7 reference list and to §6.1 Conceptual Map (Foundations + Wall-crossing rows).

## 2026-04-21

Added **Fay, "The Very General Verra Fourfold is Irrational"** (arXiv:2604.14850, April 2026) to §3.1 and the reference list. This is the first successful application of the Katzarkov–Kontsevich–Pantev–Yu Hodge-atom framework to a space with Picard rank > 1, extending the technique beyond the Picard-rank-1 cubic-fourfold case. Also added a `PRIORITY_KEYWORDS` mechanism to `src/reviewer.py`: papers whose `matched_keywords` intersect a curated list (Hodge atoms, NMMP, perverse schober, spherical functor, semi-orthogonal decomposition, quantum D-module, Chen-Ruan cohomology, GKZ system, rationality problem, modular symbols, etc.) are now surfaced deterministically in the `<!-- ARXIV_HIGHLIGHTS -->` block as a keyword-pinned bullet list, guarding against the LLM (llama3.2) missing core lit-review topics — the Verra paper was missed by the LLM filter in the 2026-04-19 run despite matching `Hodge atoms`.

## 2026-04-19

Manual literature review expansion. Added new Section 5 on **perverse schobers** as a third categorical framework alongside Hodge atoms and NMMP, with five core references: Kapranov–Schechtman (arXiv:1411.2772, foundations), Bondal–Kapranov–Schechtman (1801.08286, flops/HMMP), Donovan (1703.00592, GIT wall-crossing), Halpern-Leistner–Sam (1601.02030, combinatorial GIT equivalences), and Špenko–Van den Bergh (2007.04924, GKZ systems). Added foundational references that were previously missing: Bridgeland (math/0212237) and Bayer–Lahoz–Macrì–Stellari (1703.10839) for stability conditions; Halpern-Leistner (2010.01127) for derived Θ-stratifications; Donovan–Kuwagaki (1903.11226) for HMS schober mirrors; Bondal–Orlov (math/9712029) and Kawamata (math/0205287) promoted from "classical without arXiv" to the table. New Section 6.1 (Conceptual Map) and rewritten Section 6.2 with 9 exhaustive, non-overlapping open problems each pairing a global question with a concrete first attack. Added keywords `perverse schober`, `spherical functor`, `GKZ system`, `homological minimal model program` to `config.yaml` for future arXiv runs.

## 2026-04-14

Manual pipeline run after automated Monday run was interrupted mid-execution. 25 papers (5 Geometry & Physics, 20 AI for Mathematics) and 2 news items. Also corrected scheduled run time in CLAUDE.md and README.md: the task runs at 9:00pm (not 9:00am) on Mondays.

## 2026-04-06

Added FrenzyMath (AI4M Team, BICMR@PKU) as a new news feed source (`https://frenzymath.com/rss.xml`), focused on AI4Math, Lean 4, and formal verification. Full pipeline run: 36 papers (17 Geometry & Physics, 19 AI for Mathematics) and 3 news items (including 1 from FrenzyMath, 1 from Terence Tao).

## 2026-04-05

Manually updated literature review with three key papers: "Atoms meet symbols" (arXiv:2509.15831, Cavenaghi–Katzarkov–Kontsevich), "Toward the noncommutative minimal model program for Fano varieties" (arXiv:2601.20739, Karube–Robotis–Zuliani), and "The G-Noncommutative minimal model program" (arXiv:2602.20335, Wu–Zhang). Added new Section 3.3 on equivariant atoms/modular symbols and new Section 4 on the NMMP (non-equivariant and G-equivariant). Open problems updated accordingly.

## 2026-04-04

Improved news keyword matching: added `TITLE_KEYWORDS` list (broader terms matched against title only) to complement the existing full-text `KEYWORDS`. Full pipeline run: 36 papers (12 Geometry & Physics, 24 AI for Mathematics) and 2 news items.

## 2026-03-21

Improved search: added title-only keyword matching for AI model names (cs topics), abstract AI keyword matching for math topics, and a second search pass sorted by last-updated date (2000 results) to catch recently revised papers. Full pipeline run: 35 papers (8 Geometry & Physics, 27 AI for Mathematics) and 1 news item.

## 2026-03-08

Tightened AI for Mathematics keyword list to theorem-proving-only (removed broad AI-capability terms). Re-ran full pipeline: 8 papers (6 Geometry & Physics, 2 formal theorem proving) and 5 news items.

## 2026-03-08

Literature review updated with 7 new paper(s) via Ollama (llama3.2).

## 2026-03-08

Literature review updated with 6 new paper(s) and 15 news item(s) via Ollama (llama3.2).

## 2026-03-08

Literature review updated with 6 new paper(s) and 15 news item(s) via Ollama (llama3.2).
