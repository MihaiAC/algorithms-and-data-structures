import assert from "node:assert";

function constructTransformedArray(nums: number[]): number[] {
    const N = nums.length;
    const res: number[] = Array.from({ length: N }, () => 0);

    for (let idx = 0; idx < N; idx++) {
        let newIdx = (idx + nums[idx]) % N;
        if (newIdx < 0) newIdx += N;

        res[idx] = nums[newIdx];
    }

    return res;
}

const nums1 = [3, -2, 1, 1];
const res1 = [1, 1, 1, 3];
assert.deepEqual(constructTransformedArray(nums1), res1);

const nums2 = [-1, 4, -1];
const res2 = [-1, -1, 4];
assert.deepEqual(constructTransformedArray(nums2), res2);
