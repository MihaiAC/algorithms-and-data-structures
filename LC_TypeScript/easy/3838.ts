import assert from "node:assert";
import _ from "lodash";

const A_ASCII = "a".charCodeAt(0);

function letterToIdx(letter: string): number {
    return letter.charCodeAt(0) - A_ASCII;
}

function weightToRevLetter(weight: number): string {
    return String.fromCharCode(25 - (weight % 26) + A_ASCII);
}

function mapWordWeights(words: string[], weights: number[]): string {
    const wordWeights: number[] = words.map((word) =>
        _.sum([...word].map((letter) => weights[letterToIdx(letter)]))
    );

    return wordWeights.map((weight) => weightToRevLetter(weight)).join("");
}

assert.equal(
    mapWordWeights(
        ["abcd", "def", "xyz"],
        [5, 3, 12, 14, 1, 2, 3, 2, 10, 6, 6, 9, 7, 8, 7, 10, 8, 9, 6, 9, 9, 8, 3, 7, 7, 2]
    ),
    "rij"
);

assert.equal(
    mapWordWeights(
        ["a", "b", "c"],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ),
    "yyy"
);

assert.equal(
    mapWordWeights(
        ["abcd"],
        [7, 5, 3, 4, 3, 5, 4, 9, 4, 2, 2, 7, 10, 2, 5, 10, 6, 1, 2, 2, 4, 1, 3, 4, 4, 5]
    ),
    "g"
);
