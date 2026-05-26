import assert from "node:assert";

function numberOfSpecialChars(word: string): number {
    const lower = new Set<string>();
    const upper = new Set<string>();

    for (const letter of word) {
        if (letter === letter.toLowerCase()) lower.add(letter);
        else upper.add(letter.toLowerCase());
    }

    let ans = 0;
    for (const letter of lower) {
        if (upper.has(letter)) ans += 1;
    }

    return ans;
}

assert.equal(numberOfSpecialChars("aaAbcBC"), 3);
assert.equal(numberOfSpecialChars("abc"), 0);
assert.equal(numberOfSpecialChars("abBCab"), 1);
