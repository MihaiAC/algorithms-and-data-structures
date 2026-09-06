from typing import List
from collections import defaultdict

# https://cp-algorithms.com/graph/bridge-searching.html#implementation


class Solution:
    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
        neighbour = defaultdict(list)
        for u, v in connections:
            neighbour[u].append(v)
            neighbour[v].append(u)

        visited = [False] * n
        tin = [0] * n  # time a node was visited
        low = [0] * n  # earliest tin reachable from node's subtree
        timer = -1
        bridges = []

        def dfs(node: int, parent: int = -1):
            nonlocal timer
            timer += 1

            visited[node] = True
            tin[node] = timer
            low[node] = timer

            for nxt_node in neighbour[node]:
                if nxt_node == parent:
                    continue

                if visited[nxt_node]:
                    low[node] = min(low[node], tin[nxt_node])
                else:
                    dfs(nxt_node, node)
                    low[node] = min(low[node], low[nxt_node])

                    if low[nxt_node] > tin[node]:
                        bridges.append((node, nxt_node))

        dfs(0)
        return bridges


sol = Solution()
print(sol.criticalConnections(4, [[0, 1], [1, 2], [2, 0], [1, 3]]))
print(sol.criticalConnections(2, [[0, 1]]))
