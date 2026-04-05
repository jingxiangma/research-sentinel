# Literature Review: Birational Invariance of Enumerative Invariants and the Theory of Atoms

## 1. Executive Summary
The study of how enumerative invariants (specifically Gromov-Witten invariants) behave under birational transformations has evolved into a unifying framework connecting **Quantum Cohomology (A-side)** and **Derived Categories of Coherent Sheaves (B-side)**. Historically, the interaction between these two realms was mediated by the Dubrovin conjecture. Today, through the lens of Quantum D-modules, K-equivalence, and the recent introduction of "Hodge Atoms," it is increasingly clear that geometric operations of the Minimal Model Program (MMP) induce canonical decompositions on both the quantum and derived sides.

Three significant recent developments have deepened and broadened this picture. First, **Cavenaghi–Katzarkov–Kontsevich** ("Atoms meet symbols", arXiv:2509.15831) extended the atom framework to the G-equivariant setting by merging it with the theory of modular symbols, giving rise to **Chen-Ruan atoms** and new rationality invariants for group actions. Second, **Karube–Robotis–Zuliani** ("Toward the noncommutative minimal model program for Fano varieties", arXiv:2601.20739) implemented Halpern-Leistner's **Noncommutative Minimal Model Program (NMMP)** concretely for Grassmannians, smooth quadrics, and cubic threefolds and fourfolds by constructing explicit lifts of Iritani's quantum cohomology central charge. Third, **Wu–Zhang** ("The G-Noncommutative minimal model program", arXiv:2602.20335) extended the NMMP itself to the G-equivariant setting using Bridgeland stability conditions on equivariant derived categories and a novel notion of $\mathbb{T}$-stability conditions. Together these works mark the emergence of a fully equivariant, noncommutative framework for birational geometry.

## 2. Foundational Theory: Dubrovin, Iritani, and K-Equivalence

### 2.1 The Dubrovin Conjecture and Gamma Integral Structure
The modern bridge between enumerative geometry and derived categories began with the **Dubrovin Conjecture**, which posited that the quantum cohomology $QH^*(X)$ of a Fano manifold is semisimple if and only if its bounded derived category $D^b(X)$ admits a full exceptional collection. Early computational evidence for these structures was laid out in Bayer and Manin's *(Semi)simple exercises in quantum cohomology*.

A precise mathematical formulation of this bridge was achieved by **Hiroshi Iritani** via the $\widehat{\Gamma}$-integral structure. Iritani demonstrated that the flat sections of the quantum connection (the Dubrovin connection) over the punctured disk can be mapped to the K-theory of $X$.
* The **$\widehat{\Gamma}$-class** is a transcendental characteristic class given by $\widehat{\Gamma}_X = \prod \Gamma(1+\delta_i)$, where $\delta_i$ are the Chern roots of $T_X$.
* This structure essentially acts as a "square root" of the Todd class, formalizing the isomorphism between the Quantum D-module $QDM(X)$ and the topological K-theory of the derived category.

### 2.2 Crepant vs. Discrepant Resolutions
The behavior of these structures under birational maps splits into two distinct paradigms based on the canonical class:

* **Crepant Resolutions (K-equivalence):** When two varieties $X$ and $Y$ are K-equivalent (meaning their canonical classes pull back to the same class on a common resolution), **Ruan's Crepant Resolution Conjecture (CRC)** asserts that their quantum cohomologies are isomorphic after analytic continuation in the Novikov variables. This was rigorously studied by Coates–Iritani–Corti–Tseng and Coates–Iritani–Jiang in the toric setting. On the B-side, the **DK-equivalence conjecture** (Bondal–Orlov, Kawamata) states that K-equivalent varieties share equivalent derived categories: $D^b(X) \simeq D^b(Y)$.
* **Discrepant Resolutions (Blow-ups):** When a birational map alters the canonical class (e.g., a smooth blow-up), the structures decompose rather than remain equivalent. Orlov's celebrated blow-up formula shows that a blow-up induces a Semi-Orthogonal Decomposition (SOD) on the derived category. Mirroring this, Iritani proved a **Blow-up Formula for Quantum Cohomology**, demonstrating that the Quantum D-module decomposes into orthogonal direct summands corresponding to the exceptional divisor.

