import assert from "node:assert";

function rotateString(s: string, goal: string): boolean {
    if (s.length !== goal.length) return false;
    return /^(\w+)(\w*)\2\1$/.test(s + goal);
}

assert.equal(rotateString("abcde", "cdeab"), true);
assert.equal(rotateString("abcde", "abced"), false);
assert.equal(rotateString("aaaa", "aa"), false);
assert.equal(rotateString("abcde", "abcde"), true);
