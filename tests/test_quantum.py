# Tests for quantum circuit logic in Shor's algorithm

import unittest
from shor.quantum import quantum_order_finding

class TestQuantum(unittest.TestCase):
    def test_quantum_order_finding_classical(self):
        # For small N, the function uses classical brute-force
        # For a=2, N=15, the order r is 4 (since 2^4 % 15 == 1)
        r = quantum_order_finding(2, 15)
        self.assertEqual(r, 4)

if __name__ == "__main__":
    unittest.main() 