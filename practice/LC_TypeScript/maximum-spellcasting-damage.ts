import assert from "node:assert";

function maximumTotalDamage(power: number[]): number {
    const counter = new Map();
    power.forEach((val) => {
        if (!counter.has(val)) {
            counter.set(val, 1);
        } else {
            counter.set(val, counter.get(val) + 1);
        }
    });

    let keys = Array.from(counter.keys());
    keys.sort((a, b) => a - b);

    let spells = [[-3, 0]];
    keys.forEach((key) => spells.push([key, counter.get(key)]));

    let currMax = 0;
    let maxDamageVals = [0];
    let prevIdx = 0;

    for (let ii = 1; ii < spells.length; ii++) {
        while (prevIdx < ii && spells[prevIdx][0] < spells[ii][0] - 2) {
            currMax = Math.max(currMax, maxDamageVals[prevIdx]);
            prevIdx += 1;
        }

        maxDamageVals.push(currMax + spells[ii][0] * spells[ii][1]);
    }

    return Math.max(...maxDamageVals);
}

// Test case 1
const power1 = [1, 1, 3, 4];
assert.strictEqual(maximumTotalDamage(power1), 6);

// Test case 2
const power2 = [7, 1, 6, 6];
assert.strictEqual(maximumTotalDamage(power2), 13);

console.log("✅ All test cases passed!");
