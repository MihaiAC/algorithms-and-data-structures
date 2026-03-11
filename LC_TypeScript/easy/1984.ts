import assert from "node:assert";

function minimumDifference(nums: number[], k: number): number {
    if (k === 1) return 0;
    nums.sort((a, b) => a - b);

    let ans = nums[nums.length - 1] - nums[0];
    for (let idx = 0; idx <= nums.length - k; idx++) {
        ans = Math.min(ans, nums[idx + k - 1] - nums[idx]);
    }

    return ans;
}

assert.equal(minimumDifference([9, 4, 1, 7], 2), 2);
