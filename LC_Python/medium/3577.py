from typing import List

MODN = 10**9 + 7


class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        N = len(complexity)

        for num in complexity[1:]:
            if num <= complexity[0]:
                return 0

        ans = 1
        for num in range(2, N):
            ans = (ans * num) % MODN

        return ans
