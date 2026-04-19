import assert from "node:assert";

function maxDistance(nums1: number[], nums2: number[]): number {
    const [n1, n2] = [nums1.length, nums2.length];
    let ans = 0;
    let jj = 0;

    for (let ii = 0; ii < n1; ii++) {
        while (jj < n2 && nums1[ii] <= nums2[jj]) {
            jj += 1;
        }

        if (ii <= jj - 1 && nums1[ii] <= nums2[jj - 1]) {
            ans = Math.max(ans, jj - ii - 1);
        }
    }

    return ans;
}

assert.equal(maxDistance([55, 30, 5, 4, 2], [100, 20, 10, 10, 5]), 2);
assert.equal(maxDistance([2, 2, 2], [10, 10, 1]), 1);
assert.equal(maxDistance([30, 29, 19, 5], [25, 25, 25, 25, 25]), 2);
