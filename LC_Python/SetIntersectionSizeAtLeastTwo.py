from typing import List


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        p1, p2 = -1, -1
        count = 0
        
        for start, end in intervals:
            if start <= p1:
                continue
            elif start <= p2:
                p1 = p2
                p2 = end
                count += 1
            else:
                p1 = end - 1
                p2 = end
                count += 2
                
        return count
