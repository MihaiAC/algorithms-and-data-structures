"""
Probabilistically determine if a number is prime or not.

Problem: decide if n is prime or not. n > 2 and n % 2 = 1

Miller-Rabin Primality test:
Write n as d*2^s, s > 0, d > 0, d - odd
Choose "base" integer that is coprime to n (in practice a smaller
prime number).
n is a "strong probable prime" if either of the following relations
holds:
1) a**d = 1 (mod n)
2) base**(d*2**r) = -1 = n-1 (mod n) for some 0 <= r < s

If n is not a strong probable prime, then it is definitely composite.
"base" is a "witness" for the composite nature of n.

Source:
https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
"""

from typing import List


def is_composite(num: int, xpow: int, s: int) -> bool:
    """
    num = input number
    xpow = base**d % num
    s = same s as above

    Returns True if num is composite, False otherwise.
    """
    if xpow == 1 or xpow == num - 1:
        return False

    for _ in range(1, s):
        xpow = pow(xpow, 2, num)

        # Early stop.
        # We know previous xpow was neither 1 nor num-1.
        if xpow == 1:
            return True

        # Found the "r".
        if xpow == num - 1:
            return False

    return True


def miller_rabin(num: int, bases: List[int] = [2, 3, 5, 7]) -> bool:
    """
    num = input number
    bases = list of prime numbers to use as bases

    Returns true if num is a strong probable prime, false otherwise.
    """
    # Trivial checks.
    if num < 2:
        return False

    if num in bases:
        return True

    if num % 2 == 0:
        return False

    d, s = num - 1, 0
    while d % 2 == 0:
        d = d // 2
        s += 1

    for base in bases:
        if base >= num:
            continue

        if is_composite(num, pow(base, d, num), s):
            return False

    return True
