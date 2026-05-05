# Literature Review: Birational Invariance of Enumerative Invariants and the Theory of Atoms

## 1. Executive Summary
The study of how enumerative invariants (specifically Gromov-Witten invariants) behave under birational transformations has evolved into a unifying framework connecting **Quantum Cohomology (A-side)** and **Derived Categories of Coherent Sheaves (B-side)**. Historically, the interaction between these two realms was mediated by the Dubrovin conjecture. Today, through the lens of Quantum D-modules, K-equivalence, and the recent introduction of "Hodge Atoms," it is increasingly clear that geometric operations of the Minimal Model Program (MMP) induce canonical decompositions on both the quantum and derived sides.

Three parallel categorical frameworks now organize these decompositions: **Hodge atoms** (A-side spectral pieces of the quantum D-module), the **Noncommutative Minimal Model Program (NMMP)** (Bridgeland stability conditions and quasi-convergent paths), and **perverse schobers** (gluing data of triangulated categories on a base, with spherical-functor monodromy). Each captures a different facet of the same underlying phenomenon — the SODs and equivalences induced by birational transformations, GIT wall-crossings, and flops.

Three significant recent developments have deepened and broadened this picture. First, **Cavenaghi–Katzarkov–Kontsevich** ("Atoms meet symbols", arXiv:2509.15831) extended the atom framework to the G-equivariant setting by merging it with the theory of modular symbols, giving rise to **Chen-Ruan atoms** and new rationality invariants for group actions. Second, **Karube–Robotis–Zuliani** ("Toward the noncommutative minimal model program for Fano varieties", arXiv:2601.20739) implemented Halpern-Leistner's NMMP concretely for Grassmannians, smooth quadrics, and cubic threefolds and fourfolds by constructing explicit lifts of Iritani's quantum cohomology central charge. Third, **Wu–Zhang** ("The G-Noncommutative minimal model program", arXiv:2602.20335) extended the NMMP itself to the G-equivariant setting using Bridgeland stability conditions on equivariant derived categories and a novel notion of $\mathbb{T}$-stability conditions. Together these works mark the emergence of a fully equivariant, noncommutative framework for birational geometry.

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
**Katzarkov, Kontsevich, Pantev, and Yu** ("Birational Invariants from Hodge Structures and Quantum Multiplication", arXiv:2508.05105, August 2025) formalized the theory of **Hodge Atoms**. Building on Iritani's blow-up formula, they study the "F-bundle" (a non-archimedean version of a non-commutative Hodge structure) over the Frobenius manifold of $X$.
* Under the action of the Euler vector field, the spectral decomposition of this F-bundle yields canonical, indivisible pieces called *atoms*.
* These atoms behave additively under blow-ups. Because they are strict birational invariants, they provide a powerful new tool for attacking rationality problems (e.g., establishing the non-rationality of very general cubic fourfolds by showing their atomic decomposition contains an atom that cannot come from a rational surface).
* Furthermore, they established that the quantum D-module of product varieties $QDM(X \times Y)$ admits a formal isomorphism to $QDM(X) \otimes QDM(Y)$ at the leading order of the quantum connection, allowing for the computation of atoms for product spaces.

The first substantial extension of this program beyond the original cubic-fourfold setting is due to **Fay** ("The Very General Verra Fourfold is Irrational", arXiv:2604.14850, April 2026), who applies the Hodge atom framework to establish irrationality of the very general Verra fourfold. Two advances underpin the result: (i) a refined analysis of Hodge atoms exploiting the involution on $H^*(X)$, and (ii) a derivation of the quantum multiplication matrix directly from the quantum differential operator. Crucially, this is the **first successful application of Hodge atoms to a space with Picard rank greater than one**, establishing that the technique generalizes beyond the Picard-rank-one setting in which the KKPY framework was originally tested.

### 3.2 The B-Side: Atomic Decompositions in Derived Categories
Parallel to the A-side quantum developments, **Elagin, Schneider, and Shinder** ("Atomic decompositions for derived categories of $G$-surfaces", arXiv:2512.05064, December 2025) established the derived-category analogue.
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

