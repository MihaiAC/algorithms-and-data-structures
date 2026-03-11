import assert from "node:assert";

function minOperations(s: string): number {
    let currNum = [0, 1];
    let currOps = [0, 0];

    for (const letter of s) {
        for (let idx = 0; idx <= 1; idx++) {
            if (String(currNum[idx]) !== letter) currOps[idx]++;
            currNum[idx] = 1 - currNum[idx];
        }
    }

    return Math.min(...currOps);
}

assert.equal(minOperations("0100"), 1);
assert.equal(minOperations("10"), 0);
assert.equal(minOperations("1111"), 2);
