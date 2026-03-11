from typing import List

import SimpleProfiler


class Solution:
    @SimpleProfiler.profile
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        N = len(nums)
        jj, ii = 0, N - 1
        bin_string = ["0"] * N

        while jj <= ii:
            if nums[ii] + nums[jj] > target:
                ii -= 1
            else:
                bin_string[N - 1 - ii + jj] = "1"
                jj += 1

        return int("".join(bin_string), 2) % (10**9 + 7)


if __name__ == "__main__":
    with open("input.txt") as f:
        line = f.readline()
        nums = [int(x) for x in line.split(",")]

    target = 800708

    sol = Solution()

    print(sol.numSubseq(nums, target))
    SimpleProfiler.print_stats()