## 3. State of the Art: The Theory of Atoms

The conceptual leap from "decompositions under blow-up" to an intrinsic "atomic theory" of varieties has been a major recent breakthrough, bringing birational geometry and non-commutative motives together.

### 3.1 The A-Side: Hodge Atoms and Quantum Multiplication
Recent work by **Katzarkov, Kontsevich, Pantev, and Yu** formalized the theory of **Hodge Atoms**. Building on Iritani's blow-up formula, they study the "F-bundle" (a non-archimedean version of a non-commutative Hodge structure) over the Frobenius manifold of $X$.
* Under the action of the Euler vector field, the spectral decomposition of this F-bundle yields canonical, indivisible pieces called *atoms*.
* These atoms behave additively under blow-ups. Because they are strict birational invariants, they provide a powerful new tool for attacking rationality problems (e.g., establishing the non-rationality of very general cubic fourfolds by showing their atomic decomposition contains an atom that cannot come from a rational surface).
* Furthermore, they established that the quantum D-module of product varieties $QDM(X \times Y)$ admits a formal isomorphism to $QDM(X) \otimes QDM(Y)$ at the leading order of the quantum connection, allowing for the computation of atoms for product spaces.

### 3.2 The B-Side: Atomic Decompositions in Derived Categories
Parallel to the A-side quantum developments, **Elagin, Schneider, and Shinder** established the derived-category analogue in their work *Atomic decompositions for derived categories of $G$-surfaces*.
* They constructed canonical semi-orthogonal decompositions for derived categories of smooth projective surfaces that are strictly compatible with MMP operations (blow-ups and conic bundles).
* By doing so, they confirmed a dimension-two conjecture by Kontsevich, defining "derived atoms" that characterize rationality and birationality. The Sarkisov link factorization of birational maps between Mori fibre spaces is used to ensure these SODs mutate consistently.

### 3.3 Equivariant Extensions: Chen-Ruan Atoms and Modular Symbols
**Cavenaghi, Katzarkov, and Kontsevich** ("Atoms meet symbols", arXiv:2509.15831, September 2025) substantially extended the atom framework to **G-equivariant birational geometry** by unifying two previously separate theories:
* The **theory of atoms** (Katzarkov–Kontsevich–Pantev–Yu, A-side)
* The **theory of modular symbols** (Kontsevich–Tschinkel–Pestun)

Key contributions include:
* **Chen-Ruan atoms:** An initiation of atom theory for orbifolds and global quotient stacks, contingent on a blowup formula for quantum Chen-Ruan cohomology. This opens the atom framework to the stacky/orbifold setting, which is central to the equivariant MMP.
* **Geometric invariants for group actions:** Explicit constructions of new birational invariants for $\mathbb{Z}/2$- and $\mathbb{Z}/3$-actions on surfaces and threefolds.
* **Non-linearizability obstructions:** Applications to detecting non-$G$-linearizable group actions on projective varieties — a classical problem in equivariant birational geometry that resisted attack by earlier methods.

The merging with modular symbols indicates that the atom theory has a combinatorial/arithmetic shadow, potentially linking it to motivic cohomology.

## 4. The Noncommutative Minimal Model Program

Halpern-Leistner's **Noncommutative Minimal Model Program (NMMP)** proposes running an analog of Mori's MMP entirely within the space of Bridgeland stability conditions $\text{Stab}(D^b(X))$. The key idea is that quasi-convergent paths in stability condition space — paths that asymptotically degenerate toward a boundary wall — induce the semi-orthogonal decompositions that mirror classical MMP contractions. The central charge of such a path is required to lift Iritani's quantum cohomology central charge, directly linking the A-side to the B-side.

Two papers in early 2026 provide the first substantial concrete implementations of this program.

