from typing import List
from collections import defaultdict


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        rows = defaultdict(list)
        cols = defaultdict(list)

        for idx, (x, y) in enumerate(buildings):
            cols[x].append((y, idx))
            rows[y].append((x, idx))

        row_covered = set()
        for row in rows.values():
            row.sort()
            for _, idx in row[1:-1]:
                row_covered.add(idx)

        ans = 0
        for col in cols.values():
            col.sort()
            for _, idx in col[1:-1]:
                if idx in row_covered:
                    ans += 1

        return ans
