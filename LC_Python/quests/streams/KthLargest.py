from typing import List
from heapq import heappush, heappushpop


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heappush(self.heap, val)
        elif val > self.heap[0]:
            heappushpop(self.heap, val)
        return self.heap[0]
