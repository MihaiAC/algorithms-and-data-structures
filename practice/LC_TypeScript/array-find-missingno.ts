import assert from "node:assert";

function findDisappearedNumbers(nums: number[]): number[] {
    const setNums = new Set(nums);
    let ans = [];
    for (let num = 1; num <= nums.length; num++) {
        if (!setNums.has(num)) {
            ans.push(num);
        }
    }

    return ans;
}

const nums1 = [4, 3, 2, 7, 8, 2, 3, 1];
assert.deepEqual(findDisappearedNumbers(nums1), [5, 6]);
