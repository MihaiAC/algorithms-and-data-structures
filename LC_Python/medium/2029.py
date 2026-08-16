from typing import List


class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        count = [0, 0, 0]
        for stone in stones:
            count[stone % 3] += 1

        if count[0] % 2 == 0:
            return count[1] >= 1 and count[2] >= 1
        return count[1] > count[2] + 2 or count[2] > count[1] + 2


sol = Solution()
print(sol.stoneGameIX([2, 1]))
print(sol.stoneGameIX([2]))
print(sol.stoneGameIX([5, 1, 2, 4, 3]))
print(sol.stoneGameIX([3, 6, 9]))
