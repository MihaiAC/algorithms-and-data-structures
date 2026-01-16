from typing import List, Set

MODN = 10**9 + 7


class Solution:
    def maximizeSquareArea(
        self, m: int, n: int, hFences: List[int], vFences: List[int]
    ) -> int:
        def get_dists(fences: List[int], border: int) -> Set[int]:
            fences += [1, border]
            fences.sort()

            dists = set()
            for ii in range(len(fences)):
                for jj in range(ii + 1, len(fences)):
                    dists.add(fences[jj] - fences[ii])

            return dists

        dists = get_dists(hFences, m).intersection(get_dists(vFences, n))
        max_dist = max(dists, default=0)
        return -1 if max_dist == 0 else (max_dist**2) % MODN
