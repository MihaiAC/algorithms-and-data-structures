import assert from "node:assert";

function hasAlternatingBits(n: number): boolean {
    const bin = n.toString(2);
    let curr = bin[0]!;
    for (let idx = 1; idx < bin.length; idx++) {
        if (bin[idx] === curr) return false;
        curr = bin[idx];
    }

    return true;
}

assert.equal(hasAlternatingBits(5), true);
assert.equal(hasAlternatingBits(7), false);
assert.equal(hasAlternatingBits(11), false);
