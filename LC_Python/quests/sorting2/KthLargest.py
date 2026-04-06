from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        low, high = nums[0], nums[0]

        for num in nums:
            low = min(low, num)
            high = max(high, num)

        while True:
            guess = (low + high) // 2
            greater, equal = 0, 0

            for num in nums:
                greater += num > guess
                equal += num == guess

            if k <= greater:
                low = guess + 1
            elif k > greater + equal:
                high = guess - 1
            else:
                return guess
