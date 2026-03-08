# Literature Review: Birational Invariance of Enumerative Invariants and the Theory of Atoms

## 1. Executive Summary
The study of how enumerative invariants (specifically Gromov-Witten invariants) behave under birational transformations has evolved into a unifying framework connecting **Quantum Cohomology (A-side)** and **Derived Categories of Coherent Sheaves (B-side)**. Historically, the interaction between these two realms was mediated by the Dubrovin conjecture. Today, through the lens of Quantum D-modules, K-equivalence, and the recent introduction of "Hodge Atoms," it is increasingly clear that geometric operations of the Minimal Model Program (MMP) induce canonical decompositions on both the quantum and derived sides.

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

## 4. Synthesis and Current Open Problems
The overarching philosophy is that the A-side (Hodge atoms via Quantum D-modules) and the B-side (Derived atoms via SODs) are two manifestations of the same underlying non-commutative motivic decomposition.

**Current Bottlenecks & Open Problems:**
1. **Higher-Dimensional Derived Atoms:** While Elagin, Schneider, and Shinder solved the $G$-surface case using Sarkisov links, extending canonical atomic SODs to dimension 3 and above (where the MMP is vastly more complex) remains open.
2. **The Exact A-to-B Dictionary:** Proving a rigorous equivalence between the Hodge atoms (A-side) and the derived atoms (B-side) for arbitrary Fano varieties, effectively creating a "Birational Dubrovin Conjecture."
3. **Physics Interpretations:** Translating these atomic decompositions into the language of $\mathcal{N}=2$ supersymmetric gauge theories (e.g., how BPS states or Seiberg-Witten geometries decompose under atomic splits).

<!-- BEGIN:ARXIV_HIGHLIGHTS -->
The papers most relevant to Hodge atoms, K-equivalence, derived categories, and quantum D-modules are [Spin Ruijsenaars-Schneider models are Coulomb branches](http://arxiv.org/abs/2603.03048v1) by Gleb Arutyunov and Lukas Hardi, which studies the connection between Coulomb branches and Poisson structures, and [Special Lagrangian smoothings, Calabi ansatz and stability conditions](http://arxiv.org/abs/2603.02749v1) by Jacopo Stoppa, which discusses stability conditions in the context of Calabi ansatz and derived categories.
<!-- END:ARXIV_HIGHLIGHTS -->
