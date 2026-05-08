# numerics/tig_ground_state_scan.py

import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh_tridiagonal

# ------------------------------------------------------------
# TIG Ground State Eigenvalue Scan
# ------------------------------------------------------------
# Solves:
#
#   -u''(x) + V_rec(x,beta) u(x) = omega^2 u(x)
#
# with:
#
#   V_rec(x,beta) = -alpha/x^2 + lambda_*(beta-beta_c)^2
#
# Goal:
#   Track the lowest eigenvalue omega_0^2 as beta approaches beta_c.
# ------------------------------------------------------------


def beta_critical():
    return (4.0 / 27.0) ** (1.0 / 3.0)


def recursive_potential(x, beta, alpha=0.10, lambda_=1.0):
    beta_c = beta_critical()
    return -alpha / (x ** 2) + lambda_ * (beta - beta_c) ** 2


def build_operator(x, beta, alpha=0.10, lambda_=1.0):
    dx = x[1] - x[0]
    n = len(x)

    V = recursive_potential(x, beta, alpha, lambda_)

    diagonal = 2.0 / dx**2 + V
    off_diagonal = -1.0 / dx**2 * np.ones(n - 1)

    return diagonal, off_diagonal


def lowest_eigenvalue(beta, x, alpha=0.10, lambda_=1.0):
    diagonal, off_diagonal = build_operator(x, beta, alpha, lambda_)

    eigenvalues = eigh_tridiagonal(
        diagonal,
        off_diagonal,
        select="i",
        select_range=(0, 0)
    )[0]

    omega2_0 = eigenvalues[0]

    if omega2_0 > 0:
        omega_0 = np.sqrt(omega2_0)
    else:
        omega_0 = -np.sqrt(abs(omega2_0))

    return omega2_0, omega_0


def run_scan():
    beta_c = beta_critical()

    # Numerical domain
    x_min = 0.05
    x_max = 40.0
    n_points = 2000

    x = np.linspace(x_min, x_max, n_points)

    # Model parameters
    alpha = 0.10      # Hardy-stable test sector: alpha < 1/4
    lambda_ = 1.0

    # Beta scan around beta_c
    beta_values = np.linspace(beta_c - 0.25, beta_c + 0.25, 200)

    omega2_values = []
    omega_values = []

    for beta in beta_values:
        omega2_0, omega_0 = lowest_eigenvalue(
            beta,
            x,
            alpha=alpha,
            lambda_=lambda_
        )
        omega2_values.append(omega2_0)
        omega_values.append(omega_0)

    omega2_values = np.array(omega2_values)
    omega_values = np.array(omega_values)

    print("TIG Ground State Eigenvalue Scan")
    print("--------------------------------")
    print(f"beta_c  = {beta_c:.8f}")
    print(f"alpha   = {alpha}")
    print(f"lambda  = {lambda_}")
    print(f"min omega_0^2 = {omega2_values.min():.8e}")
    print(f"max omega_0^2 = {omega2_values.max():.8e}")

    if omega2_values.min() > 0:
        print("Result: positive lower spectral sector detected in scan.")
    elif omega2_values.max() > 0:
        print("Result: mixed sector detected; possible gap closing or instability.")
    else:
        print("Result: no positive lower sector detected in this parameter scan.")

    # Plot omega_0^2
    plt.figure(figsize=(8, 5))
    plt.plot(beta_values, omega2_values, label=r"$\omega_0^2(\beta)$")
    plt.axvline(beta_c, linestyle="--", label=r"$\beta_c$")
    plt.axhline(0.0, linestyle=":")
    plt.xlabel(r"$\beta$")
    plt.ylabel(r"$\omega_0^2$")
    plt.title("TIG Ground State Eigenvalue Scan")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Plot omega_0 signed
    plt.figure(figsize=(8, 5))
    plt.plot(beta_values, omega_values, label=r"signed $\omega_0(\beta)$")
    plt.axvline(beta_c, linestyle="--", label=r"$\beta_c$")
    plt.axhline(0.0, linestyle=":")
    plt.xlabel(r"$\beta$")
    plt.ylabel(r"$\omega_0$")
    plt.title("TIG Signed Ground State Frequency")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    run_scan()
