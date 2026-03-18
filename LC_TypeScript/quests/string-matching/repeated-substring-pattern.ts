import assert from "node:assert";

function repeatedSubstringPattern(s: string): boolean {
    return /^(\w+)\1{1,}$/.test(s);
}

assert.equal(repeatedSubstringPattern("abab"), true);
assert.equal(repeatedSubstringPattern("aba"), false);
assert.equal(repeatedSubstringPattern("abcabcabcabc"), true);
assert.equal(repeatedSubstringPattern("a"), false);
