from typing import List


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        root = list(range(n + 1))
        min_dist = [float("inf")] * (n + 1)
        size = [1] * (n + 1)

        def find(x: int) -> int:
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]

        def union(x: int, y: int, dist: int):
            x = find(x)
            y = find(y)

            if x == y:
                min_dist[x] = min(min_dist[x], dist)
                return

            if size[x] > size[y]:
                x, y = y, x

            root[x] = y
            size[y] += size[x]
            min_dist[y] = min(min_dist[x], min_dist[y], dist)

        for u, v, dist in roads:
            union(u, v, dist)

        return min_dist[find(1)]


sol = Solution()
print(sol.minScore(4, [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]))
print(sol.minScore(4, [[1, 2, 2], [1, 3, 4], [3, 4, 7]]))
