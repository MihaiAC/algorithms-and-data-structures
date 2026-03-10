import assert from "node:assert";

function checkOnesSegment(s: string): boolean {
    return !s.includes("01");
}

assert.equal(checkOnesSegment("1001"), false);
assert.equal(checkOnesSegment("110"), true);
