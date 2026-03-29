import assert from "node:assert";

function firstMissingPositive(nums: number[]): number {
    const N = nums.length;
    const present = new Array<boolean>(N + 1).fill(false);

    for (const num of nums) {
        if (num > N || num < 0) continue;
        present[num] = true;
    }

    for (let idx = 1; idx <= N; idx++) {
        if (!present[idx]) return idx;
    }

    return N + 1;
}

assert.equal(firstMissingPositive([1, 2, 0]), 3);
assert.equal(firstMissingPositive([1, 2, 3]), 4);
assert.equal(firstMissingPositive([3, 4, -1, 1]), 2);
assert.equal(firstMissingPositive([7, 8, 9, 11, 12]), 1);
