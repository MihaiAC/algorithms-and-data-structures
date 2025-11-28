from typing import List, deque
from collections import defaultdict


class Solution:
    def maxKDivisibleComponents(
        self, n: int, edges: List[List[int]], values: List[int], k: int
    ) -> int:
        neighbors = defaultdict(list)
        degree = defaultdict(int)
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)

            degree[u] += 1
            degree[v] += 1

        curr_nodes = deque()
        for node in range(n):
            if degree[node] <= 1:
                curr_nodes.appendleft(node)

        n_components = 0
        while len(curr_nodes) > 0:
            node = curr_nodes.pop()
            degree[node] -= 1

            remainder = values[node] % k
            if remainder == 0:
                n_components += 1

            for neighbor in neighbors[node]:
                if degree[neighbor] == 0:
                    continue

                degree[neighbor] -= 1
                values[neighbor] += remainder

                if degree[neighbor] == 1:
                    curr_nodes.appendleft(neighbor)

        return n_components