The technical engine for this program is the theory of **derived $\Theta$-stratifications**, developed by Halpern-Leistner ("Derived $\Theta$-stratifications and the $D$-equivalence conjecture", arXiv:2010.01127, October 2020). Θ-stratifications generalize the Białynicki-Birula / GIT instability stratification to derived algebraic stacks, providing the local model for how an SOD splits off when crossing a wall. They underlie both the NMMP construction and the GIT-equivalence results of Halpern-Leistner–Sam (§5.3); foundational Bridgeland stability is taken from Bridgeland ("Stability conditions on triangulated categories", arXiv:math/0212237, December 2002), and existence of stability conditions on Kuznetsov components — load-bearing for §4.1's cubic-fourfold results — comes from Bayer–Lahoz–Macrì–Stellari (arXiv:1703.10839, March 2017).

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

## 5. Perverse Schobers: Categorifying Perverse Sheaves

A complementary framework for organizing derived equivalences under birational transformations is the theory of **perverse schobers** — categorifications of perverse sheaves in which stalk vector spaces are replaced by triangulated categories, encoding SOD data via spherical functors on a base.

### 5.1 Foundations
**Kapranov and Schechtman** ("Perverse Schobers", arXiv:1411.2772, November 2014) introduced perverse schobers as a categorical generalization of perverse sheaves. In the simplest case — a disk with one singular point — the data of a perverse schober is equivalent to a **spherical functor** $F: \mathcal{C} \to \mathcal{D}$ between triangulated categories, whose twist and cotwist produce the autoequivalences that act as SOD monodromy around the singular point.

### 5.2 Birational Geometry and Flops
**Bondal, Kapranov, and Schechtman** ("Perverse schobers and birational geometry", arXiv:1801.08286, January 2018) demonstrated that perverse schobers arise naturally in the **Homological Minimal Model Program (HMMP)**, which studies the effect of birational transformations such as flops on coherent derived categories.
* They study schober-type diagrams of categories associated to flops of relative dimension 1, and determine the categorical analogs of (compactly supported) cohomology with coefficients in such schobers.
* They analyze the "web of flops" attached to the Grothendieck resolution of a reductive Lie algebra; for $\mathfrak{sl}(3)$ this diagram recovers the classical space of complete triangles studied by Schubert and Semple.

This work establishes perverse schobers as the natural ambient structure for the derived equivalences predicted by the Bondal–Orlov reconstruction theorem (arXiv:math/9712029, December 1997) and the Kawamata DK-equivalence conjecture (arXiv:math/0205287, May 2002) under K-equivalent birational transformations — and so as a categorical companion to the A-side blowup formula of Section 2.2.

### 5.3 GKZ Systems and Quantum D-modules
**Špenko and Van den Bergh** ("Perverse schobers and GKZ systems", arXiv:2007.04924, July 2020; Adv. Math. 2022) show that a suitable variation of perverse schober **categorifies the GKZ hypergeometric system** in the quasi-symmetric setting. Since GKZ systems control Givental I-functions / quantum periods for toric varieties, this schober categorification provides a B-side lift that directly bridges to the A-side quantum D-module of Section 2.

Taken together, schobers form a third framework — alongside Hodge atoms (A-side, §3) and NMMP via stability conditions (§4) — for organizing the categorical decompositions induced by birational transformations. Reconciling the three languages is the content of open problems 2 (A↔B dictionary) and 3 (schober↔NMMP dictionary) in §6.2 below.

## 6. Synthesis and Current Open Problems

### 6.1 Conceptual Map

The references in §§2–5 organize into three layers:

| Layer | A-Side (quantum / Hodge) | B-Side (categorical) | Bridge / Wall-crossing |
|---|---|---|---|
| **Foundations** | Dubrovin conjecture; Iritani's $\widehat{\Gamma}$-integral structure (0903.1463) | Bondal–Orlov / Kawamata DK-equivalence; Orlov blowup; Kuznetsov residual cats (0808.3351) | Coates–Corti–Iritani–Tseng / Coates–Iritani–Jiang CRC (0704.2034, 1410.0024) |
| **Decomposition formalism** | Iritani quantum blowup formula (2307.13555); Hodge atoms (KKPY, 2508.05105) | Elagin–Schneider–Shinder derived atoms for $G$-surfaces (2512.05064) | Halpern-Leistner–Sam GIT equivalences (1601.02030) |
| **Wall-crossing language** | — | Halpern-Leistner NMMP (2301.13168); Karube–Robotis–Zuliani (2601.20739); Wu–Zhang G-NMMP (2602.20335) | Kapranov–Schechtman schobers (1411.2772); Bondal–Kapranov–Schechtman (1801.08286); Špenko–Van den Bergh GKZ (2007.04924) |
| **Equivariant extensions** | Cavenaghi–Katzarkov–Kontsevich Chen-Ruan atoms (2509.15831) | Elagin–Schneider–Shinder (2512.05064) | Wu–Zhang $\mathbb{T}$-stability (2602.20335); Kontsevich–Pestun–Tschinkel modular symbols (1902.09894) |

