from typing import List
from collections import defaultdict

MODN = 10**9 + 7


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        y_count = defaultdict(int)

        for x, y in points:
            y_count[y] += 1

        ans = 0
        sum_so_far = 0
        for y in y_count:
            count = y_count[y]
            curr = count * (count - 1) // 2

            if sum_so_far != 0:
                ans = (ans + curr * sum_so_far) % MODN

            sum_so_far += curr

        return ans
