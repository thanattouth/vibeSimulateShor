# Shor's Algorithm Simulation (Custom Implementation)

This project simulates Shor's algorithm for integer factorization using a combination of classical number theory and quantum circuit simulation (via Qiskit). The quantum part is implemented manually—Qiskit's built-in Shor algorithm is NOT used.

## Project Structure
- `main.py` — Entry point to run the simulation
- `shor/` — Core logic
  - `classical.py` — Classical number theory (GCD, modular exponentiation, etc.)
  - `quantum.py` — Quantum circuit logic (order finding, QFT, etc.)
  - `utils.py` — Shared helpers
- `tests/` — Unit tests
- `requirements.txt` — Python dependencies

## Setup
1. (Recommended) Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the simulation:
   ```bash
   python main.py
   ```

## Notes
- This project does NOT use `qiskit.algorithms.Shor`. All logic is implemented manually for educational purposes. 