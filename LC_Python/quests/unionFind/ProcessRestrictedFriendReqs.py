from typing import List


class Solution:
    def friendRequests(
        self, N: int, restrictions: List[List[int]], requests: List[List[int]]
    ) -> List[bool]:
        parent = list(range(N))
        size = [1] * N

        incompat = [set() for _ in range(N)]
        for u, v in restrictions:
            incompat[u].add(v)
            incompat[v].add(u)

        def find(x: int) -> int:
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def recalc_incompat(x: int):
            new_incompat = set()
            for node in incompat[x]:
                new_incompat.add(find(node))
            incompat[x] = new_incompat

        def union(x: int, y: int) -> bool:
            x = find(x)
            y = find(y)

            if x == y:
                return True

            if size[x] > size[y]:
                x, y = y, x

            recalc_incompat(x)
            recalc_incompat(y)

            if x in incompat[y] or y in incompat[x]:
                return False

            parent[x] = y
            size[y] += size[x]
            incompat[y] = incompat[y].union(incompat[x])
            return True

        ans = []
        for u, v in requests:
            ans.append(union(u, v))

        return ans


sol = Solution()
print(sol.friendRequests(3, [[0, 1]], [[0, 2], [2, 1]]))
print(sol.friendRequests(3, [[0, 1]], [[1, 2], [0, 2]]))
print(sol.friendRequests(5, [[0, 1], [1, 2], [2, 3]], [[0, 4], [1, 2], [3, 1], [3, 4]]))
