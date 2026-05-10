import assert from "node:assert";

function maximumJumps(nums: number[], target: number): number {
    const N = nums.length;

    const dp = new Array<number>(N).fill(0);
    dp[N - 1] = 1;

    for (let ii = N - 2; ii >= 0; ii--) {
        let currMax = 0;
        for (let jj = ii + 1; jj < N; jj++) {
            if (Math.abs(nums[jj] - nums[ii]) <= target) {
                currMax = Math.max(currMax, dp[jj]);
            }
        }

        dp[ii] = currMax == 0 ? 0 : currMax + 1;
    }

    return dp[0] - 1;
}

assert.equal(maximumJumps([1, 3, 6, 4, 1, 2], 2), 3);
assert.equal(maximumJumps([1, 3, 6, 4, 1, 2], 3), 5);
assert.equal(maximumJumps([1, 3, 6, 4, 1, 2], 0), -1);