The overarching philosophy is that the A-side (Hodge atoms via Quantum D-modules) and the B-side (Derived atoms via SODs) are two manifestations of the same underlying non-commutative motivic decomposition. The NMMP provides one bridge — a quasi-convergent path in $\text{Stab}(D^b(X))$ whose central charge lifts Iritani's, automatically producing B-side SODs. Perverse schobers provide a second, more local bridge: at each wall they encode the wall-crossing equivalence as monodromy of a spherical functor. The equivariant extensions (§§3.3 and 4.2) show the philosophy accommodates group actions.

### 6.2 Open Problems and Proposed Research Directions

The following nine items partition the open territory suggested by the cited literature. Each entry states the global open problem and, where the citations point to one, names a concrete first attack. The list is intended to be exhaustive (covering all open directions identified across §§2–5) and non-overlapping (each entry has a distinct technical core).

1. **Chen-Ruan blowup formula.** The Chen-Ruan atom construction (§3.3) is contingent on a blowup formula for quantum Chen-Ruan cohomology of orbifolds — not yet established in general. This is the key missing ingredient for the full equivariant atom theory; no concrete attack is proposed in the cited literature.

2. **Birational Dubrovin Conjecture (the A-to-B dictionary).** NMMP (§4) lifts Iritani's central charge to produce B-side SODs, but a rigorous equivalence between Hodge atoms (A-side, KKPY 2508.05105) and derived atoms (B-side, Elagin–Schneider–Shinder 2512.05064) for arbitrary Fano varieties is open: atom additivity under blowups should match SOD additivity under Orlov's formula, but no precise theorem connects them. **Concrete attacks:** (a) a *per-atom refinement of Iritani's $\widehat{\Gamma}$-conjecture* (0903.1463) — each Hodge atom's flat sections should be spanned by $\widehat{\Gamma}$-images of objects in the corresponding SOD piece, sharpening the dictionary into a statement about specific bases; (b) a *Mori–Mukai atom catalogue* computing both A- and B-side atomic decompositions for the 105 deformation families of smooth Fano threefolds (matched against Belmans–Galkin–Mukhopadhyay-style SOD catalogues) as a family-by-family testbed.

3. **Schober ↔ NMMP dictionary.** Schobers (§5) and NMMP (§4) encode the same wall-crossing categorical data in different languages, but no cited paper makes the dictionary explicit. **Conjecture:** a quasi-convergent NMMP path approaching a wall produces a perverse schober on a disk transverse to the wall, whose spherical functor recovers the Halpern-Leistner mutation. **Concrete attack:** verify on the cubic threefold, where Karube–Robotis–Zuliani (2601.20739) construct the NMMP path and a Donovan-style schober (1703.00592) should be constructible from Kuznetsov's residual category (0808.3351).

4. **Higher-dimensional derived atoms via direct construction.** Elagin–Schneider–Shinder (2512.05064) construct canonical atomic SODs on surfaces by an intrinsic argument using Sarkisov-link factorization. Extending this *directly* — independent of the A-side dictionary of #2 — to Fano threefolds and beyond is open and presumably requires a higher-dimensional analog of the Sarkisov program for derived categories.

5. **Schobers on stratified bases.** All cited schober work (§5) treats a disk with an isolated singularity. Real wall-crossing in $\text{Stab}(D^b(X))$ happens along higher-codimension strata. A theory of perverse schobers on stratified bases (Riemann surfaces with several punctures, or higher-dimensional bases with constructible stratifications) would match NMMP wall geometry directly and is a natural extension of Kapranov–Schechtman (1411.2772) and Bondal–Kapranov–Schechtman (1801.08286).

