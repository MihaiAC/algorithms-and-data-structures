import assert from "node:assert";

function bitwiseComplement(n: number): number {
    return parseInt(
        Array.from(n.toString(2))
            .map((c) => (c === "0" ? "1" : "0"))
            .join(""),
        2
    );
}

assert.equal(bitwiseComplement(5), 2);
assert.equal(bitwiseComplement(7), 0);
assert.equal(bitwiseComplement(10), 5);
