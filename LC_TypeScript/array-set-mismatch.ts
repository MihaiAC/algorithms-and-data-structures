import assert from "node:assert";

function findErrorNums(nums: number[]): number[] {
    const N = nums.length;
    const S1 = Math.floor((N * (N + 1)) / 2);
    const S2 = Math.floor((N * (N + 1) * (2 * N + 1)) / 6);

    const v1 = nums.reduce((accum, curr) => accum + curr, 0);
    const v2 = nums.reduce((accum, curr) => accum + curr * curr, 0);

    const duplicate = Math.floor((v1 - S1 + (v2 - S2) / (v1 - S1)) / 2);
    const missing = Math.floor(((v2 - S2) / (v1 - S1) - v1 + S1) / 2);

    return [duplicate, missing];
}

const nums1 = [1, 2, 2, 4];
assert.deepEqual([2, 3], findErrorNums(nums1));

const nums2 = [1, 1];
assert.deepEqual([1, 2], findErrorNums(nums2));
