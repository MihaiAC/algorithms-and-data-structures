from typing import List
from collections import deque


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        N = len(arr)

        visited = [False] * N
        visited[start] = True

        queue = deque()
        queue.appendleft(start)

        while len(queue) > 0:
            cidx = queue.pop()

            if arr[cidx] == 0:
                return True

            for nidx in [cidx + arr[cidx], cidx - arr[cidx]]:
                if 0 <= nidx < N and not visited[nidx]:
                    visited[nidx] = True
                    queue.appendleft(nidx)

        return False


sol = Solution()
print(sol.canReach([4, 2, 3, 0, 3, 1, 2], 5))
print(sol.canReach([4, 2, 3, 0, 3, 1, 2], 0))
print(sol.canReach([3, 0, 2, 1, 2], 2))
