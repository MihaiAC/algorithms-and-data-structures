import assert from "node:assert";

function mirrorDistance(n: number): number {
    const revN = parseInt(Array.from(n.toString()).reverse().join(""), 10);
    return Math.abs(n - revN);
}

assert.equal(mirrorDistance(25), 27);
assert.equal(mirrorDistance(10), 9);
assert.equal(mirrorDistance(7), 0);
