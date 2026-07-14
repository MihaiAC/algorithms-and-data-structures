from typing import List
from math import gcd

MODN = 10**9 + 7


class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        N = len(nums)
        M = max(nums)

        dp = [[[0] * (M + 1) for _ in range(M + 1)] for _ in range(N + 1)]
        dp[0][0][0] = 1

        for idx in range(N):
            for left_gcd in range(M + 1):
                for right_gcd in range(M + 1):
                    dp[idx + 1][left_gcd][right_gcd] = (
                        dp[idx + 1][left_gcd][right_gcd] + dp[idx][left_gcd][right_gcd]
                    ) % MODN

                    _left_gcd = gcd(left_gcd, nums[idx])
                    dp[idx + 1][_left_gcd][right_gcd] = (
                        dp[idx + 1][_left_gcd][right_gcd] + dp[idx][left_gcd][right_gcd]
                    ) % MODN

                    _right_gcd = gcd(right_gcd, nums[idx])
                    dp[idx + 1][left_gcd][_right_gcd] = (
                        dp[idx + 1][left_gcd][_right_gcd] + dp[idx][left_gcd][right_gcd]
                    ) % MODN
        ans = 0
        for common_gcd in range(1, M + 1):
            ans = (ans + dp[N][common_gcd][common_gcd]) % MODN

        return ans


sol = Solution()
print(sol.subsequencePairCount([1, 2, 3, 4]))
print(sol.subsequencePairCount([10, 20, 30]))
print(sol.subsequencePairCount([1, 1, 1, 1]))
