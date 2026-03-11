import assert from "node:assert";

function findMaxConsecutiveOnes(nums: number[]): number {
    let ans = 0,
        curr = 0;

    for (let index = 0; index < nums.length; index++) {
        if (nums[index] === 1) {
            curr += 1;
        } else {
            ans = Math.max(ans, curr);
            curr = 0;
        }
    }

    return Math.max(ans, curr);
}

const nums1 = [1, 1, 0, 1, 1, 1];
assert.equal(findMaxConsecutiveOnes(nums1), 3);
