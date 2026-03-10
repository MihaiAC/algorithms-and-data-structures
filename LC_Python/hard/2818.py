from typing import List, Callable

MAX_NUM = 10**5 + 1
MODN = 10**9 + 7
num_primes = [0] * (MAX_NUM)

for num in range(2, MAX_NUM, 2):
    num_primes[num] += 1

for num in range(3, MAX_NUM, 2):
    if num_primes[num] == 0:
        for curr in range(num, MAX_NUM, num):
            num_primes[curr] += 1


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        N = len(nums)

        def build_accum(
            idx_range: List[int], compare: Callable[[int, int], bool]
        ) -> List[int]:
            ls = [0] * N
            stack = [(0, 0)]

            for idx in idx_range:
                num_factors = num_primes[nums[idx]]
                accum = 1
                while stack and compare(num_factors, stack[-1][0]):
                    _, count = stack.pop()
                    accum += count
                ls[idx] = accum - 1
                stack.append((num_factors, accum))

            return ls

        suffixes = build_accum(range(N - 1, -1, -1), lambda x, y: x >= y)
        prefixes = build_accum(range(N), lambda x, y: x > y)

        sorted_nums = sorted(zip(nums, range(N)), key=lambda x: x[0])

        ans = 1
        while k > 0:
            num, idx = sorted_nums.pop()
            num_intervals = (
                1 + prefixes[idx] + suffixes[idx] + prefixes[idx] * suffixes[idx]
            )
            ans = ans * pow(num, min(k, num_intervals), MODN) % MODN
            k -= num_intervals

        return ans
