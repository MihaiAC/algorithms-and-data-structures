import assert from "node:assert";

function addAtEnd(digit: string, num: number): number {
    return num * 2 + parseInt(digit);
}

function removeFromFront(digit: string, num: number, k: number): number {
    if (digit === "0") return num;
    return num - (1 << k);
}

function hasAllCodes(s: string, k: number): boolean {
    const nums = new Set<number>();
    let num = 0;

    for (let idx = 0; idx < Math.min(k, s.length); idx++) {
        num = addAtEnd(s[idx]!, num);
    }
    nums.add(num);

    for (let idx = Math.min(k, s.length); idx < s.length; idx++) {
        num = addAtEnd(s[idx]!, num);
        num = removeFromFront(s[idx - k]!, num, k);
        nums.add(num);
    }

    return nums.size === 1 << k;
}

assert.equal(hasAllCodes("00110110", 2), true);
assert.equal(hasAllCodes("0110", 1), true);
assert.equal(hasAllCodes("0110", 2), false);
