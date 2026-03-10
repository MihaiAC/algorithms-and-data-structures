import assert from "node:assert";

const MODN = 1000000007n;

function concatenatedBinary(n: number): number {
    let ans = 0n;
    let len = 0n;
    let nextPow2 = 1;

    for (let num = 1; num <= n; num++) {
        if (num === nextPow2) {
            len += 1n;
            nextPow2 *= 2;
        }

        ans = ((ans << len) + BigInt(num)) % MODN;
    }

    return Number(ans);
}

assert.equal(concatenatedBinary(1), 1);
assert.equal(concatenatedBinary(3), 27);
assert.equal(concatenatedBinary(12), 505379714);
assert.equal(concatenatedBinary(42), 727837408);
assert.equal(concatenatedBinary(86401), 612546858);
