import assert from "node:assert";

function smallerNumbersThanCurrent(nums: number[]): number[] {
    const nums_idx = nums.map((x, idx) => [x, idx]).sort((x1, x2) => x1[0] - x2[0]);

    const ans = Array(nums.length).fill(0);
    let [prev, prev_idx] = [-1, -1];
    for (let idx = 0; idx < nums_idx.length; idx++) {
        const [elem, orig_idx] = nums_idx[idx];
        if (elem != prev) {
            prev = elem;
            prev_idx = idx;
            ans[orig_idx] = idx;
        } else {
            ans[orig_idx] = prev_idx;
        }
    }

    return ans;
}

const nums1 = [6, 5, 4, 8];
assert.deepEqual(smallerNumbersThanCurrent(nums1), [2, 1, 0, 3]);

const nums2 = [7, 7, 7, 7];
assert.deepEqual(smallerNumbersThanCurrent(nums2), [0, 0, 0, 0]);
