# ============================================================
# Yang–Mills Recursive Operator Scan
# ============================================================
#
# Exploratory numerical spectral investigation
# within the Structural Integrity Recursion (SIR) framework.
#
# This script does NOT solve the Yang–Mills Mass Gap problem.
#
# The purpose is investigating whether recursively perturbed
# operator systems exhibit:
#
# - bounded spectral evolution,
# - stable low eigenvalue sectors,
# - recursive stabilization behavior,
# - and exploratory lower spectral organization.
#
# ============================================================

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# Parameters
# ------------------------------------------------------------

N = 40                     # matrix dimension
epsilon_values = np.linspace(0.0, 1.5, 120)

lowest_eigenvalues = []
spectral_gaps = []

# ------------------------------------------------------------
# Base Operator
# ------------------------------------------------------------
#
# Discrete Laplacian-like operator:
#
#     2  -1   0
#    -1   2  -1
#     0  -1   2
#
# ------------------------------------------------------------

base_matrix = (
    2 * np.eye(N)
    - np.eye(N, k=1)
    - np.eye(N, k=-1)
)

# ------------------------------------------------------------
# Recursive Perturbation Function
# ------------------------------------------------------------

def recursive_perturbation(n, epsilon):

    diag = np.zeros(n)

    for i in range(n):

        x = (i + 1) / n

        # Recursive stabilization structure
        diag[i] = (
            epsilon * np.sin(4 * np.pi * x)
            +
            0.25 / (1 + 10 * x**2)
        )

    return np.diag(diag)

# ------------------------------------------------------------
# Spectral Scan
# ------------------------------------------------------------

for eps in epsilon_values:

    H = base_matrix + recursive_perturbation(N, eps)

    eigenvalues = np.linalg.eigvalsh(H)

    eigenvalues = np.sort(eigenvalues)

    lambda0 = eigenvalues[0]
    lambda1 = eigenvalues[1]

    gap = lambda1 - lambda0

    lowest_eigenvalues.append(lambda0)
    spectral_gaps.append(gap)

# ------------------------------------------------------------
# Plot 1
# Lowest Eigenvalue
# ------------------------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(epsilon_values, lowest_eigenvalues)

plt.xlabel("Recursive Perturbation Strength ε")
plt.ylabel("Lowest Eigenvalue λ₀")

plt.title("Recursive Spectral Stability Scan")

plt.grid(True)

plt.tight_layout()

plt.show()

# ------------------------------------------------------------
# Plot 2
# Spectral Gap
# ------------------------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(epsilon_values, spectral_gaps)

plt.xlabel("Recursive Perturbation Strength ε")
plt.ylabel("Spectral Gap λ₁ - λ₀")

plt.title("Exploratory Recursive Spectral Gap Behavior")

plt.grid(True)

plt.tight_layout()

plt.show()

# ------------------------------------------------------------
# Console Output
# ------------------------------------------------------------

print("\n================================================")
print("Recursive Spectral Scan Complete")
print("================================================")

print(f"Minimum λ₀ : {min(lowest_eigenvalues):.6f}")
print(f"Minimum Gap: {min(spectral_gaps):.6f}")

print("================================================")
print("Exploratory numerical investigation only.")
print("No Yang–Mills Mass Gap claim is made.")
print("================================================")
