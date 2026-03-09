import assert from "node:assert";

const isLower = (char: string): boolean => char === char.toLowerCase();
const isUpper = (char: string): boolean => char === char.toUpperCase();

function detectCapitalUse(word: string): boolean {
    if (word.length === 1) return true;

    let restLower;
    if (isLower(word[0])) restLower = true;
    else if (isLower(word[1])) restLower = true;
    else restLower = false;

    const capCheck = restLower ? isLower : isUpper;
    return Array.from(word.slice(1)).every((char) => capCheck(char));
}

assert.equal(detectCapitalUse("USA"), true);
assert.equal(detectCapitalUse("FLaG"), false);
assert.equal(detectCapitalUse("lowercase"), true);
assert.equal(detectCapitalUse("uSA"), false);
