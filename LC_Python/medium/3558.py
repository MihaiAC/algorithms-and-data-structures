from typing import List
from collections import defaultdict, deque

MODN = 10**9 + 7


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        N = len(edges) + 1
        neighbors = defaultdict(list)

        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)

        visited = [False] * (N + 1)
        visited[1] = True

        queue = deque([1])

        depth = 0
        while len(queue) > 0:
            for _ in range(len(queue)):
                node = queue.pop()
                for neighbor in neighbors[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.appendleft(neighbor)

            if len(queue) > 0:
                depth += 1

        return pow(2, depth - 1, MODN)


sol = Solution()
print(sol.assignEdgeWeights([[1, 2]]))
print(sol.assignEdgeWeights([[1, 2], [1, 3], [3, 4], [3, 5]]))
