from typing import List
from math import floor, log2


class Solution:
    def pathExistenceQueries(
        self, N: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[int]:
        nums = [(nums[idx], idx) for idx in range(N)]
        nums.sort()

        sorted_idx = [0] * N
        for idx in range(N):
            sorted_idx[nums[idx][1]] = idx

        first_unreachable = [0] * (N + 1)
        right = 0
        for left in range(N):
            while right + 1 < N and nums[right + 1][0] - nums[left][0] <= maxDiff:
                right += 1

            if right < left:
                right = left

            first_unreachable[left] = right

        # Calculate how big our sparse array should be.
        K = floor(log2(N)) + 1

        # Binary jumping.
        skip = [[0] * (K + 1) for _ in range(N + 1)]

        for idx in range(N):
            skip[idx][0] = first_unreachable[idx]

        for pow_idx in range(1, K):
            for idx in range(N):
                skip[idx][pow_idx] = skip[skip[idx][pow_idx - 1]][pow_idx - 1]

        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue

            left_idx, right_idx = (
                min(sorted_idx[u], sorted_idx[v]),
                max(sorted_idx[u], sorted_idx[v]),
            )

            if first_unreachable[left_idx] == left_idx:
                ans.append(-1)
                continue

            curr_idx = left_idx
            curr_step = 0

            for pow_idx in range(K - 1, -1, -1):
                if skip[curr_idx][pow_idx] < right_idx:
                    curr_idx = skip[curr_idx][pow_idx]
                    curr_step += 2**pow_idx

            if first_unreachable[curr_idx] < right_idx:
                ans.append(-1)
            else:
                ans.append(curr_step + 1)

        return ans


sol = Solution()
print(sol.pathExistenceQueries(5, [1, 8, 3, 4, 2], 3, [[0, 3], [2, 4]]))
print(
    sol.pathExistenceQueries(5, [5, 3, 1, 9, 10], 2, [[0, 1], [0, 2], [2, 3], [4, 3]])
)
print(sol.pathExistenceQueries(3, [3, 6, 1], 1, [[0, 0], [0, 1], [1, 2]]))
