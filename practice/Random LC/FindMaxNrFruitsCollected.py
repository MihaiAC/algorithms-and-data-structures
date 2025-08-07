from typing import List
from collections import defaultdict

class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        N = len(fruits)
        ans = 0
        for ii in range(N):
            ans += fruits[ii][ii]
            fruits[ii][ii] = 0

        deltas = [(1, -1), (1, 0), (1, 1)]
        
        def bfs() -> int:
            dp = defaultdict(lambda: -1)
            dp[(0, N-1)] = fruits[0][N-1]

            for _ in range(N-1):
                next_dp = defaultdict(lambda: -1)
                for (x, y), val in dp.items():
                    if val == -1: continue
                    for dx, dy in deltas:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < N and ny >= nx and nx + ny >= N - 1:
                            new_val = val + fruits[nx][ny]
                            next_dp[(nx, ny)] = max(next_dp[(nx, ny)], new_val)
                dp = next_dp
                if not dp:
                    return 0

            return dp.get((N-1, N-1), 0)

        ans += bfs()
        for ii in range(N):
            for jj in range(ii):
                fruits[ii][jj], fruits[jj][ii] = fruits[jj][ii], fruits[ii][jj]
        
        ans += bfs()
        return ans
        