6. **Equivariant A↔B comparison.** Wu–Zhang G-NMMP (2602.20335, §4.2) and Cavenaghi–Katzarkov–Kontsevich Chen-Ruan atoms (2509.15831, §3.3) extend their respective frameworks to G-equivariant settings, but no paper compares the resulting decompositions on a shared example. **Concrete attack:** $[\mathbb{P}^n/G]$ for small finite $G$, testing the equivariant version of #2.

7. **Beyond Fano: stability and log atoms.** The Hodge atom construction (KKPY 2508.05105) uses spectral decomposition under the Euler vector field, which degenerates for Calabi–Yau (trivial $K_X$) and general type. Two layers of obstruction: (a) **Foundational** — Bridgeland stability conditions on general Calabi–Yau threefolds remain conjectural (only surfaces, Fano 3folds, and Kuznetsov components of cubic 4folds are covered by Bridgeland math/0212237 and Bayer–Lahoz–Macrì–Stellari 1703.10839); (b) **Constructive** — a "log atom" theory for log Calabi–Yau pairs $(X,D)$ via Gross–Siebert log GW invariants is unexplored and would extend the framework to a much wider class of varieties.

8. **Arithmetic side: L-functions of atoms.** The atoms ↔ modular symbols merger of CKK (2509.15831, §3.3) suggests a deeper link to motivic cohomology and arithmetic geometry. **Concrete refinement:** modular symbols (Kontsevich–Pestun–Tschinkel 1902.09894) carry associated L-functions; if atoms have a modular-symbol shadow, the resulting L-values should give arithmetic invariants of birational equivalence classes — a wholly unexplored arithmetic refinement of the rationality applications.

9. **Physics: Coulomb branches and BPS decomposition.** Translating atomic decompositions into $\mathcal{N}=2$ supersymmetric gauge theories (BPS-state decomposition under atomic splits, Seiberg–Witten interpretations) is largely unexplored. **Concrete attack:** for $X$ a symplectic resolution, the Coulomb branch of the corresponding 3d $\mathcal{N}=4$ gauge theory (Braverman–Finkelberg–Nakajima) carries a quantization often coinciding with $D^b(X)$; an atomic decomposition of $X$ should descend to a decomposition of the Coulomb branch and its quantized algebra of functions, providing a physics realization of the SODs from NMMP and atom theory.

## 7. Reference List

All papers cited in this review with arXiv links, sorted from most to least recent. Classical papers that predate arXiv are listed separately below.

