from typing import List
from collections import defaultdict


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        num_to_indices = defaultdict(list)

        for idx, num in enumerate(nums):
            num_to_indices[num].append(idx)

        ans = [0] * len(nums)
        for num, indices in num_to_indices.items():
            if len(indices) == 1:
                continue

            left_sum = 0
            right_sum = sum(indices)

            for ii, index in enumerate(indices):
                curr_dist = index * ii - left_sum
                right_sum -= index
                if ii < len(indices) - 1:
                    curr_dist += right_sum - (len(indices) - 1 - ii) * index

                ans[index] = curr_dist

                left_sum += index

        return ans


sol = Solution()
print(sol.distance([1, 3, 1, 1, 2]))
print(sol.distance([0, 5, 3]))
