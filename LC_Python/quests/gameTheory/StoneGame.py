from typing import List
from functools import cache


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        N = len(piles)

        @cache
        def minimax(left: int, right: int, alice: int) -> int:
            if left == right:
                return piles[left]

            if alice == 1:
                return max(
                    piles[left] + minimax(left + 1, right, 0),
                    piles[right] + minimax(left, right - 1, 0),
                )
            return min(minimax(left + 1, right, 1), minimax(left, right - 1, 1))

        aliceMax = minimax(0, N - 1, 1)
        return 2 * aliceMax > sum(piles)


sol = Solution()
print(sol.stoneGame([5, 3, 4, 5]))
print(sol.stoneGame([3, 7, 2, 3]))
