from typing import List
from itertools import accumulate
from bisect import bisect_right


class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_num = max(nums)

        count = [0] * (max_num + 1)
        for num in nums:
            count[num] += 1

        gcd_count = [0] * (max_num + 1)
        for num in range(max_num, 0, -1):
            multiples_count = sum(count[num::num])
            gcd_count[num] = multiples_count * (multiples_count - 1) // 2 - sum(
                gcd_count[num::num]
            )

        accum_gcd = list(accumulate(gcd_count))
        return [bisect_right(accum_gcd, query) for query in queries]


sol = Solution()
print(sol.gcdValues([2, 3, 4], [0, 2, 2]))
print(sol.gcdValues([4, 4, 2, 1], [5, 3, 1, 0]))
print(sol.gcdValues([2, 2], [0, 0]))
