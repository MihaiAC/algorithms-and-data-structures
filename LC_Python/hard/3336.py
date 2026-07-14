from typing import List
from math import gcd

MODN = 10**9 + 7


class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        M = max(nums)

        dp = [[0] * (M + 1) for _ in range(M + 1)]
        dp[0][0] = 1

        for num in nums:
            next_dp = [[0] * (M + 1) for _ in range(M + 1)]
            for left_gcd in range(M + 1):
                _left_gcd = gcd(left_gcd, num)
                for right_gcd in range(M + 1):
                    curr = dp[left_gcd][right_gcd]

                    next_dp[left_gcd][right_gcd] = (
                        next_dp[left_gcd][right_gcd] + curr
                    ) % MODN

                    next_dp[_left_gcd][right_gcd] = (
                        next_dp[_left_gcd][right_gcd] + curr
                    ) % MODN

                    _right_gcd = gcd(right_gcd, num)
                    next_dp[left_gcd][_right_gcd] = (
                        next_dp[left_gcd][_right_gcd] + curr
                    ) % MODN

            dp = next_dp

        ans = 0
        for common_gcd in range(1, M + 1):
            ans = (ans + dp[common_gcd][common_gcd]) % MODN

        return ans


sol = Solution()
print(sol.subsequencePairCount([1, 2, 3, 4]))
print(sol.subsequencePairCount([10, 20, 30]))
print(sol.subsequencePairCount([1, 1, 1, 1]))
