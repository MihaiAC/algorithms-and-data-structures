import assert from "node:assert";

function minimumCost(cost: number[]): number {
    cost.sort((a, b) => a - b);

    let ans = 0;
    for (let idx = cost.length - 1; idx >= 0; idx -= 3) {
        ans += cost[idx];
        if (idx - 1 >= 0) ans += cost[idx - 1];
    }

    return ans;
}

assert.equal(minimumCost([1, 2, 3]), 5);
assert.equal(minimumCost([6, 5, 7, 9, 2, 2]), 23);
assert.equal(minimumCost([5, 5]), 10);
