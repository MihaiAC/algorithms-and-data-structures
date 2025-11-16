import assert from "node:assert";

const MODN = 1e9 + 7;

function numSub(s: string): number {
    return (
        s
            .split("0")
            .filter((x) => x !== "")
            .map((x) => x.length)
            .reduce((prev, curr) => prev + Math.floor((curr * (curr + 1)) / 2), 0) % MODN
    );
}

const s1 = "0110111";
assert.equal(numSub(s1), 9);

const s2 = "111111";
assert.equal(numSub(s2), 21);
