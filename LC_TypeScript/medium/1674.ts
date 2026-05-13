import assert from "node:assert";

function minMoves(nums: number[], limit: number): number {
    const N = nums.length;
    const ops = new Array<number>(2 * limit + 1).fill(0);

    let [a, b] = [0, 0];
    for (let idx = 0; idx < Math.floor(nums.length / 2); idx++) {
        [a, b] = [
            Math.min(nums[idx], nums[N - idx - 1]),
            Math.max(nums[idx], nums[N - idx - 1]),
        ];

        ops[2] += 2;
        ops[a + 1] -= 1;
        ops[a + b] -= 1;
        ops[a + b + 1] += 1;
        ops[b + limit + 1] += 1;
    }

    let [minOps, currOps] = [N, 0];
    for (let target = 2; target <= 2 * limit; target++) {
        currOps += ops[target];
        if (minOps > currOps) minOps = currOps;
    }

    return minOps;
}

assert.equal(minMoves([1, 2, 4, 3], 4), 1);
assert.equal(minMoves([1, 2, 2, 1], 2), 2);
assert.equal(minMoves([1, 2, 1, 2], 2), 0);
