# Discrete Spectrum Theorem

## Purpose

This document establishes discreteness of the spectrum for the simplified continuum model operator introduced within the exploratory Yang–Mills Interface framework of Structural Integrity Recursion (SIR).

The objective is not proving the Yang–Mills Mass Gap problem.

Instead, the purpose is establishing mathematically controlled spectral structure for the simplified continuum baseline operator.

The framework remains exploratory and mathematically structural.

---

# 1. Hilbert Space

Let:

\[
\mathcal H
=
L^2([0,1])
\]

equipped with the standard inner product and norm.

---

# 2. Model Operator

Define the operator:

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

where:

\[
V_{\mathrm{rec}}(x)
=
\epsilon\sin(4\pi x)
+
\frac{\alpha}{1+\beta x^2}
\]

with parameters:

\[
\kappa,\mu,\epsilon,\alpha,\beta>0
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
\mathcal D(H)
=
H^2([0,1])
\cap
H_0^1([0,1])
\]

---

# 3. Self-Adjointness Recall

The previous self-adjointness analysis established that:

\[
H
\]

is self-adjoint on:

\[
\mathcal D(H)
\]

The perturbation sector:

\[
V_{\mathrm{rec}}
\]

defines a bounded multiplication operator on:

\[
L^2([0,1])
\]

and therefore preserves self-adjointness through the Kato–Rellich theorem.

---

# 4. Compact Interval Structure

The operator acts on the compact interval:

\[
[0,1]
\]

with Dirichlet boundary conditions.

The confinement and perturbation potentials are bounded on:

\[
[0,1]
\]

Therefore the operator defines a standard one-dimensional Schrödinger operator on a compact domain.

---

# 5. Compact Resolvent Structure

Classical Schrödinger operator theory implies:

- the Dirichlet Laplacian on a compact interval possesses compact resolvent,
- bounded potential perturbations preserve compactness of the resolvent,
- and self-adjoint bounded perturbations preserve discrete spectral structure.

Therefore:

\[
(H-\lambda I)^{-1}
\]

is compact for all:

\[
\lambda
\]

outside the spectrum.

---

# 6. Discrete Spectrum Theorem

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
\kappa,\mu,\epsilon,\alpha,\beta>0
\]

defined on:

\[
\mathcal D(H)
=
H^2([0,1])
\cap
H_0^1([0,1])
\]

with Dirichlet boundary conditions.

Then:

\[
H
\]

possesses purely discrete spectrum.

More precisely:

\[
\sigma(H)
=
\{\lambda_n\}_{n=0}^\infty
\]

where:

- each eigenvalue has finite multiplicity,
- the spectrum is bounded from below,
- and:

\[
\lambda_n\rightarrow\infty
\quad
\text{as}
\quad
n\rightarrow\infty
\]

---

# 7. Proof

The Dirichlet Laplacian on the compact interval:

\[
[0,1]
\]

is self-adjoint and possesses compact resolvent.

The confinement potential:

\[
\kappa(x-\tfrac12)^2
+
\mu
\]

is bounded from below and continuous.

The recursive perturbation sector:

\[
V_{\mathrm{rec}}
\]

is bounded on:

\[
L^2([0,1])
\]

Therefore the full operator:

\[
H
\]

defines a self-adjoint Schrödinger operator with compact resolvent.

Classical spectral theory for compact-resolvent self-adjoint operators implies:

- the spectrum consists entirely of isolated eigenvalues,
- each eigenvalue has finite multiplicity,
- and eigenvalues diverge to:

\[
+\infty
\]

This proves the claim.

\[
\Box
\]

---

# 8. Ground-State Structure

Since the spectrum is discrete and bounded from below, there exists a lowest eigenvalue:

\[
\lambda_0
=
\inf\sigma(H)
\]

corresponding to the ground-state sector.

The first excited spectral level is:

\[
\lambda_1
\]

Therefore the quantity:

\[
\lambda_1-\lambda_0
\]

is mathematically well-defined within the present continuum model.

---

# 9. Interpretation

The present result establishes:

- mathematically controlled discrete spectral structure,
- existence of a well-defined ground state,
- ordered eigenvalue organization,
- and a mathematically meaningful spectral-gap candidate.

This does NOT establish a Yang–Mills Mass Gap proof.

The result applies only to the simplified continuum model operator introduced within the exploratory framework.

---

# 10. Current Scientific Position

The scientifically correct current position is:

- the simplified continuum model operator possesses rigorously discrete spectrum,
- the operator admits a mathematically well-defined ground state,
- and the framework now contains a rigorous discrete-spectrum theorem.

No rigorous Yang–Mills Mass Gap proof is currently claimed.

---

# 11. Long-Term Objective

The long-term objective is extending rigorous spectral analysis toward:

- vacuum-relative spectral separation,
- continuum-stable lower spectral persistence,
- gauge-consistent continuum operators,
- and dynamically generated effective-mass structures

within progressively more physically meaningful non-linear gauge systems.

At the current stage, the framework remains exploratory mathematical research only.
