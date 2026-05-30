from typing import List
from sortedcontainers import SortedList

# This is a combination of https://cp-algorithms.com/data_structures/segment_tree.html#sum-queries
# and the editorial.
# The hints and the explanation in the editorial were not great for this one.
# But, the code in the editorial was understandable.
# Managed to understand the solution and implement it, which is OK for a Saturday.
# But yeah, giving this problem in an interview/contest is rough :))


class SegmentTree:
    def __init__(self, size: int):
        self.n = size
        self.tree = [0] * (4 * size)

    def update(
        self, pos: int, val: int, node: int = 1, seg_left: int = 0, seg_right: int = -1
    ):
        if seg_right == -1:
            seg_right = self.n - 1

        if seg_left == seg_right:
            self.tree[node] = val
            return

        mid = (seg_left + seg_right) // 2

        if pos <= mid:
            self.update(pos, val, 2 * node, seg_left, mid)
        else:
            self.update(pos, val, 2 * node + 1, mid + 1, seg_right)

        self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])

    def get_max(self, range_left: int, range_right: int) -> int:
        return self._get_max(1, 0, self.n - 1, range_left, range_right)

    def _get_max(
        self,
        node: int,
        seg_left: int,
        seg_right: int,
        range_left: int,
        range_right: int,
    ) -> int:
        if range_left > range_right:
            return 0

        if range_left == seg_left and range_right == seg_right:
            return self.tree[node]

        mid = (seg_left + seg_right) // 2

        left_max = self._get_max(
            2 * node, seg_left, mid, range_left, min(range_right, mid)
        )

        right_max = self._get_max(
            2 * node + 1, mid + 1, seg_right, max(range_left, mid + 1), range_right
        )
        return max(left_max, right_max)


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        # If TLE => use max bound. This is an additional O(len(queries)).
        max_pos = max(query[1] for query in queries) + 1

        st = SegmentTree(max_pos + 1)

        # Maintain a sorted list of obstacles.
        obstacles = SortedList([0, max_pos])

        # Add a fake obstacle at max_pos (bound).
        st.update(0, max_pos)

        results = []
        for query in queries:
            if query[0] == 1:
                # Coordinate of the obstacle we need to insert.
                obstacle_x = query[1]

                # Index of the obstacle inside the SortedList of obstacles.
                obstacle_idx = min(
                    len(obstacles) - 1, obstacles.bisect_right(obstacle_x)
                )

                # Coordinate of the obstacle to the right of the one we're inserting.
                right_obstacle_x = obstacles[obstacle_idx]

                # Coordinate of the obstacle to the left of the one we're inserting.
                left_obstacle_x = (
                    obstacles[obstacle_idx - 1] if obstacle_idx > 0 else obstacles[0]
                )

                # Update d[left_obstacle_x].
                st.update(left_obstacle_x, obstacle_x - left_obstacle_x)

                # Update d[obstacle_x].
                st.update(obstacle_x, right_obstacle_x - obstacle_x)

                # Add obstacle_x to the SortedList.
                obstacles.add(obstacle_x)
            else:
                x, sz = query[1:]
                results.append(st.get_max(0, x - sz) >= sz)

        return results


sol = Solution()
print(sol.getResults([[1, 2], [2, 3, 3], [2, 3, 1], [2, 2, 2]]))
print(sol.getResults([[1, 7], [2, 7, 6], [1, 2], [2, 7, 5], [2, 7, 6]]))
