import assert from "node:assert";

const BALONS = "balon";
const SINGLE = ["b", "a", "n"];
const DOUBLE = ["l", "o"];

function maxNumberOfBalloons(text: string): number {
    const counter = new Map<string, number>();

    for (const letter of text) {
        if (BALONS.includes(letter)) {
            counter.set(letter, (counter.get(letter) || 0) + 1);
        }
    }

    return Math.min(
        SINGLE.reduce(
            (min: number, letter: string): number =>
                Math.min(min, counter.get(letter) || 0),
            Infinity
        ),
        DOUBLE.reduce(
            (min: number, letter: string): number =>
                Math.min(min, Math.floor((counter.get(letter) || 0) / 2) || 0),
            Infinity
        )
    );
}

assert.equal(maxNumberOfBalloons("nlaebolko"), 1);
assert.equal(maxNumberOfBalloons("loonbalxballpoon"), 2);
assert.equal(maxNumberOfBalloons("leetcode"), 0);
