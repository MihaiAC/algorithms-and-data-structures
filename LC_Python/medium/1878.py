from typing import List, Tuple
from collections import defaultdict


# No need to use heap for three elements.
def update_arr(x: int, big_three: List[int]):
    if x in big_three:
        return
    elif len(big_three) < 3:
        big_three.append(x)
    else:
        min_val = min(big_three, default=0)
        if x > min_val:
            big_three[big_three.index(min_val)] = x


class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        M, N = len(grid), len(grid[0])
        top_left = defaultdict(int)
        top_right = defaultdict(int)

        ans = []

        for ii in range(M):
            for jj in range(N):
                # Top left neighbor
                top_left[(ii, jj)] = grid[ii][jj] + top_left[(ii - 1, jj - 1)]

                # Top right neighbor
                top_right[(ii, jj)] = grid[ii][jj] + top_right[(ii - 1, jj + 1)]

                update_arr(grid[ii][jj], ans)

        def within_bounds(point: Tuple[int, int]) -> bool:
            return 0 <= point[0] and 0 <= point[1] and point[0] < M and point[1] < N

        for width in range(1, N, 2):
            for ii in range(M):
                for jj in range(N):
                    half = (width - 1) // 2
                    top = (ii, jj)
                    bottom = (ii + 2 * half + 2, jj)
                    left = (ii + half + 1, jj - half - 1)
                    right = (ii + half + 1, jj + half + 1)

                    if any(
                        not within_bounds(point) for point in [top, bottom, left, right]
                    ):
                        continue

                    perimeter = (
                        (top_right[bottom] - top_right[right])
                        + (top_right[left] - top_right[top])
                        + (top_left[bottom] - top_left[left])
                        + (top_left[right] - top_left[top])
                        - grid[bottom[0]][bottom[1]]
                        + grid[top[0]][top[1]]
                    )

                    update_arr(perimeter, ans)

        ans.sort(reverse=True)
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(
        sol.getBiggestThree(
            [
                [3, 4, 5, 1, 3],
                [3, 3, 4, 2, 3],
                [20, 30, 200, 40, 10],
                [1, 5, 5, 4, 1],
                [4, 3, 2, 2, 5],
            ]
        )
    )
    print(sol.getBiggestThree([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(sol.getBiggestThree([[7, 7, 7]]))
