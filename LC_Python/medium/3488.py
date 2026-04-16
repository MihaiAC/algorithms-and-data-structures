from typing import List
from collections import defaultdict
from bisect import bisect_left


class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        N = len(nums)
        ans = []

        indices = defaultdict(list)
        for idx, num in enumerate(nums):
            indices[num].append(idx)

        for query_idx in queries:
            query_num = nums[query_idx]
            occurrences = indices.get(query_num, [])
            M = len(indices.get(query_num, []))

            if M in [0, 1]:
                ans.append(-1)
                continue

            find_idx = bisect_left(occurrences, query_idx)
            min_dist = N + 1

            if find_idx == M - 1:
                min_dist = min(
                    query_idx - occurrences[find_idx - 1],
                    N - query_idx + occurrences[0],
                )
            elif find_idx == 0:
                min_dist = min(
                    occurrences[1] - query_idx, query_idx + N - occurrences[-1]
                )
            else:
                min_dist = min(
                    query_idx - occurrences[find_idx - 1],
                    occurrences[find_idx + 1] - query_idx,
                )

            ans.append(min_dist)

        return ans


sol = Solution()
print(sol.solveQueries([1, 3, 1, 4, 1, 3, 2], [0, 3, 5, 1]))
