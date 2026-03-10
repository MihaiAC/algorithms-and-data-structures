class Solution:
    def minCost(self, grid: list[list[int]], k: int) -> int:
        M, N = len(grid), len(grid[0])
        points = [(ii, jj) for ii in range(M) for jj in range(N)]
        points.sort(key=lambda p: grid[p[0]][p[1]])
        costs = [[float("inf")] * N for _ in range(M)]

        for t in range(k + 1):
            minCost = float("inf")
            jj = 0

            # Update costs for points with the same grid value.
            for ii in range(len(points)):
                minCost = min(minCost, costs[points[ii][0]][points[ii][1]])

                if (
                    ii + 1 < len(points)
                    and grid[points[ii][0]][points[ii][1]]
                    == grid[points[ii + 1][0]][points[ii + 1][1]]
                ):
                    ii += 1
                    continue

                for r in range(jj, ii + 1):
                    costs[points[r][0]][points[r][1]] = minCost

                jj = ii + 1

            # Update caosts with teleportations taken into account.
            for ii in range(M - 1, -1, -1):
                for jj in range(N - 1, -1, -1):
                    if ii == M - 1 and jj == N - 1:
                        costs[ii][jj] = 0
                        continue

                    if ii != M - 1:
                        costs[ii][jj] = min(
                            costs[ii][jj], costs[ii + 1][jj] + grid[ii + 1][jj]
                        )

                    if jj != N - 1:
                        costs[ii][jj] = min(
                            costs[ii][jj], costs[ii][jj + 1] + grid[ii][jj + 1]
                        )

        return costs[0][0]
