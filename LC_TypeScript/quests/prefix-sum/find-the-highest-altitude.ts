import assert from "node:assert";

function largestAltitude(gain: number[]): number {
    let ans = 0;
    let curr = 0;

    for (const dy of gain) {
        curr += dy;
        ans = Math.max(ans, curr);
    }

    return ans;
}

assert.equal(largestAltitude([-5, 1, 5, 0, -7]), 1);
assert.equal(largestAltitude([-4, -3, -2, -1, 4, 3, 2]), 0);
