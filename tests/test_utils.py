# Tests for shared helper functions in Shor's algorithm

import unittest
from shor.utils import continued_fraction, get_order_from_phase

class TestUtils(unittest.TestCase):
    def test_continued_fraction(self):
        # Test rational approximation
        num, denom = continued_fraction(0.333333, 100)
        self.assertEqual((num, denom), (1, 3))
        num, denom = continued_fraction(0.5, 100)
        self.assertEqual((num, denom), (1, 2))
        num, denom = continued_fraction(0.142857, 100)
        self.assertEqual((num, denom), (1, 7))

    def test_get_order_from_phase(self):
        # For phase = 0.25 and N = 15, denominator should be 4
        r = get_order_from_phase(0.25, 15, 10)
        self.assertEqual(r, 4)
        # For phase = 0.5 and N = 15, denominator should be 2
        r = get_order_from_phase(0.5, 15, 10)
        self.assertEqual(r, 2)
        # For phase = 0.1 and N = 15, denominator should be None (not a valid order)
        r = get_order_from_phase(0.1, 15, 10)
        self.assertEqual(r, 10)

if __name__ == "__main__":
    unittest.main() 