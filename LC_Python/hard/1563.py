from typing import List


class Solution:
    def stoneGameV(self, stones: List[int]) -> int:
        cum_sum = [0]
        for stone in stones:
            cum_sum.append(cum_sum[-1] + stone)

        N = len(stones)
        max_stones = [[0] * N for _ in range(N)]

        for width in range(1, N):
            for left in range(N - width):
                right = left + width

                sum_right = cum_sum[right + 1] - cum_sum[left]
                sum_left, curr_max = 0, 0

                for idx in range(left, right):
                    sum_left += stones[idx]
                    sum_right -= stones[idx]

                    if sum_left < sum_right:
                        curr_max = max(curr_max, max_stones[left][idx] + sum_left)
                    elif sum_left > sum_right:
                        curr_max = max(curr_max, max_stones[idx + 1][right] + sum_right)
                    else:
                        curr_max = max(
                            curr_max,
                            max(
                                max_stones[left][idx],
                                max_stones[idx + 1][right],
                            )
                            + sum_left,
                        )

                max_stones[left][right] = curr_max

        return max_stones[0][N - 1]


sol = Solution()
print(sol.stoneGameV([6, 2, 3, 4, 5, 5]))
print(sol.stoneGameV([7, 7, 7, 7, 7, 7, 7]))
print(sol.stoneGameV([4]))
