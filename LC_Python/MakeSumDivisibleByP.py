from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        rightmost_idx = {0: -1}
        MOD = sum(nums) % p

        if MOD == 0:
            return 0

        prefix = 0
        ans = len(nums)

        for idx in range(len(nums)):
            num = nums[idx]
            prefix += num

            target_mod = (prefix - MOD + p) % p
            if target_mod in rightmost_idx:
                ans = min(ans, idx - rightmost_idx[target_mod])

            rightmost_idx[prefix % p] = idx

        return ans if ans != len(nums) else -1