### 4.1 The Non-Equivariant Case: Fano Varieties
**Karube, Robotis, and Zuliani** ("Toward the noncommutative minimal model program for Fano varieties", arXiv:2601.20739, January 2026) carry out the NMMP explicitly for a range of classical Fano varieties:
* **Grassmannians and smooth quadrics:** Lifts of Iritani's central charge are constructed, quasi-convergence is verified, and the resulting SODs match the classically known exceptional collections.
* **Cubic threefolds and fourfolds:** These are geometrically subtle cases — the cubic fourfold is a central object in rationality theory. The paper establishes geometric stability conditions and shows that the quasi-convergent paths can be **reoriented to start in the geometric region** after appropriate isomonodromic deformations, ensuring the NMMP path connects to honest sheaf-theoretic stability.
* The work verifies that the SODs produced by NMMP paths on these varieties align with previously known decompositions (e.g., Kuznetsov's residual categories for cubic fourfolds), providing strong evidence for the coherence of the NMMP framework.

### 4.2 The G-Equivariant Case
**Wu and Zhang** ("The $G$-Noncommutative minimal model program", arXiv:2602.20335, February 2026) extend the NMMP to the **G-equivariant setting**, working with Bridgeland stability conditions on $D^b_G(X)$ (derived categories of G-equivariant coherent sheaves):
* **Finite group actions:** Induction techniques are used to lift non-equivariant quasi-convergent paths to the equivariant derived category, extending the NMMP to $D^b_G(X)$ for finite $G$.
* **$\mathbb{T}$-stability conditions:** For algebraic group actions, a new notion of $\mathbb{T}$-stability condition is introduced — a torus-equivariant version of Bridgeland stability — providing a framework for stability in settings where classical Bridgeland conditions do not directly apply.
* **Equivariant projective spaces:** Quasi-convergent paths are explicitly constructed for equivariant projective spaces using small quantum cohomology, giving the first concrete examples of G-NMMP paths.

Together, these two papers establish that the NMMP is not merely a formal proposal but a computationally accessible framework, and that it extends naturally to equivariant contexts — bringing it into direct dialogue with the Chen-Ruan atom theory of Section 3.3.

## 5. Synthesis and Current Open Problems

The overarching philosophy is that the A-side (Hodge atoms via Quantum D-modules) and the B-side (Derived atoms via SODs) are two manifestations of the same underlying non-commutative motivic decomposition. The NMMP provides a concrete mechanism for passing between sides: a quasi-convergent path in $\text{Stab}(D^b(X))$ whose central charge lifts the A-side quantum cohomology data automatically produces B-side SODs. The equivariant extensions (Sections 3.3 and 4.2) show that this philosophy is robust enough to accommodate group actions.

**Current Bottlenecks & Open Problems:**

1. **Blowup formula for Chen-Ruan cohomology:** The construction of Chen-Ruan atoms (Section 3.3) is contingent on a blowup formula for quantum Chen-Ruan cohomology of orbifolds — this formula has not yet been established in general and is the key missing ingredient for the full equivariant atom theory.

2. **Higher-Dimensional Derived Atoms:** While Elagin, Schneider, and Shinder solved the $G$-surface case, and the NMMP papers handle Grassmannians and cubics, extending *canonical* atomic SODs to arbitrary Fano threefolds and beyond (where the MMP is vastly more complex) remains open. The NMMP framework suggests a path via quasi-convergent paths, but verifying quasi-convergence in general is hard.

3. **The Exact A-to-B Dictionary:** The NMMP partially addresses this — Iritani's central charge on the A-side is lifted to produce B-side SODs — but a rigorous equivalence between Hodge atoms (A-side) and derived atoms (B-side) for *arbitrary* Fano varieties remains open. This is a "Birational Dubrovin Conjecture."

4. **Modular Symbols and Motivic Integration:** The merger of atoms with modular symbols (Section 3.3) suggests a deeper link to motivic cohomology and arithmetic geometry. Making this connection precise — and understanding what the modular symbols count arithmetically — is a new open direction.

5. **Physics Interpretations:** Translating these atomic decompositions into the language of $\mathcal{N}=2$ supersymmetric gauge theories (e.g., how BPS states or Seiberg-Witten geometries decompose under atomic splits) remains largely unexplored. The equivariant extensions may have natural interpretations in terms of orbifold string theory.

## 6. Reference List

All papers cited in this review with arXiv links, sorted from most to least recent. Classical papers that predate arXiv are listed separately below.

| Date | Authors | Title | arXiv |
|---|---|---|---|
| Feb 2026 | Dongjian Wu, Nantao Zhang | The $G$-Noncommutative Minimal Model Program | [2602.20335](https://arxiv.org/abs/2602.20335) |
| Jan 2026 | Tomohiro Karube, Antonios-Alexandros Robotis, Vanja Zuliani | Toward the Noncommutative Minimal Model Program for Fano Varieties | [2601.20739](https://arxiv.org/abs/2601.20739) |
| Dec 2025 | Alexey Elagin, Julia Schneider, Evgeny Shinder | Atomic Decompositions for Derived Categories of $G$-Surfaces | [2512.05064](https://arxiv.org/abs/2512.05064) |
| Sep 2025 | Leonardo F. Cavenaghi, Ludmil Katzarkov, Maxim Kontsevich | Atoms Meet Symbols | [2509.15831](https://arxiv.org/abs/2509.15831) |
| Aug 2025 | Ludmil Katzarkov, Maxim Kontsevich, Tony Pantev, Renke Yu | Birational Invariants from Hodge Structures and Quantum Multiplication | [2508.05105](https://arxiv.org/abs/2508.05105) |
| Jul 2023 | Hiroshi Iritani | Quantum Cohomology of Blowups | [2307.13555](https://arxiv.org/abs/2307.13555) |
| Jan 2023 | Daniel Halpern-Leistner | The Noncommutative Minimal Model Program | [2301.13168](https://arxiv.org/abs/2301.13168) |
| Feb 2019 | Maxim Kontsevich, Vasily Pestun, Yuri Tschinkel | Equivariant Birational Geometry and Modular Symbols | [1902.09894](https://arxiv.org/abs/1902.09894) |
| Sep 2014 | Tom Coates, Hiroshi Iritani, Yunfeng Jiang | The Crepant Transformation Conjecture for Toric Complete Intersections | [1410.0024](https://arxiv.org/abs/1410.0024) |
| Mar 2009 | Hiroshi Iritani | An Integral Structure in Quantum Cohomology and Mirror Symmetry for Toric Orbifolds | [0903.1463](https://arxiv.org/abs/0903.1463) |
| Aug 2008 | Alexander Kuznetsov | Derived Categories of Cubic Fourfolds | [0808.3351](https://arxiv.org/abs/0808.3351) |
| Apr 2007 | Tom Coates, Alessio Corti, Hiroshi Iritani, Hsian-Hua Tseng | The Crepant Resolution Conjecture for Type A Surface Singularities | [0704.2034](https://arxiv.org/abs/0704.2034) |
| Aug 2001 | Yongbin Ruan | Cohomology Ring of Crepant Resolutions of Orbifolds | [math/0108195](https://arxiv.org/abs/math/0108195) |
| Mar 2001 | Arend Bayer, Yuri Manin | (Semi)simple Exercises in Quantum Cohomology | [math/0103164](https://arxiv.org/abs/math/0103164) |

**Classical references without arXiv:**
- **Orlov** (1992) — Projective bundles, monoidal transformations, and derived categories of coherent sheaves. *Izv. Ross. Akad. Nauk Ser. Mat.* 56(4). *(Blow-up formula for derived categories.)*
- **Bondal–Orlov** (ICM 2002) / **Kawamata** — DK-equivalence conjecture: derived categories of K-equivalent varieties are equivalent.

<!-- BEGIN:ARXIV_HIGHLIGHTS -->
The papers most relevant to Hodge atoms, K-equivalence, derived categories, and quantum D-modules are [Spin Ruijsenaars-Schneider models are Coulomb branches](http://arxiv.org/abs/2603.03048v1) by Gleb Arutyunov and Lukas Hardi, which studies the connection between Coulomb branches and Poisson structures, and [Special Lagrangian smoothings, Calabi ansatz and stability conditions](http://arxiv.org/abs/2603.02749v1) by Jacopo Stoppa, which discusses stability conditions in the context of Calabi ansatz and derived categories.
<!-- END:ARXIV_HIGHLIGHTS -->