| Date | Authors | Title | arXiv |
|---|---|---|---|
| Apr 2026 | Aideen Fay | The Very General Verra Fourfold is Irrational | [2604.14850](https://arxiv.org/abs/2604.14850) |
| Feb 2026 | Dongjian Wu, Nantao Zhang | The $G$-Noncommutative Minimal Model Program | [2602.20335](https://arxiv.org/abs/2602.20335) |
| Jan 2026 | Tomohiro Karube, Antonios-Alexandros Robotis, Vanja Zuliani | Toward the Noncommutative Minimal Model Program for Fano Varieties | [2601.20739](https://arxiv.org/abs/2601.20739) |
| Dec 2025 | Alexey Elagin, Julia Schneider, Evgeny Shinder | Atomic Decompositions for Derived Categories of $G$-Surfaces | [2512.05064](https://arxiv.org/abs/2512.05064) |
| Sep 2025 | Leonardo F. Cavenaghi, Ludmil Katzarkov, Maxim Kontsevich | Atoms Meet Symbols | [2509.15831](https://arxiv.org/abs/2509.15831) |
| Aug 2025 | Ludmil Katzarkov, Maxim Kontsevich, Tony Pantev, Renke Yu | Birational Invariants from Hodge Structures and Quantum Multiplication | [2508.05105](https://arxiv.org/abs/2508.05105) |
| Jul 2023 | Hiroshi Iritani | Quantum Cohomology of Blowups | [2307.13555](https://arxiv.org/abs/2307.13555) |
| Jan 2023 | Daniel Halpern-Leistner | The Noncommutative Minimal Model Program | [2301.13168](https://arxiv.org/abs/2301.13168) |
| Oct 2020 | Daniel Halpern-Leistner | Derived $\Theta$-Stratifications and the $D$-Equivalence Conjecture | [2010.01127](https://arxiv.org/abs/2010.01127) |
| Jul 2020 | Špela Špenko, Michel Van den Bergh | Perverse Schobers and GKZ Systems | [2007.04924](https://arxiv.org/abs/2007.04924) |
| Feb 2019 | Maxim Kontsevich, Vasily Pestun, Yuri Tschinkel | Equivariant Birational Geometry and Modular Symbols | [1902.09894](https://arxiv.org/abs/1902.09894) |
| Jan 2018 | Alexey Bondal, Mikhail Kapranov, Vadim Schechtman | Perverse Schobers and Birational Geometry | [1801.08286](https://arxiv.org/abs/1801.08286) |
| Mar 2017 | Arend Bayer, Martí Lahoz, Emanuele Macrì, Paolo Stellari | Stability Conditions on Kuznetsov Components | [1703.10839](https://arxiv.org/abs/1703.10839) |
| Mar 2017 | Will Donovan | Perverse Schobers and Wall Crossing | [1703.00592](https://arxiv.org/abs/1703.00592) |
| Jan 2016 | Daniel Halpern-Leistner, Steven V. Sam | Combinatorial Constructions of Derived Equivalences | [1601.02030](https://arxiv.org/abs/1601.02030) |
| Nov 2014 | Mikhail Kapranov, Vadim Schechtman | Perverse Schobers | [1411.2772](https://arxiv.org/abs/1411.2772) |
| Sep 2014 | Tom Coates, Hiroshi Iritani, Yunfeng Jiang | The Crepant Transformation Conjecture for Toric Complete Intersections | [1410.0024](https://arxiv.org/abs/1410.0024) |
| Mar 2009 | Hiroshi Iritani | An Integral Structure in Quantum Cohomology and Mirror Symmetry for Toric Orbifolds | [0903.1463](https://arxiv.org/abs/0903.1463) |
| Aug 2008 | Alexander Kuznetsov | Derived Categories of Cubic Fourfolds | [0808.3351](https://arxiv.org/abs/0808.3351) |
| Apr 2007 | Tom Coates, Alessio Corti, Hiroshi Iritani, Hsian-Hua Tseng | The Crepant Resolution Conjecture for Type A Surface Singularities | [0704.2034](https://arxiv.org/abs/0704.2034) |
| Dec 2002 | Tom Bridgeland | Stability Conditions on Triangulated Categories | [math/0212237](https://arxiv.org/abs/math/0212237) |
| May 2002 | Yujiro Kawamata | $D$-Equivalence and $K$-Equivalence | [math/0205287](https://arxiv.org/abs/math/0205287) |
| Aug 2001 | Yongbin Ruan | Cohomology Ring of Crepant Resolutions of Orbifolds | [math/0108195](https://arxiv.org/abs/math/0108195) |
| Mar 2001 | Arend Bayer, Yuri Manin | (Semi)simple Exercises in Quantum Cohomology | [math/0103164](https://arxiv.org/abs/math/0103164) |
| Dec 1997 | Alexei Bondal, Dmitri Orlov | Reconstruction of a Variety from the Derived Category and Groups of Autoequivalences | [math/9712029](https://arxiv.org/abs/math/9712029) |

**Classical references without arXiv:**
- **Orlov** (1992) — Projective bundles, monoidal transformations, and derived categories of coherent sheaves. *Izv. Ross. Akad. Nauk Ser. Mat.* 56(4). *(Blow-up formula for derived categories.)*

<!-- BEGIN:ARXIV_HIGHLIGHTS -->
The papers most relevant to Hodge atoms, K-equivalence, derived categories, and quantum D-modules are [Spin Ruijsenaars-Schneider models are Coulomb branches](http://arxiv.org/abs/2603.03048v1) by Gleb Arutyunov and Lukas Hardi, which studies the connection between Coulomb branches and Poisson structures, and [Special Lagrangian smoothings, Calabi ansatz and stability conditions](http://arxiv.org/abs/2603.02749v1) by Jacopo Stoppa, which discusses stability conditions in the context of Calabi ansatz and derived categories.
<!-- END:ARXIV_HIGHLIGHTS -->
