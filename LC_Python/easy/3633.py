from typing import List
from bisect import bisect_right


class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:
        land_rides = sorted(zip(landStartTime, landDuration))
        water_rides = sorted(zip(waterStartTime, waterDuration))

        M = len(water_rides)

        water_earliest_end = [0] * M
        water_earliest_end[M - 1] = sum(water_rides[M - 1])
        for idx in range(M - 2, -1, -1):
            water_earliest_end[idx] = min(
                water_earliest_end[idx + 1], sum(water_rides[idx])
            )

        water_rolling_min_duration = [0] * M
        water_rolling_min_duration[0] = water_rides[0][1]
        for idx in range(1, M):
            water_rolling_min_duration[idx] = min(
                water_rolling_min_duration[idx - 1], water_rides[idx][1]
            )

        sorted_water_ends = sorted(start + duration for start, duration in water_rides)

        ans = 3001
        for land_start, land_duration in land_rides:
            land_finish = land_start + land_duration

            # Land first.
            water_idx = bisect_right(
                water_rides, land_finish, key=lambda water_ride: water_ride[0]
            )

            if water_idx < M:
                ans = min(ans, water_earliest_end[water_idx])

            if water_idx > 0:
                ans = min(ans, land_finish + water_rolling_min_duration[water_idx - 1])

            # Water first.
            water_end_idx = bisect_right(sorted_water_ends, land_start)
            if water_end_idx > 0:
                ans = min(ans, land_finish)
            else:
                ans = min(ans, sorted_water_ends[0] + land_duration)

        return ans


sol = Solution()
print(sol.earliestFinishTime([2, 8], [4, 1], [6], [3]))
print(sol.earliestFinishTime([5], [3], [1], [10]))
print(sol.earliestFinishTime([1000], [1000], [1000], [1000]))
