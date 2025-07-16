# Classical number theory functions for Shor's algorithm
# (GCD, modular exponentiation, etc.)


def gcd(a, b):
    """
    Compute the greatest common divisor (GCD) of a and b using Euclid's algorithm.
    Returns the largest integer that divides both a and b.
    """
    while b != 0:
        a, b = b, a % b
    return a


def modinv(a, m):
    """
    Compute the modular inverse of a modulo m using the extended Euclidean algorithm.
    Returns x such that (a * x) % m == 1, or None if no inverse exists.
    """
    t, new_t = 0, 1
    r, new_r = m, a
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    if r > 1:
        return None  # No inverse exists
    if t < 0:
        t += m
    return t


def modexp(a, b, m):
    """
    Compute (a ** b) % m efficiently using exponentiation by squaring.
    Useful for large exponents in modular arithmetic.
    """
    result = 1
    a = a % m
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m
        a = (a * a) % m
        b //= 2
    return result


def is_prime(n):
    """
    Simple primality check for small numbers.
    Returns True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True 