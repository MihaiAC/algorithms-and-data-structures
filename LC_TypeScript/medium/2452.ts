import assert from "node:assert";

function twoEditWords(queries: string[], dictionary: string[]): string[] {
    let ans = [];
    outerloop: for (let query of queries) {
        for (let target of dictionary) {
            let diffs = 0;
            for (let idx = 0; idx < query.length; idx++) {
                if (query[idx] !== target[idx]) {
                    diffs += 1;
                    if (diffs > 2) {
                        continue;
                    }
                }
            }

            if (diffs <= 2) {
                ans.push(query);
                continue outerloop;
            }
        }
    }

    return ans;
}

assert.deepEqual(
    twoEditWords(["word", "note", "ants", "wood"], ["wood", "joke", "moat"]),
    ["word", "note", "wood"]
);

assert.deepEqual(twoEditWords(["yes"], ["not"]), []);
