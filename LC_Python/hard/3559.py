from typing import List, Dict
from collections import defaultdict
import math

MODN = 10**9 + 7


class LcaWrapper:
    def __init__(self, neighbors: Dict[int, List[int]]):
        self.N = len(neighbors)
        self.log = math.ceil(math.log2(self.N)) if self.N > 1 else 1

        self.preprocess(neighbors)

    def preprocess(self, neighbors: Dict[int, List[int]]):
        self.time_in = [0] * (self.N + 1)
        self.time_out = [0] * (self.N + 1)
        self.up = [[0] * (self.log + 1) for _ in range(self.N + 1)]

        timer = 0

        def dfs(node: int, parent: int):
            nonlocal timer
            timer += 1

            self.time_in[node] = timer
            self.up[node][0] = parent

            for exp in range(1, self.log + 1):
                self.up[node][exp] = self.up[self.up[node][exp - 1]][exp - 1]

            for neighbor in neighbors[node]:
                if neighbor != parent:
                    dfs(neighbor, node)

            timer += 1
            self.time_out[node] = timer

        dfs(1, 1)

    def is_ancestor(self, node1: int, node2: int) -> bool:
        return (
            self.time_in[node1] <= self.time_in[node2]
            and self.time_out[node1] >= self.time_out[node2]
        )

    def lca(self, node1: int, node2: int) -> int:
        if self.is_ancestor(node1, node2):
            return node1

        if self.is_ancestor(node2, node1):
            return node2

        for exp in range(self.log, -1, -1):
            if not self.is_ancestor(self.up[node1][exp], node2):
                node1 = self.up[node1][exp]

        return self.up[node1][0]


class Solution:
    def assignEdgeWeights(
        self, edges: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        neighbors = defaultdict(list)

        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)

        lca_wrapper = LcaWrapper(neighbors)

        depth = [0] * (lca_wrapper.N + 1)

        def calc_depth(node: int, parent: int) -> int:
            for neighbor in neighbors[node]:
                if neighbor != parent:
                    depth[neighbor] = depth[node] + 1
                    calc_depth(neighbor, node)

        calc_depth(1, 1)

        ans = []
        for node1, node2 in queries:
            lca_node = lca_wrapper.lca(node1, node2)
            distance = depth[node1] + depth[node2] - 2 * depth[lca_node]
            ans.append(0 if distance == 0 else pow(2, distance - 1, MODN))

        return ans


sol = Solution()
print(sol.assignEdgeWeights([[1, 2]], [[1, 1], [1, 2]]))
print(sol.assignEdgeWeights([[1, 2], [1, 3], [3, 4], [3, 5]], [[1, 4], [3, 4], [2, 5]]))
