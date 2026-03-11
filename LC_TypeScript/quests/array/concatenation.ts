import assert from "node:assert";

function getConcatenation(nums: number[]): number[] {
    const N = nums.length;
    const ans = new Array(2 * N);

    for (let index = 0; index < N; index++) {
        ans[index] = nums[index];
        ans[N + index] = nums[index];
    }

    return ans;
}

// Test cases.
const nums1 = [1, 2, 1];
assert.deepEqual(getConcatenation(nums1), [1, 2, 1, 1, 2, 1]);
