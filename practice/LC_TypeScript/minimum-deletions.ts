import assert from "node:assert";

function minimumDeletions(s: string): number {
    let numA = Array.from(s).reduce(
        (accum, letter) => accum + (letter === "a" ? 1 : 0),
        0
    );

    let numB = s.length - numA;
    let minDeletions = numA;
    let currB = 0;

    for (let currIdx = 0; currIdx < s.length; currIdx++) {
        currB += s[currIdx] === "b" ? 1 : 0;
        minDeletions = Math.min(minDeletions, 2 * currB + numA - currIdx - 1);
    }

    return minDeletions;
}

assert.equal(minimumDeletions("aababbab"), 2);
assert.equal(minimumDeletions("bbaaaaabb"), 2);
