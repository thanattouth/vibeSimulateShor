# Main entry point for custom Shor's algorithm simulation
# This script will tie together the classical and quantum parts.

import random
import os
from shor.classical import gcd, is_prime
from shor.quantum import quantum_order_finding


def shor_factor(N, show_circuit=False, show_histogram=False, save_circuit=False, save_histogram=False, circuit_filename=None, histogram_filename=None):
    """
    Attempt to factor N using Shor's algorithm.
    Returns a tuple of non-trivial factors or None if unsuccessful.
    Passes visualization options to quantum_order_finding.
    """
    if N % 2 == 0:
        return 2, N // 2
    if is_prime(N):
        print(f"{N} is prime!")
        return None

    for attempt in range(5):  # Try a few random values
        a = random.randrange(2, N)
        print(f"\nAttempt {attempt+1}: Trying a = {a}")
        d = gcd(a, N)
        if d > 1:
            print(f"Found a non-trivial factor by GCD: {d}")
            return d, N // d
        # Pass visualization options for small/medium N
        if N <= 60:
            # Ensure images folder exists if saving images
            if save_circuit or save_histogram:
                os.makedirs('images', exist_ok=True)
            # Set default filenames in images/ if not provided
            if save_circuit and not circuit_filename:
                circuit_filename = f"images/circuit_N{N}_a{a}.png"
            if save_histogram and not histogram_filename:
                histogram_filename = f"images/histogram_N{N}_a{a}.png"
            r = quantum_order_finding(
                a, N,
                show_circuit=show_circuit,
                show_histogram=show_histogram,
                save_circuit=save_circuit,
                save_histogram=save_histogram,
                circuit_filename=circuit_filename,
                histogram_filename=histogram_filename
            )
        else:
            r = quantum_order_finding(a, N)
        print(f"Order r found: {r}")
        if r is None or r % 2 != 0:
            print("Order not found or not even, retrying...")
            continue
        x = pow(a, r // 2, N)
        if x == N - 1 or x == 1:
            print("Trivial root found, retrying...")
            continue
        factor1 = gcd(x + 1, N)
        factor2 = gcd(x - 1, N)
        if 1 < factor1 < N:
            return factor1, N // factor1
        if 1 < factor2 < N:
            return factor2, N // factor2
    return None


def main():
    """
    Main workflow for Shor's algorithm simulation.
    Prompts user for N, runs the algorithm, and prints the result.
    Offers visualization and save options for quantum runs.
    """
    print("Custom Shor's Algorithm Simulation (not using qiskit.algorithms.Shor)")
    try:
        N = int(input("Enter a composite number to factor (default 15): ") or 15)
    except ValueError:
        print("Invalid input. Using default N = 15.")
        N = 15

    show_circuit = False
    show_histogram = False
    save_circuit = False
    save_histogram = False
    circuit_filename = None
    histogram_filename = None
    if N <= 60:
        ans = input("Show quantum circuit diagram? (y/N): ").strip().lower()
        show_circuit = (ans == 'y')
        ans = input("Show measurement histogram? (y/N): ").strip().lower()
        show_histogram = (ans == 'y')
        ans = input("Save quantum circuit diagram as image? (y/N): ").strip().lower()
        save_circuit = (ans == 'y')
        if save_circuit:
            circuit_filename = input("Enter filename for circuit image (or press Enter for default): ").strip() or None
        ans = input("Save measurement histogram as image? (y/N): ").strip().lower()
        save_histogram = (ans == 'y')
        if save_histogram:
            histogram_filename = input("Enter filename for histogram image (or press Enter for default): ").strip() or None

    result = shor_factor(
        N,
        show_circuit=show_circuit,
        show_histogram=show_histogram,
        save_circuit=save_circuit,
        save_histogram=save_histogram,
        circuit_filename=circuit_filename,
        histogram_filename=histogram_filename
    )
    if result:
        print(f"\nNon-trivial factors of {N}: {result[0]} x {result[1]} = {N}")
    else:
        print(f"\nFailed to find non-trivial factors for {N}.")


if __name__ == "__main__":
    main() 