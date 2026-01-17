from typing import List


class Solution:
    def largestSquareArea(
        self, bottomLeft: List[List[int]], topRight: List[List[int]]
    ) -> int:
        N = len(bottomLeft)
        max_side = 0

        for ii in range(N - 1):
            bl_ii, tr_ii = bottomLeft[ii], topRight[ii]
            for jj in range(ii + 1, N):
                bl_jj, tr_jj = bottomLeft[jj], topRight[jj]

                dx = min(tr_ii[0], tr_jj[0]) - max(bl_ii[0], bl_jj[0])
                dy = min(tr_ii[1], tr_jj[1]) - max(bl_ii[1], bl_jj[1])

                max_side = max(max_side, min(dx, dy))

        return max_side**2
