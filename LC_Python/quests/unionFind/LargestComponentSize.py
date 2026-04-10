from typing import List
from collections import defaultdict

MAXN = 10**5

# sieve[x] = p => p is the smallest prime s.t x % p = 0
sieve = list(range(MAXN + 1))

for number in range(2, int(MAXN**0.5) + 1):
    if sieve[number] == number:
        for multiple in range(number * number, MAXN + 1, number):
            if sieve[multiple] == multiple:
                sieve[multiple] = number


def prime_factors(num: int) -> List[int]:
    if sieve[num] == num:
        return [num]

    factors = []
    while num > 1:
        smallest_prime = sieve[num]
        factors.append(smallest_prime)
        while num % smallest_prime == 0:
            num //= smallest_prime

    return factors


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        N = len(nums)
        size = [1] * N
        parent = list(range(N))
        primes_to_indices = defaultdict(list)

        def find(idx: int) -> int:
            if idx == parent[idx]:
                return idx
            parent[idx] = find(parent[idx])
            return parent[idx]

        def union(idx1: int, idx2: int):
            idx1 = find(idx1)
            idx2 = find(idx2)

            if idx1 == idx2:
                return

            if size[idx2] < size[idx1]:
                idx1, idx2 = idx2, idx1

            parent[idx1] = idx2
            size[idx2] += size[idx1]

        for idx, num in enumerate(nums):
            factors = prime_factors(num)
            for factor in factors:
                primes_to_indices[factor].append(idx)

        for indices in primes_to_indices.values():
            if len(indices) > 1:
                for index in indices[1:]:
                    union(indices[0], index)

        return max(size)


sol = Solution()
print(sol.largestComponentSize([4, 6, 15, 35]))
print(sol.largestComponentSize([20, 50, 9, 63]))
print(sol.largestComponentSize([2, 3, 6, 7, 4, 12, 21, 39]))
