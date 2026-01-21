import assert from "node:assert";

function minBitwiseArray(nums: number[]): number[] {
    const ans = [];

    for (const num of nums) {
        let num_ii = -1;
        let digit = 1;

        while ((num & digit) !== 0) {
            num_ii = num - digit;
            digit <<= 1;
        }

        ans.push(num_ii);
    }

    return ans;
}

const nums1 = [2, 3, 5, 7];
const ans1 = [-1, 1, 4, 3];
assert.deepStrictEqual(ans1, minBitwiseArray(nums1));
