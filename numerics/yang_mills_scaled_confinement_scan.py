# ============================================================
# Yang–Mills Scaled Confinement Scan
# ============================================================
#
# Exploratory numerical investigation within the
# Structural Integrity Recursion (SIR) framework.
#
# Objective:
#
# Investigate whether continuum-scaled recursive
# confinement structures preserve:
#
#     λ₁ - λ₀ > 0
#
# under increasing operator dimension.
#
# This script does NOT solve the Yang–Mills Mass Gap problem.
#
# ============================================================

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# Parameters
# ------------------------------------------------------------

N_values = [20, 40, 80, 160, 320]

epsilon_max = 2.0

mu = 1.25

kappa = 12.0

epsilon_values = np.linspace(0.0, epsilon_max, 120)

# ------------------------------------------------------------
# Continuum-Scaled Laplacian
# ------------------------------------------------------------

def base_operator(N):

    dx = 1.0 / (N + 1)

    return (
        (
            2 * np.eye(N)
            - np.eye(N, k=1)
            - np.eye(N, k=-1)
        ) / dx**2
    )

# ------------------------------------------------------------
# Recursive Perturbation
# ------------------------------------------------------------

def recursive_perturbation(N, epsilon):

    diag = np.zeros(N)

    for i in range(N):

        x = (i + 1) / N

        diag[i] = (
            epsilon * np.sin(4 * np.pi * x)
            +
            0.25 / (1 + 10 * x**2)
        )

    return np.diag(diag)

# ------------------------------------------------------------
# Confinement Potential
# ------------------------------------------------------------

def confinement_potential(N, kappa):

    diag = np.zeros(N)

    for i in range(N):

        x = (i + 1) / N

        diag[i] = (
            kappa * (x - 0.5)**2
        )

    return np.diag(diag)

# ------------------------------------------------------------
# Spectral Scan
# ------------------------------------------------------------

results = []

for N in N_values:

    lambda0_values = []

    gap_values = []

    for eps in epsilon_values:

        H = (
            base_operator(N)
            + recursive_perturbation(N, eps)
            + confinement_potential(N, kappa)
            + mu * np.eye(N)
        )

        eigenvalues = np.linalg.eigvalsh(H)

        eigenvalues = np.sort(eigenvalues)

        lambda0 = eigenvalues[0]

        lambda1 = eigenvalues[1]

        gap = lambda1 - lambda0

        lambda0_values.append(lambda0)

        gap_values.append(gap)

    min_lambda0 = min(lambda0_values)

    min_gap = min(gap_values)

    results.append((N, min_lambda0, min_gap))

# ------------------------------------------------------------
# Console Output
# ------------------------------------------------------------

print("\n================================================")
print("Scaled Recursive Confinement Scan")
print("================================================")

print(f"Stabilization parameter μ = {mu}")
print(f"Confinement parameter κ  = {kappa}")

print("================================================\n")

for N, min_lambda0, min_gap in results:

    print(
        f"N={N:4d} | "
        f"min λ₀ = {min_lambda0:.6f} | "
        f"min gap = {min_gap:.6f}"
    )

print("\n================================================")
print("Exploratory numerical investigation only.")
print("No Yang–Mills Mass Gap proof is made.")
print("================================================")

# ------------------------------------------------------------
# Plot
# ------------------------------------------------------------

N_plot = [r[0] for r in results]

gap_plot = [r[2] for r in results]

plt.figure(figsize=(8,5))

plt.plot(N_plot, gap_plot, marker='o')

plt.xlabel("Operator Dimension N")

plt.ylabel("Minimum Spectral Gap")

plt.title("Scaled Recursive Confinement Gap Scaling")

plt.grid(True)

plt.tight_layout()

plt.show()
