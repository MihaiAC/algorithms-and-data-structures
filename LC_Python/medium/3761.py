from typing import List
from collections import defaultdict


def reverseNum(num: int) -> int:
    """We know num != 0."""
    while num % 10 == 0:
        num = num // 10
    return int("".join(str(num)[::-1]))


class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        N = len(nums)
        closestIdx = defaultdict(int)
        min_dist = N + 1

        for idx in range(N - 1, -1, -1):
            num = nums[idx]
            reverse_num = reverseNum(num)
            if reverse_num in closestIdx:
                min_dist = min(min_dist, closestIdx[reverse_num] - idx)
            closestIdx[num] = idx

        return min_dist if min_dist < N + 1 else -1


sol = Solution()
print(sol.minMirrorPairDistance([12, 45, 21, 33, 54]))
print(sol.minMirrorPairDistance([120, 21]))
print(sol.minMirrorPairDistance([21, 120]))
