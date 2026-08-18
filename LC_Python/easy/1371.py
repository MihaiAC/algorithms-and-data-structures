from typing import List
from collections import Counter


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        N = len(nums)

        if k == N:
            return max(nums)
        elif k == 1:
            freq = Counter(nums)
            ans = -1

            for num in freq:
                if freq[num] == 1:
                    ans = max(ans, num)

            return ans
        else:
            left, right = nums[0], nums[-1]

            if left == right:
                return -1

            for num in nums[1:-1]:
                if num == left:
                    left = -1

                if num == right:
                    right = -1

            return max(left, right)


sol = Solution()
print(sol.largestInteger([3, 9, 2, 1, 7], 3))
print(sol.largestInteger([3, 9, 7, 2, 1, 7], 4))
print(sol.largestInteger([0, 0], 1))
