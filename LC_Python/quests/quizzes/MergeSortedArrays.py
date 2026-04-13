from typing import List
from collections import deque


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        extra = deque()
        idx1 = 0
        idx2 = 0

        for idx1 in range(m + n):
            if idx1 < m:
                extra.append(nums1[idx1])

            if len(extra) > 0 and idx2 < n:
                if nums2[idx2] < extra[0]:
                    nums1[idx1] = nums2[idx2]
                    idx2 += 1
                else:
                    nums1[idx1] = extra[0]
                    extra.popleft()
            elif idx2 < n:
                nums1[idx1] = nums2[idx2]
                idx2 += 1
            else:
                nums1[idx1] = extra[0]
                extra.popleft()


sol = Solution()
n1 = [1, 2, 3, 0, 0, 0]
n2 = [2, 5, 6]
sol.merge(n1, 3, n2, 3)
print(n1)
