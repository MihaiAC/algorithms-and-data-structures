import assert from "node:assert";

function repeatedSubstringPattern(s: string): boolean {
    if (s.length === 1) return false;

    // For all divisors of s.length, check if s = s[0:div]+.
    for (let divisor = 1; divisor <= Math.floor(s.length / 2); divisor++) {
        const pattern = new RegExp(`^(${s.slice(0, divisor)})+$`, "g");
        if (pattern.test(s)) return true;
    }

    return false;
}

assert.equal(repeatedSubstringPattern("abab"), true);
assert.equal(repeatedSubstringPattern("aba"), false);
assert.equal(repeatedSubstringPattern("abcabcabcabc"), true);
assert.equal(repeatedSubstringPattern("a"), false);
