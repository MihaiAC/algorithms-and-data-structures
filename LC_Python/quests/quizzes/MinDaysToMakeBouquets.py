from typing import List
from heapq import heappush, heappop


def createRollingMax(days: int, k: int) -> int:
    n = len(days)

    # rollingMax[idx] = maximum value from max(0, idx-k+1) to days[idx].
    rollingMax = []

    heap = []

    for idx in range(n):
        heappush(heap, (-days[idx], idx))
        while heap[0][1] < max(0, idx - k + 1):
            heappop(heap)
        rollingMax.append(-heap[0][0])

    return rollingMax


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)

        if n < m * k:
            return -1

        prev = [0 for _ in range(n)]
        rollingMax = createRollingMax(bloomDay, k)

        for jj in range(1, m + 1):
            curr = [float("inf") for _ in range(n)]
            start = jj * k - 1
            curr[start] = max(rollingMax[start], prev[start - k])
            for ii in range(start + 1, n):
                curr[ii] = min(
                    curr[ii - 1],
                    max(
                        rollingMax[ii],
                        prev[ii - k],
                    ),
                )
            prev = curr

        return min(prev)


sol = Solution()
print(sol.minDays([1, 10, 3, 10, 2], 3, 1))
print(sol.minDays([1, 10, 3, 10, 2], 3, 2))
print(sol.minDays([7, 7, 7, 7, 12, 7, 7], 2, 3))
