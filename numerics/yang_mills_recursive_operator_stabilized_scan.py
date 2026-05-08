# ============================================================
# Yang–Mills Recursive Operator Stabilized Scan
# ============================================================
#
# Exploratory stabilized spectral investigation
# within the Structural Integrity Recursion (SIR) framework.
#
# This script does NOT solve the Yang–Mills Mass Gap problem.
#
# The purpose is investigating whether recursively stabilized
# operator systems may preserve:
#
# - positive low spectral sectors,
# - bounded spectral evolution,
# - recursive stabilization behavior,
# - and persistent spectral separation.
#
# ============================================================

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# Parameters
# ------------------------------------------------------------

N = 40

epsilon_values = np.linspace(0.0, 1.5, 120)

mu = 1.25

lowest_eigenvalues = []
spectral_gaps = []

# ------------------------------------------------------------
# Base Operator
# ------------------------------------------------------------

base_matrix = (
    2 * np.eye(N)
    - np.eye(N, k=1)
    - np.eye(N, k=-1)
)

# ------------------------------------------------------------
# Recursive Perturbation
# ------------------------------------------------------------

def recursive_perturbation(n, epsilon):

    diag = np.zeros(n)

    for i in range(n):

        x = (i + 1) / n

        diag[i] = (
            epsilon * np.sin(4 * np.pi * x)
            +
            0.25 / (1 + 10 * x**2)
        )

    return np.diag(diag)

# ------------------------------------------------------------
# Stabilized Spectral Scan
# ------------------------------------------------------------

for eps in epsilon_values:

    H = (
        base_matrix
        + recursive_perturbation(N, eps)
        + mu * np.eye(N)
    )

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

plt.title("Stabilized Recursive Spectral Scan")

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

plt.title("Stabilized Recursive Spectral Gap Behavior")

plt.grid(True)

plt.tight_layout()

plt.show()

# ------------------------------------------------------------
# Console Output
# ------------------------------------------------------------

min_lambda0 = min(lowest_eigenvalues)
min_gap = min(spectral_gaps)

print("\n================================================")
print("Stabilized Recursive Spectral Scan Complete")
print("================================================")

print(f"Stabilization Parameter μ : {mu:.4f}")
print(f"Minimum λ₀                : {min_lambda0:.6f}")
print(f"Minimum Gap               : {min_gap:.6f}")

print("================================================")

if min_lambda0 > 0 and min_gap > 0:

    print("Stable positive low spectral sector observed.")
    print("Persistent spectral separation maintained.")

else:

    print("Low spectral stabilization incomplete.")

print("================================================")
print("Exploratory numerical investigation only.")
print("No Yang–Mills Mass Gap claim is made.")
print("================================================")
