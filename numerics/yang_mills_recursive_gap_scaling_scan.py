# numerics/yang_mills_recursive_gap_scaling_scan.py

import numpy as np

# ------------------------------------------------------------
# Yang–Mills Recursive Gap Scaling Scan
# ------------------------------------------------------------
# Exploratory SIR numerical test.
#
# Tests:
# 1. N-scaling
# 2. minimum stabilization threshold mu_min
# 3. robustness of positive low spectral sector
#
# No Yang–Mills Mass Gap proof is claimed.
# ------------------------------------------------------------


def base_operator(N):
    return (
        2 * np.eye(N)
        - np.eye(N, k=1)
        - np.eye(N, k=-1)
    )


def recursive_perturbation(N, epsilon):
    diag = np.zeros(N)

    for i in range(N):
        x = (i + 1) / N
        diag[i] = (
            epsilon * np.sin(4 * np.pi * x)
            + 0.25 / (1 + 10 * x**2)
        )

    return np.diag(diag)


def spectral_values(N, epsilon, mu):
    H = (
        base_operator(N)
        + recursive_perturbation(N, epsilon)
        + mu * np.eye(N)
    )

    eigenvalues = np.linalg.eigvalsh(H)
    eigenvalues = np.sort(eigenvalues)

    lambda0 = eigenvalues[0]
    gap = eigenvalues[1] - eigenvalues[0]

    return lambda0, gap


def scan_for_N(N, epsilon_max=1.5, mu=1.25, steps=120):
    eps_values = np.linspace(0.0, epsilon_max, steps)

    lambda0_values = []
    gap_values = []

    for eps in eps_values:
        lambda0, gap = spectral_values(N, eps, mu)
        lambda0_values.append(lambda0)
        gap_values.append(gap)

    return min(lambda0_values), min(gap_values)


def find_mu_threshold(N, epsilon_max=1.5, steps_eps=80, mu_max=3.0, steps_mu=120):
    mu_values = np.linspace(0.0, mu_max, steps_mu)

    for mu in mu_values:
        min_lambda0, min_gap = scan_for_N(
            N=N,
            epsilon_max=epsilon_max,
            mu=mu,
            steps=steps_eps
        )

        if min_lambda0 > 0 and min_gap > 0:
            return mu, min_lambda0, min_gap

    return None, None, None


def run_scaling_scan():
    N_values = [20, 40, 80, 160, 320]
    epsilon_ranges = [1.5, 2.0, 5.0]

    print("\n================================================")
    print("Yang–Mills Recursive Gap Scaling Scan")
    print("================================================")
    print("Exploratory numerical investigation only.")
    print("No Yang–Mills Mass Gap proof is claimed.")
    print("================================================\n")

    for epsilon_max in epsilon_ranges:
        print(f"\n--- Epsilon Range: [0, {epsilon_max}] ---")

        for N in N_values:
            mu_min, min_lambda0, min_gap = find_mu_threshold(
                N=N,
                epsilon_max=epsilon_max
            )

            if mu_min is None:
                print(
                    f"N={N:4d} | no stable μ found up to scan limit"
                )
            else:
                print(
                    f"N={N:4d} | "
                    f"μ_min≈{mu_min:.4f} | "
                    f"min λ₀≈{min_lambda0:.6f} | "
                    f"min gap≈{min_gap:.6f}"
                )

    print("\n================================================")
    print("Scaling scan complete.")
    print("Interpretation:")
    print("- Stable μ_min across increasing N supports robustness.")
    print("- Growing μ_min may indicate finite-size or instability effects.")
    print("- Vanishing gap as N increases weakens the gap candidate.")
    print("================================================\n")


if __name__ == "__main__":
    run_scaling_scan()
