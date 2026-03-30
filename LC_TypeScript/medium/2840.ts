import assert from "node:assert";

function letterToNum(letter: string): number {
    return letter.charCodeAt(0) - "a".charCodeAt(0);
}

function checkStrings(s1: string, s2: string): boolean {
    const freqEven = new Array(26).fill(0);
    const freqOdd = new Array(26).fill(0);

    const N = s1.length;

    for (let idx = 0; idx < N; idx++) {
        if (idx % 2 === 0) {
            freqEven[letterToNum(s1[idx])]++;
            freqEven[letterToNum(s2[idx])]--;
        } else {
            freqOdd[letterToNum(s1[idx])]++;
            freqOdd[letterToNum(s2[idx])]--;
        }
    }

    return freqEven.every((x) => x === 0) && freqOdd.every((x) => x === 0);
}

assert(checkStrings("abcdba", "cabdab"));
assert(!checkStrings("abe", "bea"));
