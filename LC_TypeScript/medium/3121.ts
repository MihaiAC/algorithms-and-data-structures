import assert from "node:assert";

function numberOfSpecialChars(word: string): number {
    const lastLower = new Map<string, number>();
    const firstUpper = new Map<string, number>();

    for (let idx = 0; idx < word.length; idx++) {
        const letter = word[idx];
        if (letter === letter.toLowerCase()) lastLower.set(letter, idx);
        else {
            firstUpper.set(
                letter.toLowerCase(),
                firstUpper.get(letter.toLowerCase()) ?? idx
            );
        }
    }

    let ans = 0;
    for (const letter of lastLower.keys()) {
        if (lastLower.get(letter)! < (firstUpper.get(letter) ?? -1)) {
            ans += 1;
        }
    }

    return ans;
}

assert.equal(numberOfSpecialChars("aaAbcBC"), 3);
assert.equal(numberOfSpecialChars("abc"), 0);
assert.equal(numberOfSpecialChars("AbBCab"), 0);
