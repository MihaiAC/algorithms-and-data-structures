import assert from "node:assert";

function minRemoval(nums: number[], k: number): number {
    const N = nums.length;
    nums.sort((a, b) => a - b);

    let rightIdx = 0;
    let ans = N;

    for (let leftIdx = 0; leftIdx < N; leftIdx++) {
        while (rightIdx < N && nums[rightIdx] <= nums[leftIdx] * k) {
            rightIdx++;
        }

        ans = Math.min(ans, N + leftIdx - rightIdx);
    }

    return ans;
}

assert.equal(minRemoval([2, 1, 5], 2), 1);
assert.equal(minRemoval([1, 6, 2, 9], 3), 2);
assert.equal(minRemoval([4, 6], 2), 0);
