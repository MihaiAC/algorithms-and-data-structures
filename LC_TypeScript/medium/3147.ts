import assert from "node:assert/strict";

function maximumEnergy(energy: number[], k: number): number {
    const modEnergy: number[] = [];
    energy.forEach((val, idx) => {
        const new_idx = idx % k;
        if (new_idx >= modEnergy.length) {
            modEnergy.push(val);
        } else {
            modEnergy[new_idx] = Math.max(val, val + modEnergy[new_idx]);
        }
    });

    return Math.max(...modEnergy);
}

// Test case 1
const energy1 = [5, 2, -10, -5, 1];
const k1 = 3;
assert.strictEqual(maximumEnergy(energy1, k1), 3);

// Test case 2
const energy2 = [-2, -3, -1];
const k2 = 2;
assert.strictEqual(maximumEnergy(energy2, k2), -1);

console.log("✅ All test cases passed!");
