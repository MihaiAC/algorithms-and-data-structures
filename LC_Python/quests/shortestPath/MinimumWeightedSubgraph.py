from typing import List, Dict
from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def minimumWeight(
        self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int
    ) -> int:
        forward = defaultdict(list)
        backward = defaultdict(list)

        for u, v, w in edges:
            forward[u].append((w, v))
            backward[v].append((w, u))

        def min_dist(graph: Dict[int, List[int]], source: int) -> int:
            dists = [float("inf")] * n
            heap = [(0, source)]

            while len(heap) > 0:
                curr_time, node = heappop(heap)
                if dists[node] == float("inf"):
                    dists[node] = curr_time
                    for time, nxt in graph[node]:
                        heappush(heap, (curr_time + time, nxt))
            return dists

        d1 = min_dist(forward, src1)
        d2 = min_dist(forward, src2)
        dd = min_dist(backward, dest)

        ans = float("inf")
        for x in range(n):
            ans = min(ans, d1[x] + d2[x] + dd[x])

        return ans if ans != float("inf") else -1


sol = Solution()
print(
    sol.minimumWeight(
        6,
        [
            [0, 2, 2],
            [0, 5, 6],
            [1, 0, 3],
            [1, 4, 5],
            [2, 1, 1],
            [2, 3, 3],
            [2, 3, 4],
            [3, 4, 2],
            [4, 5, 1],
        ],
        0,
        1,
        5,
    )
)
