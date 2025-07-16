# Quantum circuit logic for Shor's algorithm
# (Order finding, QFT, etc.)

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.circuit.library import QFT, UnitaryGate
import numpy as np
from shor.utils import get_order_from_phase
from shor.classical import gcd


def modular_exponentiation_gate(a, N, n):
    """
    Create a modular exponentiation gate for small N using a unitary matrix.
    Only practical for small N (e.g., N <= 15).
    Ensures a is coprime to N and the mapping is a permutation (unitary).
    """
    if gcd(a, N) != 1:
        raise ValueError(f"a={a} is not coprime to N={N}, cannot build unitary modular exponentiation gate.")
    dim = 2 ** n
    outputs = set()
    U = np.zeros((dim, dim))
    for x in range(dim):
        y = pow(a, x, N)
        if y in outputs:
            raise ValueError(f"Mapping is not a permutation for a={a}, N={N}, n={n}.")
        outputs.add(y)
        U[y, x] = 1
    return UnitaryGate(U, label=f"ModExp_{a}^{N}")


def quantum_order_finding(a, N, n_count=4):
    """
    Find the order r of a modulo N using a quantum circuit with a real modular exponentiation gate for small N.
    Falls back to classical brute-force if the gate cannot be constructed.
    """
    # For very small N, fallback to classical brute-force
    if N < 8:
        r = 1
        while pow(a, r, N) != 1 and r < N:
            r += 1
        if r == N:
            return None
        return r

    n = int(np.ceil(np.log2(N)))
    qc = QuantumCircuit(n_count + n, n_count)
    qc.x(n_count + n - 1)  # Initialize result register to |1>
    qc.h(range(n_count))   # Hadamard on counting qubits

    # Try to build and apply the modular exponentiation gate
    try:
        modexp_gate = modular_exponentiation_gate(a, N, n)
        for q in range(n_count):
            controlled_modexp = modexp_gate.control(1)
            qc.append(controlled_modexp, [q] + list(range(n_count, n_count + n)))
    except ValueError as e:
        print(f"[Warning] {e} Falling back to classical brute-force for order finding.")
        r = 1
        while pow(a, r, N) != 1 and r < N:
            r += 1
        if r == N:
            return None
        return r

    qc.append(QFT(num_qubits=n_count, inverse=True, do_swaps=True), range(n_count))
    qc.measure(range(n_count), range(n_count))

    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator)
    result = simulator.run(compiled_circuit, shots=1).result()
    counts = result.get_counts()
    measured = max(counts, key=counts.get)
    phase = int(measured, 2) / (2 ** n_count)

    r = get_order_from_phase(phase, N)
    return r

# Note: This implementation is only practical for small N (e.g., N <= 15) due to the exponential size of the unitary matrix.
# For larger N, a more efficient modular exponentiation circuit is required. 