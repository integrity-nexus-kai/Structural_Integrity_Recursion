# Rigorous Relative Perturbation Bound

## Purpose

This document establishes a rigorous perturbative boundedness result for the recursive perturbation sector introduced within the exploratory Yang–Mills Interface framework of Structural Integrity Recursion (SIR).

The objective is not proving the Yang–Mills Mass Gap problem.

Instead, the purpose is establishing mathematically controlled perturbative behavior for the simplified continuum model operator.

The framework remains exploratory and mathematically structural.

---

# 1. Hilbert Space

Let:

\[
\mathcal H
=
L^2([0,1])
\]

with norm:

\[
\|\psi\|^2
=
\int_0^1
|\psi(x)|^2dx
\]

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

defined on:

\[
\mathcal D(H_0)
=
H^2([0,1])
\cap
H_0^1([0,1])
\]

subject to Dirichlet boundary conditions.

---

# 3. Recursive Perturbation Sector

Define the recursive perturbation potential:

\[
V_{\mathrm{rec}}(x)
=
\epsilon\sin(4\pi x)
+
\frac{\alpha}{1+\beta x^2}
\]

with parameters:

\[
\epsilon,\alpha,\beta>0
\]

The perturbation operator acts as multiplication by:

\[
V_{\mathrm{rec}}(x)
\]

on:

\[
L^2([0,1])
\]

---

# 4. Boundedness of the Trigonometric Sector

Since:

\[
|\sin(4\pi x)|\le1
\]

for all:

\[
x\in[0,1]
\]

it follows that:

\[
|\epsilon\sin(4\pi x)|
\le
\epsilon
\]

Therefore the trigonometric perturbation sector is bounded.

---

# 5. Boundedness of the Rational Sector

Since:

\[
1+\beta x^2\ge1
\]

for all:

\[
x\in[0,1]
\]

we obtain:

\[
\left|
\frac{\alpha}{1+\beta x^2}
\right|
\le
\alpha
\]

Therefore the rational perturbation sector is also bounded.

---

# 6. Uniform Perturbation Bound

Combining both estimates yields:

\[
|V_{\mathrm{rec}}(x)|
\le
\epsilon+\alpha
\]

for all:

\[
x\in[0,1]
\]

Define:

\[
C
=
\epsilon+\alpha
\]

Then:

\[
|V_{\mathrm{rec}}(x)|
\le
C
\]

uniformly on:

\[
[0,1]
\]

---

# 7. Rigorous Perturbation Bound Lemma

## Lemma

Let:

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

Then the multiplication operator:

\[
V_{\mathrm{rec}}
:
L^2([0,1])
\rightarrow
L^2([0,1])
\]

is bounded.

Moreover:

\[
\|V_{\mathrm{rec}}\psi\|
\le
C\|\psi\|
\]

for all:

\[
\psi\in L^2([0,1])
\]

where:

\[
C=\epsilon+\alpha
\]

---

# 8. Proof

Using the uniform estimate:

\[
|V_{\mathrm{rec}}(x)|
\le
C
\]

we compute:

\[
|V_{\mathrm{rec}}(x)\psi(x)|^2
\le
C^2|\psi(x)|^2
\]

Integrating over:

\[
[0,1]
\]

gives:

\[
\int_0^1
|V_{\mathrm{rec}}(x)\psi(x)|^2dx
\le
C^2
\int_0^1
|\psi(x)|^2dx
\]

Therefore:

\[
\|V_{\mathrm{rec}}\psi\|^2
\le
C^2\|\psi\|^2
\]

Taking square roots yields:

\[
\|V_{\mathrm{rec}}\psi\|
\le
C\|\psi\|
\]

which proves boundedness of the multiplication operator.

\[
\Box
\]

---

# 9. Relation to Relative Boundedness

Since:

\[
V_{\mathrm{rec}}
\]

is bounded on:

\[
L^2([0,1])
\]

it follows immediately that:

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

This provides a mathematically controlled perturbative baseline for subsequent self-adjointness investigations.

---

# 10. Interpretation

The present result establishes:

- rigorous boundedness of the recursive perturbation sector,
- rigorous perturbative operator control,
- and relative boundedness with respect to the reference operator.

This does NOT establish a Yang–Mills Mass Gap proof.

The result applies only to the simplified continuum model operator introduced within the exploratory framework.

---

# 11. Current Scientific Position

The scientifically correct current position is:

- the recursive perturbation sector defines a bounded multiplication operator on:
  
\[
L^2([0,1])
\]

- the perturbation is rigorously controlled relative to the reference operator,
- and the framework now contains a mathematically rigorous perturbative boundedness result.

No rigorous Yang–Mills Mass Gap proof is currently claimed.

---

# 12. Long-Term Objective

The long-term objective is extending rigorous perturbative analysis toward:

- self-adjoint continuum operators,
- controlled continuum evolution,
- vacuum-relative spectral persistence,
- and continuum-stable lower spectral organization

within progressively more physically meaningful non-linear gauge systems.

At the current stage, the framework remains exploratory mathematical research only.
