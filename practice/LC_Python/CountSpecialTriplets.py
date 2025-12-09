from typing import List
from collections import defaultdict

MODN = 10**9 + 7


class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        left = defaultdict(int)
        right = defaultdict(int)

        for num in nums:
            right[num] += 1

        ans = 0
        for num in nums:
            right[num] -= 1
            ans = (ans + left[2 * num] * right[2 * num]) % MODN
            left[num] += 1

        return ans
