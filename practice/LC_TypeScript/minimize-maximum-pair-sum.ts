import assert from "node:assert";

function minPairSum(nums: number[]): number {
    nums.sort((a, b) => a - b);

    let maxSum = 0;
    const N = nums.length;
    for (let ii = 0; ii < Math.floor(N / 2); ii++) {
        maxSum = Math.max(maxSum, nums[ii] + nums[N - ii - 1]);
    }

    return maxSum;
}

assert.equal(minPairSum([3, 5, 2, 3]), 7);
assert.equal(minPairSum([3, 5, 4, 2, 4, 6]), 8);
