from typing import List
from collections import defaultdict


class Solution:
    def maximalPathQuality(
        self, values: List[int], edges: List[List[int]], maxTime: int
    ) -> int:
        neighbors = defaultdict(list)
        for u, v, time in edges:
            neighbors[u].append((time, v))
            neighbors[v].append((time, u))

        ans = 0
        visited = defaultdict(int)
        visited[0] = 1

        def dfs(curr_node: int, curr_time: int):
            if curr_node == 0:
                nonlocal ans
                ans = max(ans, sum([values[x] for x in visited if visited[x] > 0]))

            for time, node in neighbors[curr_node]:
                if curr_time + time <= maxTime:
                    visited[node] += 1
                    dfs(node, curr_time + time)
                    visited[node] -= 1

        dfs(0, 0)
        return ans


sol = Solution()
print(sol.maximalPathQuality([0, 32, 10, 43], [[0, 1, 10], [1, 2, 15], [0, 3, 10]], 49))
print(sol.maximalPathQuality([5, 10, 15, 20], [[0, 1, 10], [1, 2, 10], [0, 3, 10]], 30))
print(
    sol.maximalPathQuality(
        [1, 2, 3, 4], [[0, 1, 10], [1, 2, 11], [2, 3, 12], [1, 3, 13]], 50
    )
)
