import assert from "node:assert";

function leftRightDifference(nums: number[]): number[] {
    const N = nums.length;

    let ans = [];
    let currSum = 0;

    for (let idx = 0; idx < N; idx++) {
        ans.push(currSum);
        currSum += nums[idx];
    }

    currSum = 0;
    for (let idx = N - 1; idx >= 0; idx--) {
        ans[idx] = Math.abs(ans[idx] - currSum);
        currSum += nums[idx];
    }

    return ans;
}

assert.deepEqual(leftRightDifference([10, 4, 8, 3]), [15, 1, 11, 22]);
assert.deepEqual(leftRightDifference([1]), [0]);
