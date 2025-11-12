from typing import List
from math import gcd
from functools import reduce


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        overall_gcd = nums[0]
        num_ones = 0
        N = len(nums)

        for num in nums:
            overall_gcd = gcd(overall_gcd, num)
            num_ones += num == 1

        if num_ones > 0:
            return N - num_ones

        if overall_gcd != 1:
            return -1

        def check_subarray_len(length: int) -> bool:
            for ii in range(N - length + 1):
                subarray_gcd = reduce(gcd, nums[ii : (ii + length)], nums[ii])
                if subarray_gcd == 1:
                    return True
            return False

        left, right = 2, N
        while left < right:
            mid = (left + right) // 2
            if check_subarray_len(mid):
                right = mid
            else:
                left = mid + 1

        return left + N - 2
