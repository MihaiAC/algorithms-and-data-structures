from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.N = len(nums)
        self.segment = [0] * (4 * self.N + 1)
        self.build(nums, 1, 0, self.N - 1)

    def build(self, nums: List[int], segIdx: int, left: int, right: int):
        if left == right:
            self.segment[segIdx] = nums[left]
        else:
            mid = (left + right) // 2
            self.build(nums, 2 * segIdx, left, mid)
            self.build(nums, 2 * segIdx + 1, mid + 1, right)
            self.segment[segIdx] = (
                self.segment[2 * segIdx] + self.segment[2 * segIdx + 1]
            )

    def _update(self, segIdx: int, left: int, right: int, idx: int, new_val: int):
        if left == right:
            self.segment[segIdx] = new_val
        else:
            mid = (left + right) // 2
            if idx <= mid:
                self._update(2 * segIdx, left, mid, idx, new_val)
            else:
                self._update(2 * segIdx + 1, mid + 1, right, idx, new_val)
            self.segment[segIdx] = (
                self.segment[2 * segIdx] + self.segment[2 * segIdx + 1]
            )

    def update(self, index: int, val: int) -> None:
        self._update(1, 0, self.N - 1, index, val)

    def _sum(
        self, segIdx: int, segLeft: int, segRight: int, left: int, right: int
    ) -> int:
        if left > right:
            return 0

        if left == segLeft and right == segRight:
            return self.segment[segIdx]

        segMid = (segLeft + segRight) // 2
        return self._sum(
            2 * segIdx, segLeft, segMid, left, min(right, segMid)
        ) + self._sum(
            2 * segIdx + 1, segMid + 1, segRight, max(left, segMid + 1), right
        )

    def sumRange(self, left: int, right: int) -> int:
        return self._sum(1, 0, self.N - 1, left, right)
