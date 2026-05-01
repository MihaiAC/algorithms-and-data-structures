import assert from "node:assert";

function maxRotateFunction(nums: number[]): number {
    const N = nums.length;

    let sum = 0;
    let currSum = 0;

    for (let idx = 0; idx < N; idx++) {
        sum += nums[idx];
        currSum += idx * nums[idx];
    }

    let ans = currSum;
    for (let k = 1; k < N; k++) {
        currSum = currSum + sum - N * nums[N - k];
        ans = Math.max(ans, currSum);
    }

    return ans;
}

assert.equal(maxRotateFunction([4, 3, 2, 6]), 26);
assert.equal(maxRotateFunction([100]), 0);
