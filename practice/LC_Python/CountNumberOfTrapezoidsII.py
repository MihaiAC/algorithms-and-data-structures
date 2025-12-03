from collections import defaultdict
from typing import List


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        N = len(points)
        INF = 10**9 + 7
        slope_to_intercept = defaultdict(list)
        mid_to_slope = defaultdict(list)

        for idx1 in range(N - 1):
            x1, y1 = points[idx1]
            for idx2 in range(idx1 + 1, N):
                x2, y2 = points[idx2]
                dx = x1 - x2

                if dx == 0:
                    slope = INF
                    intercept = x1
                else:
                    slope = (y2 - y1) / dx
                    intercept = (y1 * dx - x1 * (y1 - y2)) / dx

                mid = (x1 + x2) * 10000 + (y1 + y2)
                slope_to_intercept[slope].append(intercept)
                mid_to_slope[mid].append(slope)

        ans = 0

        # Count trapezoids
        for intercepts in slope_to_intercept.values():
            if len(intercepts) <= 1:
                continue

            intercept_count = defaultdict(int)
            for intercept in intercepts:
                intercept_count[intercept] += 1

            total = 0
            for count in intercept_count.values():
                ans += total * count
                total += count

        # Subtract parallelograms
        for slopes in mid_to_slope.values():
            if len(slopes) <= 1:
                continue

            slope_count = defaultdict(int)
            for slope in slopes:
                slope_count[slope] += 1

            total = 0
            for count in slope_count.values():
                ans -= total * count
                total += count

        return ans


points = [[82, 7], [82, -9], [82, -52], [82, 78]]
sol = Solution()
print(sol.countTrapezoids(points))
