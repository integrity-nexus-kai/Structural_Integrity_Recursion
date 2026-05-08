# TIG Gap Hunting Program

## Goal

This document defines the concrete research path for investigating whether the TIG effective spectral framework can generate an emergent spectral gap.

The central target is:

\[
\inf \sigma(\mathcal{L}_{\mathrm{TIG}}) > 0
\]

for recursively admissible perturbative sectors.

---

# 1. Gap Definition

The TIG spectral operator is:

\[
\mathcal{L}_{\mathrm{TIG}}
=
-\Delta
+
V_{\mathrm{rec}}(x,\beta)
\]

A TIG gap exists if there is a strictly positive constant \(c>0\) such that:

\[
\langle h,\mathcal{L}_{\mathrm{TIG}}h\rangle
\geq
c\|h\|^2
\]

for all admissible perturbations:

\[
h \in \mathcal{D}(\mathcal{L}_{\mathrm{TIG}})
\]

This implies:

\[
\omega_{\min}^2 \geq c > 0
\]

---

# 2. Operator Domain

The first task is defining the admissible domain:

\[
\mathcal{D}(\mathcal{L}_{\mathrm{TIG}})
\]

This includes:

- admissible perturbation functions,
- finite norm condition,
- asymptotic decay,
- boundary conditions,
- regularity assumptions,
- recursive admissibility constraints.

A minimal working choice is:

\[
h \in H^1(\mathcal{M})
\]

with:

\[
\|h\| < \infty
\]

and:

\[
h(x)\rightarrow 0
\quad
\text{as}
\quad
x\rightarrow\infty
\]

---

# 3. Effective Radial Model

The first gap-hunting equation is the radial eigenvalue problem:

\[
-\frac{d^2u}{dx^2}
+
V_{\mathrm{rec}}(x,\beta)u
=
\omega^2u
\]

with:

\[
V_{\mathrm{rec}}(x,\beta)
=
-\frac{\alpha}{x^2}
+
\lambda(\beta-\beta_c)^2
\]

where:

\[
\alpha>0,
\qquad
\lambda>0
\]

and:

\[
\beta_c=
\left(\frac{4}{27}\right)^{1/3}
\]

---

# 4. Main Danger

Near the critical point:

\[
\beta\rightarrow\beta_c
\]

the stabilizing term becomes:

\[
\lambda(\beta-\beta_c)^2 \rightarrow 0
\]

Therefore the gap may close.

This is the central danger zone.

The key question is:

\[
\omega_{\min}(\beta)>0
\quad
\text{near but not necessarily at}
\quad
\beta_c
\]

---

# 5. Lower Bound Test

The quadratic form is:

\[
Q[u]
=
\int
\left(
|u'(x)|^2
+
V_{\mathrm{rec}}(x,\beta)|u(x)|^2
\right)
dx
\]

A gap requires:

\[
Q[u]
\geq
c\|u\|^2
\]

with:

\[
c>0
\]

for all admissible \(u\).

---

# 6. First Analytical Target

Determine parameter regimes where:

\[
-\frac{\alpha}{x^2}
+
\lambda(\beta-\beta_c)^2
\]

does not drive the operator below zero.

The working question is:

\[
\lambda(\beta-\beta_c)^2
>
\text{effective inverse-square instability}
\]

If this holds, TIG may admit a positive lower spectral sector.

---

# 7. Numerical Gap Hunt

Numerically solve:

\[
-\frac{d^2u}{dx^2}
+
\left(
-\frac{\alpha}{x^2}
+
\lambda(\beta-\beta_c)^2
\right)u
=
\omega^2u
\]

Track:

\[
\omega_{\min}(\beta)
\]

for:

\[
\beta < \beta_c,
\qquad
\beta \approx \beta_c,
\qquad
\beta > \beta_c
\]

---

# 8. Expected Outcomes

## Case A — Gap Persists

If:

\[
\omega_{\min}(\beta)>0
\]

over a stable parameter region, TIG has a candidate emergent spectral gap.

---

## Case B — Gap Closes at Criticality

If:

\[
\omega_{\min}(\beta)\rightarrow 0
\quad
\text{as}
\quad
\beta\rightarrow\beta_c
\]

then TIG exhibits critical gap-closing behavior.

This would still be mathematically meaningful.

---

## Case C — Instability

If:

\[
\omega_{\min}^2<0
\]

then the chosen potential or boundary conditions are unstable and must be revised.

---

# 9. Immediate Research Task

The next concrete task is:

> Compute or estimate the lowest eigenvalue of the TIG radial operator as a function of \(\beta\).

This is the first real gap-hunting test.

---

# 10. Current Status

TIG is not yet gap-proven.

TIG is now gap-testable.

The immediate milestone is to determine whether:

\[
\inf \sigma(\mathcal{L}_{\mathrm{TIG}})>0
\]

can hold for a well-defined admissible operator domain.
