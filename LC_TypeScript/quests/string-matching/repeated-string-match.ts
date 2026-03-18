import assert from "node:assert";

function repeatedStringMatch(a: string, b: string): number {
    let repeated = a;
    let count = 1;

    while (repeated.length < b.length) {
        repeated += a;
        count++;
    }

    if (repeated.includes(b)) return count;

    repeated += a;
    count++;

    if (repeated.includes(b)) return count;

    return -1;
}

assert.equal(repeatedStringMatch("abcd", "cdabcdab"), 3);
assert.equal(repeatedStringMatch("a", "aa"), 2);
