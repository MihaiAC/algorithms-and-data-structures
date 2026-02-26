import assert from "node:assert";

function numSteps(s: string): number {
    let carry = 0;
    let steps = 0;

    for (let idx = s.length - 1; idx > 0; idx--) {
        const num = parseInt(s[idx], 2);
        if (num !== carry) {
            steps += 2;
            carry = 1;
        } else {
            steps += 1;
        }
    }

    if (carry === 1) steps += 1;

    return steps;
}

assert.equal(numSteps("1101"), 6);
assert.equal(numSteps("10"), 1);
assert.equal(numSteps("1"), 0);
