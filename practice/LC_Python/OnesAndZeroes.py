from collections import defaultdict
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = defaultdict(int)
        dp[(0, 0)] = 0

        for curr in strs:
            cz = curr.count("0")
            co = len(curr) - cz

            updates = dict()
            for (pz, po), pmax in dp.items():
                nz, no = pz + cz, po + co
                if nz <= m and no <= n:
                    if (nz, no) not in dp or dp[(nz, no)] < pmax + 1:
                        updates[(nz, no)] = pmax + 1

            dp.update(updates)

        return max(dp.values())
