from typing import List


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        root = list(range(n))
        size = [1] * n

        def find(u: int) -> int:
            if u == root[u]:
                return u
            root[u] = find(root[u])
            return root[u]

        def union(u: int, v: int):
            u = find(u)
            v = find(v)

            if u == v:
                return

            if size[v] < size[u]:
                u, v = v, u

            root[u] = v
            size[v] += size[u]

        for u, v in edges:
            union(u, v)

        return find(source) == find(destination)


sol = Solution()
print(sol.validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2))
print(sol.validPath(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5))
