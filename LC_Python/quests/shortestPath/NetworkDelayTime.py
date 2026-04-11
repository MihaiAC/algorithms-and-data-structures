from typing import List
from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        if n == 1:
            return 0

        neighbors = defaultdict(list)
        for u, v, time in times:
            neighbors[u].append((v, time))

        visited = set()
        heap = [(0, k)]

        while len(heap) > 0:
            curr_time, node = heappop(heap)

            if node in visited:
                continue

            visited.add(node)
            if len(visited) == n:
                return curr_time

            for neighbor, time in neighbors[node]:
                if neighbor not in visited:
                    heappush(heap, (curr_time + time, neighbor))

        return -1


sol = Solution()
print(sol.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
print(sol.networkDelayTime([[1, 2, 1]], 2, 1))
print(sol.networkDelayTime([[1, 2, 1]], 2, 2))
