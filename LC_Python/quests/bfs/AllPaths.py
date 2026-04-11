from typing import List
from collections import deque


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        queue = deque()
        queue.appendleft((0, []))

        ans = []

        while len(queue) > 0:
            for _ in range(len(queue)):
                curr_node, path = queue.pop()

                if curr_node == n - 1:
                    ans.append(path + [n - 1])
                    continue

                for nxt in graph[curr_node]:
                    queue.appendleft((nxt, [x for x in path] + [curr_node]))

        return ans


sol = Solution()
print(sol.allPathsSourceTarget([[1, 2], [3], [3], []]))
print(sol.allPathsSourceTarget([[4, 3, 1], [3, 2, 4], [3], [4], []]))
