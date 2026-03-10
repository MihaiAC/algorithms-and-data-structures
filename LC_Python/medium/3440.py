from heapq import heappush, heappushpop
from typing import List


class Solution:
    def maxFreeTime(
        self, eventTime: int, startTime: List[int], endTime: List[int]
    ) -> int:
        N = len(startTime)
        top3_gaps = []

        def insert_gap(gap_len: int, start_idx: int):
            if len(top3_gaps) < 3:
                heappush(top3_gaps, (gap_len, start_idx))
            elif gap_len > top3_gaps[0][0]:
                heappushpop(top3_gaps, (gap_len, start_idx))

        def get_largest_avail_gap(curr_idx: int) -> int:
            largest_len = -1
            for gap_len, start_idx in top3_gaps:
                if (
                    start_idx != curr_idx
                    and start_idx != curr_idx - 1
                    and gap_len > largest_len
                ):
                    largest_len = gap_len
            return largest_len

        for idx in range(N):
            # Adding only the left gap.
            if idx > 0:
                insert_gap(startTime[idx] - endTime[idx - 1], idx - 1)
            elif startTime[idx] > 0:
                insert_gap(startTime[idx], -1)

        # Add the last gap.
        if endTime[N - 1] < eventTime:
            insert_gap(eventTime - endTime[N - 1], N - 1)

        # For each tile, see if you can move it to another spot or not.
        ans = 0
        for idx in range(N):
            tile_len = endTime[idx] - startTime[idx]
            largest_free_gap = get_largest_avail_gap(idx)

            left_gap = startTime[idx] - endTime[idx - 1] if idx > 0 else startTime[idx]
            right_gap = (
                startTime[idx + 1] - endTime[idx]
                if idx < N - 1
                else eventTime - endTime[idx]
            )

            if largest_free_gap >= tile_len:
                ans = max(ans, left_gap + right_gap + tile_len)
            else:
                ans = max(ans, left_gap + right_gap)

        return ans


if __name__ == "__main__":
    sol = Solution()
    eventTime = 41
    startTime = [17, 24]
    endTime = [19, 25]

    print(sol.maxFreeTime(eventTime, startTime, endTime))
