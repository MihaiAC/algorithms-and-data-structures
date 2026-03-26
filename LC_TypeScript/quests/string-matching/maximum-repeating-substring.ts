import assert from "node:assert";

function maxRepeating(sequence: string, word: string): number {
    if (!sequence.includes(word)) return 0;

    let currWord = word;
    while (sequence.includes(currWord)) {
        currWord += word;
    }

    return Math.floor(currWord.length / word.length) - 1;
}

assert.equal(maxRepeating("ababc", "ab"), 2);
assert.equal(maxRepeating("ababc", "ba"), 1);
assert.equal(maxRepeating("ababc", "ac"), 0);
