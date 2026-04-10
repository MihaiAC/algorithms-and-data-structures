from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        if len(nums_set) <= 1:
            return len(nums_set)

        size = {}

        for num in nums_set:
            if num - 1 not in nums_set:
                continue

            if num - 1 in size:
                size[num] = 1 + size[num - 1]
            else:
                x = num
                chain = 1
                while x - 1 in nums_set:
                    x -= 1
                    chain += 1
                    size[x] = 2
                size[num] = chain

        return max(size.values()) if size else 1


sol = Solution()
print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))
print(sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
print(sol.longestConsecutive([1, 0, 1, 2]))
