# Rigorous Global Mass Persistence Attempt

## Purpose

This worksheet investigates whether asymptotic tightness and strong local convergence together prevent global \(L^2\)-mass escape in the simplified continuum operator setting.

The objective is not proving the Yang–Mills Mass Gap problem.

Instead, the purpose is establishing the first genuine non-escape mechanism for asymptotic low-energy states.

---

# 1. Setup

Let:

\[
H_N=-\Delta+V_N
\]

on:

\[
L^2(\mathbb R^d)
\]

with normalized states:

\[
\|\psi_N\|_{L^2}=1
\]

Assume:

\[
\langle \psi_N,H_N\psi_N\rangle\le E
\]

uniformly in \(N\).

Assume additionally:

\[
V_N(x)\ge -C_0
\]

uniformly.

---

# 2. Previously Established Structures

Previous worksheets yielded:

---

## Tightness

For every:

\[
\varepsilon>0
\]

there exists:

\[
R_\varepsilon
\]

such that:

\[
\int_{|x|>R_\varepsilon}
|\psi_N(x)|^2dx
<
\varepsilon
\]

uniformly in \(N\).

---

## Strong Local Convergence

There exists a subsequence:

\[
\psi_{N_k}
\rightarrow
\psi_\infty
\]

strongly in:

\[
L^2_{\mathrm{loc}}(\mathbb R^d)
\]

---

# 3. Compact Localization Region

Fix:

\[
\varepsilon>0
\]

Choose radius:

\[
R_\varepsilon
\]

from tightness.

Define:

\[
B_{R_\varepsilon}
=
\{x\in\mathbb R^d:\ |x|\le R_\varepsilon\}
\]

Then:

\[
\int_{\mathbb R^d\setminus B_{R_\varepsilon}}
|\psi_N|^2dx
<
\varepsilon
\]

uniformly in \(N\).

---

# 4. Interior Mass Persistence

Since:

\[
\psi_{N_k}
\rightarrow
\psi_\infty
\]

strongly in:

\[
L^2(B_{R_\varepsilon})
\]

we obtain:

\[
\int_{B_{R_\varepsilon}}
|\psi_{N_k}|^2dx
\rightarrow
\int_{B_{R_\varepsilon}}
|\psi_\infty|^2dx
\]

---

# 5. Total Mass Control

Using normalization:

\[
\|\psi_N\|_{L^2}=1
\]

we have:

\[
\int_{B_{R_\varepsilon}}
|\psi_N|^2dx
\ge
1-\varepsilon
\]

uniformly in \(N\).

Passing formally to the limit yields:

\[
\int_{B_{R_\varepsilon}}
|\psi_\infty|^2dx
\ge
1-\varepsilon
\]

Hence:

\[
\|\psi_\infty\|_{L^2}
\ge
1-\varepsilon
\]

Since:

\[
\varepsilon>0
\]

was arbitrary, heuristically:

\[
\psi_\infty\neq0
\]

and potentially:

\[
\|\psi_\infty\|_{L^2}=1
\]

---

# 6. Proto-Global Mass Persistence Lemma

If:

1. asymptotic tightness holds,
2. and strong local \(L^2\)-convergence holds,

then asymptotic \(L^2\)-mass escape is suppressed.

Potentially:

\[
\psi_\infty\neq0
\]

and asymptotic low-energy structure remains globally meaningful.

---

# 7. Structural Meaning

This is the first genuine non-escape mechanism in the program.

The chain now becomes:

```text
bounded energy
        ↓
tightness
        ↓
local H¹-bounds
        ↓
Rellich compactness
        ↓
strong local convergence
        ↓
global mass persistence
        ↓
nontrivial limit states
```

---

# 8. Critical Remaining Problem

Even if:

\[
\psi_\infty\neq0
\]

the following remains completely open:

Does:

\[
\psi_\infty
\]

retain meaningful spectral structure?

This is now the central unresolved question.

---

# 9. Next Step

The next worksheet must therefore be:

```text
rigorous_low_energy_limit_structure_attempt.md
```

Goal:

Investigate whether:

\[
H_N\psi_N=\lambda_N\psi_N
\]

combined with asymptotic compactness implies a meaningful limiting low-energy spectral structure.

---

# 10. Limitation

This worksheet does NOT prove:

- spectral convergence,
- existence of a limiting operator,
- spectral gap persistence,
- or Yang–Mills mass gap results.

It establishes only a global non-escape compactness mechanism.
