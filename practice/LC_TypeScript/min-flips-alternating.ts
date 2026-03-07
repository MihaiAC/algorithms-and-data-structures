import assert from "node:assert";

function dumbMinFlips(s: string): number {
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

function minFlips(s: string): number {
    if (s.length === 1) return 0;
    if (s[0] === s.at(-1)) return dumbMinFlips(s);

    let firstIdx = -1;
    for (let idx = 0; idx < s.length - 1; idx++) {
        if (s[idx] === s[idx + 1]) {
            firstIdx = idx;
            break;
        }
    }
    if (firstIdx === -1) return 0;

    return Math.min(
        dumbMinFlips(s.slice(firstIdx + 1) + s.slice(0, firstIdx + 1)),
        dumbMinFlips(s)
    );
}

assert.equal(minFlips("111000"), 2);
assert.equal(minFlips("010"), 0);
assert.equal(minFlips("1110"), 1);
assert.equal(minFlips("10001100101000000"), 5);
