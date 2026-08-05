from typing import List
from collections import defaultdict


class Solution:
    def remainingMethods(
        self, n: int, k: int, invocations: List[List[int]]
    ) -> List[int]:
        calls = defaultdict(list)

        for fn1, fn2 in invocations:
            calls[fn1].append(fn2)

        infected = {k}
        queue = [k]
        while len(queue) > 0:
            curr_fn = queue.pop()

            for fn in calls[curr_fn]:
                if fn not in infected:
                    infected.add(fn)
                    queue.append(fn)

        for fn1, fn2 in invocations:
            if fn1 not in infected and fn2 in infected:
                return list(range(n))

        return [fn for fn in range(n) if fn not in infected]


sol = Solution()
print(sol.remainingMethods(4, 1, [[1, 2], [0, 1], [3, 2]]))
print(sol.remainingMethods(5, 0, [[1, 2], [0, 2], [0, 1], [3, 4]]))
print(sol.remainingMethods(3, 2, [[1, 2], [0, 1], [2, 0]]))
