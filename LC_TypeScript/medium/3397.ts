import assert from "node:assert";

function maxDistinctElements(nums: number[], k: number): number {
    nums = nums.sort((n1, n2) => n1 - n2);
    let threshold = nums[0] - k;
    let ans = 1;

    for (let idx = 1; idx < nums.length; idx++) {
        if (Math.abs(nums[idx] - threshold - 1) <= k) {
            threshold += 1;
            ans += 1;
        } else if (threshold + 1 < nums[idx] - k) {
            threshold = nums[idx] - k;
            ans += 1;
        }
    }

    return ans;
}

// Test case 1
const nums1 = [1, 2, 2, 3, 3, 4];
const k1 = 2;
assert.strictEqual(maxDistinctElements(nums1, k1), 6);

// Test case 2
const nums2 = [4, 4, 4, 4];
const k2 = 1;
assert.strictEqual(maxDistinctElements(nums2, k2), 3);

console.log("✅ All test cases passed!");
