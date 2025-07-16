# Shared helper functions for Shor's algorithm


def continued_fraction(x, max_denominator=1000):
    """
    Compute the best rational approximation of x with denominator <= max_denominator
    using continued fractions. Returns (numerator, denominator).
    Useful for extracting the order from the measured quantum phase.
    """
    from fractions import Fraction
    frac = Fraction(x).limit_denominator(max_denominator)
    return frac.numerator, frac.denominator


def get_order_from_phase(phase, N, max_denominator=1000):
    """
    Given a measured phase (as a float in [0, 1)),
    use continued fractions to estimate the order r such that phase ≈ s/r.
    Returns the denominator r if it is a valid order, else None.
    """
    num, denom = continued_fraction(phase, max_denominator)
    if denom >= 2 and pow(int(round(phase * denom)), denom, N) == 1:
        return denom
    return None 