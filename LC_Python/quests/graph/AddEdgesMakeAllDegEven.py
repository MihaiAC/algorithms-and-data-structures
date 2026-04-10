from typing import List
from collections import defaultdict


class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        neighbors = defaultdict(set)

        for n1, n2 in edges:
            neighbors[n1].add(n2)
            neighbors[n2].add(n1)

        nodes = []
        for node in range(1, n + 1):
            if len(neighbors[node]) % 2 == 1:
                nodes.append(node)

        if len(nodes) > 4:
            return False
        elif len(nodes) == 4:
            # Need to find two pairs among the 4 s.t there are no direct edges between the nodes in each pair.
            a, b, c, d = nodes

            # (a, b), (c, d)
            if b not in neighbors[a] and d not in neighbors[c]:
                return True

            # (a, c), (b, d)
            if a not in neighbors[c] and b not in neighbors[d]:
                return True

            # (a, d), (b, c)
            if a not in neighbors[d] and b not in neighbors[c]:
                return True

            return False

        elif len(nodes) == 2:
            if nodes[0] not in neighbors[nodes[1]]:
                return True
            for node in range(1, n + 1):
                if (
                    node != nodes[0]
                    and node != nodes[1]
                    and node not in neighbors[nodes[0]]
                    and node not in neighbors[nodes[1]]
                ):
                    return True
            return False
        elif len(nodes) == 0:
            return True
        return False


sol = Solution()
print(sol.isPossible(5, [[1, 2], [2, 3], [3, 4], [4, 2], [1, 4], [2, 5]]))
print(sol.isPossible(4, [[1, 2], [3, 4]]))
print(sol.isPossible(4, [[1, 2], [1, 3], [1, 4]]))
