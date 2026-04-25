from typing import List
from bisect import bisect_left


class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        # Map all the points to one line.
        # (0, y) -> y
        # (x, side) -> side + x
        # (side, y) -> 3*side-y
        # (x, 0) -> 4*side-x
        arr = []
        for x, y in points:
            if x == 0:
                arr.append(y)
            elif y == side:
                arr.append(side + x)
            elif x == side:
                arr.append(3 * side - y)
            else:
                arr.append(4 * side - x)

        # Sort the array.
        arr.sort()

        def is_possible(min_dist: int) -> bool:
            for start in arr:
                left = start
                # Encodes the wrap-around - useful only if start is on the first side (I think)
                right = start + 4 * side - min_dist
                found = True
                curr_idx = 1

                for _ in range(k - 1):
                    curr_idx = bisect_left(arr, left + min_dist, lo=curr_idx)
                    if curr_idx == len(arr) or arr[curr_idx] > right:
                        found = False
                        break
                    left = arr[curr_idx]

                if found:
                    return True
            return False

        left_dist, right_dist = 1, 2 * side
        while left_dist < right_dist:
            mid_dist = (left_dist + right_dist + 1) // 2
            if is_possible(mid_dist):
                left_dist = mid_dist
            else:
                right_dist = mid_dist - 1
        return left_dist


sol = Solution()
print(sol.maxDistance(2, [[0, 2], [2, 0], [2, 2], [0, 0]], 4))
print(sol.maxDistance(2, [[0, 0], [1, 2], [2, 0], [2, 2], [2, 1]], 4))
print(sol.maxDistance(2, [[0, 0], [0, 1], [0, 2], [1, 2], [2, 0], [2, 2], [2, 1]], 5))
