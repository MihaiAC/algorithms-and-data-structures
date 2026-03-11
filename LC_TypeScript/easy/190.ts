import assert from "node:assert";

function reverseBits(n: number): number {
    const nStr = n.toString(2).padStart(32, "0");
    const revStr = nStr.split("").reverse().join("");
    return parseInt(revStr, 2);
}

assert.equal(reverseBits(43261596), 964176192);
assert.equal(reverseBits(2147483644), 1073741822);
