from typing import List


class Solution:
    def minimumWeight(
        self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int
    ) -> int:
        # Floyd-Warshall (might be too slow)
        dist = [[float("inf") for _ in range(n)] for _ in range(n)]

        for x in range(n):
            dist[x][x] = 0

        for x, y, w in edges:
            dist[x][y] = min(dist[x][y], w)

        for k in range(n):
            for x in range(n):
                for y in range(n):
                    if dist[x][k] + dist[k][y] < dist[x][y]:
                        dist[x][y] = dist[x][k] + dist[k][y]

        ans = float("inf")
        for x in range(n):
            ans = min(ans, dist[src1][x] + dist[src2][x] + dist[x][dest])

        return ans if ans != float("inf") else -1


sol = Solution()
print(
    sol.minimumWeight(
        6,
        [
            [0, 2, 2],
            [0, 5, 6],
            [1, 0, 3],
            [1, 4, 5],
            [2, 1, 1],
            [2, 3, 3],
            [2, 3, 4],
            [3, 4, 2],
            [4, 5, 1],
        ],
        0,
        1,
        5,
    )
)
