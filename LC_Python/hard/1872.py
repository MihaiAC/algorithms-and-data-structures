from typing import List


class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        accum = [0]
        for stone in stones:
            accum.append(accum[-1] + stone)

        N = len(stones)
        max_possible = [0] * N
        max_possible[-1] = accum[-1]
        for idx in range(N - 2, -1, -1):
            max_possible[idx] = max(
                max_possible[idx + 1], accum[idx + 1] - max_possible[idx + 1]
            )

        return max_possible[1]


sol = Solution()
print(sol.stoneGameVIII([-1, 2, -3, 4, -5]))
print(sol.stoneGameVIII([7, -6, 5, 10, 5, -2, -6]))
print(sol.stoneGameVIII([-10, -12]))
