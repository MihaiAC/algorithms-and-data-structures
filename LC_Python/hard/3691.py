from typing import List
from heapq import heappush, heappop

# Adapted from 3161.


class SegmentTree:
    def __init__(self, nums: list):
        self.n = len(nums)
        self.max_tree = [0] * (4 * self.n)
        self.min_tree = [0] * (4 * self.n)

        self._build(nums, 1, 0, self.n - 1)

    def _build(self, nums: list, node: int, seg_left: int, seg_right: int):
        if seg_left == seg_right:
            self.max_tree[node] = nums[seg_left]
            self.min_tree[node] = nums[seg_left]

            return

        mid = (seg_left + seg_right) // 2
        self._build(nums, 2 * node, seg_left, mid)
        self._build(nums, 2 * node + 1, mid + 1, seg_right)

        self.max_tree[node] = max(self.max_tree[2 * node], self.max_tree[2 * node + 1])
        self.min_tree[node] = min(self.min_tree[2 * node], self.min_tree[2 * node + 1])

    def query(self, range_left: int, range_right: int) -> tuple:
        return self._query(1, 0, self.n - 1, range_left, range_right)

    def _query(
        self,
        node: int,
        seg_left: int,
        seg_right: int,
        range_left: int,
        range_right: int,
    ) -> tuple:
        if range_left > range_right:
            return float("inf"), 0

        if range_left == seg_left and range_right == seg_right:
            return self.min_tree[node], self.max_tree[node]

        mid = (seg_left + seg_right) // 2

        left_min, left_max = self._query(
            2 * node, seg_left, mid, range_left, min(range_right, mid)
        )
        right_min, right_max = self._query(
            2 * node + 1, mid + 1, seg_right, max(range_left, mid + 1), range_right
        )

        return min(left_min, right_min), max(left_max, right_max)


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        N = len(nums)
        tree = SegmentTree(nums)
        heap = []

        for left_idx in range(len(nums)):
            range_min, range_max = tree.query(left_idx, N - 1)
            heappush(heap, (range_min - range_max, left_idx, N - 1))

        ans = 0
        for _ in range(k):
            val, left_idx, right_idx = heappop(heap)
            ans -= val

            if right_idx > left_idx:
                right_idx -= 1
                range_min, range_max = tree.query(left_idx, right_idx)
                heappush(heap, (range_min - range_max, left_idx, right_idx))

        return ans


sol = Solution()
print(sol.maxTotalValue([1, 3, 2], 2))
print(sol.maxTotalValue([4, 2, 5, 1], 3))
