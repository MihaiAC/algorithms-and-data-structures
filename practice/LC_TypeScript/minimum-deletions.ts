import assert from "node:assert";

function minimumDeletions(s: string): number {
    let numA = 0;
    let minDeletions = 0;
    let currB = 0;

    for (let currIdx = 0; currIdx < s.length; currIdx++) {
        if (s[currIdx] === "b") currB += 1;
        else numA += 1;
        minDeletions = Math.min(minDeletions, 2 * currB - currIdx - 1);
    }

    return minDeletions + numA;
}

assert.equal(minimumDeletions("aababbab"), 2);
assert.equal(minimumDeletions("bbaaaaabb"), 2);
