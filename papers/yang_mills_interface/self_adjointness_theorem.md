# Self-Adjointness Theorem

## Purpose

This document establishes self-adjointness of the simplified continuum model operator introduced within the exploratory Yang–Mills Interface framework of Structural Integrity Recursion (SIR).

The objective is not proving the Yang–Mills Mass Gap problem.

Instead, the purpose is establishing mathematically controlled operator-theoretic consistency for the simplified continuum baseline model.

The framework remains exploratory and mathematically structural.

---

# 1. Hilbert Space

Let:

\[
\mathcal H
=
L^2([0,1])
\]

equipped with the standard inner product.

---

# 2. Reference Operator

Define the reference operator:

\[
H_0
=
-\Delta
+
\kappa(x-\tfrac12)^2
+
\mu I
\]

with:

\[
\kappa>0,
\qquad
\mu>0
\]

The Laplacian is defined by:

\[
-\Delta
=
-\frac{d^2}{dx^2}
\]

subject to Dirichlet boundary conditions.

The operator domain is:

\[
\mathcal D(H_0)
=
H^2([0,1])
\cap
H_0^1([0,1])
\]

---

# 3. Recursive Perturbation Sector

Define the recursive perturbation operator:

\[
V_{\mathrm{rec}}(x)
=
\epsilon\sin(4\pi x)
+
\frac{\alpha}{1+\beta x^2}
\]

with:

\[
\epsilon,\alpha,\beta>0
\]

The full operator is:

\[
H
=
H_0
+
V_{\mathrm{rec}}
\]

---

# 4. Perturbative Boundedness Result

The previous perturbation-bound analysis established that:

\[
V_{\mathrm{rec}}
:
L^2([0,1])
\rightarrow
L^2([0,1])
\]

defines a bounded multiplication operator.

In particular:

\[
\|V_{\mathrm{rec}}\psi\|
\le
C\|\psi\|
\]

for all:

\[
\psi\in L^2([0,1])
\]

with:

\[
C=\epsilon+\alpha
\]

Therefore:

\[
V_{\mathrm{rec}}
\]

is relatively bounded with respect to:

\[
H_0
\]

with relative bound:

\[
a=0
\]

---

# 5. Self-Adjointness of the Reference Operator

The operator:

\[
H_0
=
-\Delta
+
\kappa(x-\tfrac12)^2
+
\mu I
\]

with Dirichlet boundary conditions defines a standard Schrödinger operator on:

\[
L^2([0,1])
\]

Since:

- the potential is real-valued,
- continuous,
- and bounded from below,

the operator:

\[
H_0
\]

is self-adjoint on:

\[
\mathcal D(H_0)
=
H^2([0,1])
\cap
H_0^1([0,1])
\]

This is a classical result from Schrödinger operator theory.

---

# 6. Kato–Rellich Theorem

## Theorem (Kato–Rellich)

Let:

\[
A
\]

be self-adjoint on:

\[
\mathcal D(A)
\]

and let:

\[
B
\]

be symmetric and relatively bounded with respect to:

\[
A
\]

with relative bound:

\[
a<1
\]

Then:

\[
A+B
\]

is self-adjoint on:

\[
\mathcal D(A)
\]

---

# 7. Application to the Model Operator

In the present framework:

\[
A=H_0
\]

and:

\[
B=V_{\mathrm{rec}}
\]

The perturbation operator is bounded, hence relatively bounded with relative bound:

\[
a=0<1
\]

Therefore all assumptions of the Kato–Rellich theorem are satisfied.

---

# 8. Self-Adjointness Theorem

## Theorem

Let:

\[
H
=
-\Delta
+
\kappa(x-\tfrac12)^2
+
\mu I
+
V_{\mathrm{rec}}
\]

with:

\[
V_{\mathrm{rec}}(x)
=
\epsilon\sin(4\pi x)
+
\frac{\alpha}{1+\beta x^2}
\]

where:

\[
\kappa,\mu,\epsilon,\alpha,\beta>0
\]

Then:

\[
H
\]

is self-adjoint on:

\[
\mathcal D(H)
=
H^2([0,1])
\cap
H_0^1([0,1])
\]

---

# 9. Proof

The reference operator:

\[
H_0
\]

is self-adjoint on:

\[
\mathcal D(H_0)
\]

by standard Schrödinger operator theory.

The perturbation operator:

\[
V_{\mathrm{rec}}
\]

is bounded on:

\[
L^2([0,1])
\]

hence relatively bounded with respect to:

\[
H_0
\]

with relative bound:

\[
a=0<1
\]

Applying the Kato–Rellich theorem yields:

\[
H
=
H_0+V_{\mathrm{rec}}
\]

is self-adjoint on:

\[
\mathcal D(H_0)
\]

which proves the claim.

\[
\Box
\]

---

# 10. Interpretation

The present result establishes:

- mathematically controlled self-adjointness,
- well-defined spectral theory,
- well-defined eigenvalue structure,
- and controlled perturbative operator evolution

for the simplified continuum model operator.

This does NOT establish a Yang–Mills Mass Gap proof.

The result applies only to the simplified continuum operator baseline introduced within the exploratory framework.

---

# 11. Current Scientific Position

The scientifically correct current position is:

- the simplified continuum model operator is rigorously self-adjoint,
- the operator possesses mathematically controlled spectral structure,
- and the framework now contains a rigorous operator-theoretic consistency result.

No rigorous Yang–Mills Mass Gap proof is currently claimed.

---

# 12. Long-Term Objective

The long-term objective is extending rigorous operator-theoretic analysis toward:

- continuum-stable spectral persistence,
- vacuum-relative excitation separation,
- gauge-consistent continuum operators,
- and dynamically generated effective-mass structures

within progressively more physically meaningful non-linear gauge systems.

At the current stage, the framework remains exploratory mathematical research only.
