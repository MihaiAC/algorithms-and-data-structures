from typing import List
from collections import defaultdict

layouts = [[2, 3, 4, 5], [6, 7, 8, 9], [4, 5, 6, 7]]


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = defaultdict(list)
        for row, seat in reservedSeats:
            reserved[row].append(seat)

        ans = 0
        for row in reserved:
            if row not in reserved:
                ans += 2
                continue

            dx = 0
            curr_row = reserved[row]
            for layout in layouts:
                if layout[0] == 4 and dx > 0:
                    break

                occupied = False
                for seat in layout:
                    if seat in curr_row:
                        occupied = True
                        break
                if not occupied:
                    dx += 1

            ans += dx

        return ans + 2 * (n - len(reserved))


sol = Solution()
print(sol.maxNumberOfFamilies(3, [[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]]))
print(sol.maxNumberOfFamilies(2, [[2, 1], [1, 8], [2, 6]]))
print(sol.maxNumberOfFamilies(4, [[4, 3], [1, 4], [4, 6], [1, 7]]))
