from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        window = set()
        for num in nums[: (k + 1)]:
            if num in window:
                return True
            window.add(num)

        for idx in range(k + 1, N):
            window.remove(nums[idx - k - 1])
            if nums[idx] in window:
                return True
            window.add(nums[idx])

        return False


sol = Solution()
assert sol.containsNearbyDuplicate([1, 2, 3, 1], 3)
assert sol.containsNearbyDuplicate([1, 0, 1, 1], 1)
assert not sol.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2)
