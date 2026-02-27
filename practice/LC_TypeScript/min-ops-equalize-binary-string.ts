import assert from "node:assert";

function minOperations(s: string, k: number): number {
    const N = s.length;
    const nZeros = Array.from(s).reduce(
        (accum, curr) => accum + (curr === "0" ? 1 : 0),
        0
    );

    if (nZeros === 0) return 0;
    if (N === k) {
        if (nZeros === N) return 1;
        if (nZeros === 0) return 0;
        return -1;
    }

    let ans = Infinity;

    if (k % 2 === nZeros % 2) {
        let ops = Math.max(Math.ceil(nZeros / k), Math.ceil((N - nZeros) / (N - k)));
        if (ops % 2 === 0) ops++;
        ans = Math.min(ans, ops);
    }

    if (nZeros % 2 === 0) {
        let ops = Math.max(Math.ceil(nZeros / k), Math.ceil(nZeros / (N - k)));
        if (ops % 2 === 1) ops++;
        ans = Math.min(ans, ops);
    }

    return ans === Infinity ? -1 : ans;
}

assert.equal(minOperations("101", 2), -1);
assert.equal(minOperations("0101", 3), 2);
assert.equal(minOperations("110", 1), 1);
