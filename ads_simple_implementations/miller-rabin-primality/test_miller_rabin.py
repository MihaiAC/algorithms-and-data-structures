from miller_rabin import miller_rabin

MAX_N = 10**6
sieve = [True] * (MAX_N + 1)
sieve[0] = False
sieve[1] = False

for even in range(4, MAX_N + 1, 2):
    sieve[even] = False

for p in range(3, MAX_N + 1, 2):
    if sieve[p]:
        for mp in range(2 * p, MAX_N + 1, p):
            sieve[mp] = False


def test_primes():
    for num in range(MAX_N + 1):
        assert sieve[num] == miller_rabin(num), f"Test failed for num={num}"
