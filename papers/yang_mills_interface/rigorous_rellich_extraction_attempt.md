# Rigorous Rellich Extraction Attempt

## Purpose

This worksheet investigates whether bounded local \(H^1\)-control implies strong local compactness extraction for low-energy states in the simplified continuum operator setting.

The objective is not proving the Yang–Mills Mass Gap problem.

Instead, the purpose is establishing the next compactness step after the local \(H^1\)-bound estimate.

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

# 2. Previously Established Local H1 Bound

Previous analysis yielded:

\[
\|\psi_N\|_{H^1(K)}
\le C_K
\]

for every compact:

\[
K\subset\mathbb R^d
\]

uniformly in \(N\).

---

# 3. Rellich-Type Compactness Input

For bounded domains:

\[
K\subset\mathbb R^d
\]

Rellich–Kondrachov compactness heuristics suggest:

\[
H^1(K)
\hookrightarrow
L^2(K)
\]

compactly.

---

# 4. Compactness Extraction

Since:

\[
\{\psi_N\}
\]

is bounded in:

\[
H^1(K)
\]

there exists a subsequence:

\[
\psi_{N_k}
\]

and limit state:

\[
\psi_\infty
\]

such that:

\[
\psi_{N_k}
\rightarrow
\psi_\infty
\]

strongly in:

\[
L^2(K)
\]

for compact \(K\).

---

# 5. Local Strong Convergence

Since the compact region \(K\) was arbitrary, heuristically:

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

# 6. Proto-Rellich Extraction Lemma

If:

1. \(\|\psi_N\|_{L^2}=1\),
2. \(\langle \psi_N,H_N\psi_N\rangle\le E\),
3. and \(V_N\ge -C_0\) uniformly,

then bounded local \(H^1\)-control yields subsequences satisfying:

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

# 7. Structural Meaning

This is the first genuine compactness mechanism in the program.

The chain now becomes:

```text
bounded energy
        ↓
global gradient control
        ↓
local H¹-bounds
        ↓
Rellich compactness
        ↓
strong local convergence
```

---

# 8. Remaining Problem

Strong local convergence alone does NOT prevent global mass escape.

Mass may still disappear toward spatial infinity.

Therefore the next required step is combining:

```text
strong local convergence
+
tightness
```

to obtain:

```text
global mass persistence
```

---

# 9. Next Step

The next worksheet must therefore be:

```text
rigorous_global_mass_persistence_attempt.md
```

Goal:

Show that tightness prevents loss of total \(L^2\)-mass and forces:

\[
\psi_\infty\neq0
\]

potentially even:

\[
\|\psi_\infty\|_{L^2}=1
\]

---

# 10. Limitation

This worksheet does NOT prove:

- global compactness,
- spectral convergence,
- gap persistence,
- or Yang–Mills mass gap results.

It establishes only a local compactness extraction mechanism.
