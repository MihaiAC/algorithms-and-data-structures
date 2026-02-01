import assert from "node:assert";

function minimumCost(nums: number[]): number {
    let rightMin = nums.at(-1)!;
    let minCost = nums.at(-1)! + nums.at(-2)!;

    for (let idx = nums.length - 2; idx >= 1; idx--) {
        minCost = Math.min(minCost, nums[idx] + rightMin);
        rightMin = Math.min(rightMin, nums[idx]);
    }

    return minCost + nums[0]!;
}

assert.equal(minimumCost([1, 2, 3, 12]), 6);
assert.equal(minimumCost([5, 4, 3]), 12);
assert.equal(minimumCost([10, 3, 1, 1]), 12);
