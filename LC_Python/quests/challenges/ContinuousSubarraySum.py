from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        elif len(nums) == 2:
            return sum(nums) % k == 0

        mods = {0}
        currSum = 0
        for idx in range(len(nums) - 1):
            if (currSum + nums[idx] + nums[idx + 1]) % k in mods:
                return True

            currSum = (currSum + nums[idx]) % k
            mods.add(currSum)

        return False


if __name__ == "__main__":
    sol = Solution()
    assert sol.checkSubarraySum([23, 2, 4, 6, 7], 6)
    assert sol.checkSubarraySum([23, 2, 6, 4, 7], 6)
    assert not sol.checkSubarraySum([23, 2, 6, 4, 7], 13)
