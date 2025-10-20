import assert from "node:assert";

function finalValueAfterOperations(operations: string[]): number {
    let ans = 0;
    for (const op of operations) {
        if (op.includes("++")) {
            ans += 1;
        } else {
            ans -= 1;
        }
    }

    return ans;
}

// Test cases
const op1 = ["--X", "X++", "X++"];
assert.strictEqual(finalValueAfterOperations(op1), 1);

const op2 = ["++X", "++X", "X++"];
assert.strictEqual(finalValueAfterOperations(op2), 3);

const op3 = ["X++", "++X", "--X", "X--"];
assert.strictEqual(finalValueAfterOperations(op3), 0);

console.log("✅ All test cases passed!");
