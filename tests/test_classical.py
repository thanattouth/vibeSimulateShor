# Tests for classical number theory functions in Shor's algorithm

import unittest
from shor.classical import gcd, modinv, modexp, is_prime

class TestClassical(unittest.TestCase):
    def test_gcd(self):
        # Test GCD of two numbers
        self.assertEqual(gcd(54, 24), 6)
        self.assertEqual(gcd(17, 13), 1)
        self.assertEqual(gcd(100, 10), 10)

    def test_modinv(self):
        # Test modular inverse
        self.assertEqual(modinv(3, 11), 4)  # 3*4 % 11 == 1
        self.assertIsNone(modinv(2, 4))     # No inverse exists

    def test_modexp(self):
        # Test modular exponentiation
        self.assertEqual(modexp(2, 10, 1000), 24)  # 2^10 % 1000 = 1024 % 1000 = 24
        self.assertEqual(modexp(3, 0, 7), 1)       # 3^0 % 7 = 1

    def test_is_prime(self):
        # Test primality check
        self.assertTrue(is_prime(13))
        self.assertFalse(is_prime(15))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))

if __name__ == "__main__":
    unittest.main() 