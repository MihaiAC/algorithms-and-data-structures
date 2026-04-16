from typing import List
from sortedcontainers import SortedSet


class SummaryRanges:
    def __init__(self):
        self.set = SortedSet()

    def addNum(self, value: int) -> None:
        self.set.add(value)

    def getIntervals(self) -> List[List[int]]:
        intervals = []

        if len(self.set) == 0:
            return intervals

        left, right = self.set[0], self.set[0]
        for num in self.set[1:]:
            if num > right + 1:
                intervals.append([left, right])
                left, right = num, num
            else:
                right = num
        intervals.append([left, right])
        return intervals
