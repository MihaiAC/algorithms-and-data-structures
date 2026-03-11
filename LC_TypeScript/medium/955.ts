import assert from "node:assert";

function minDeletionSize(strs: string[]): number {
    const strLen = strs[0]!.length;

    const remaining = new Set();
    for (let idx = 0; idx < strLen; idx++) {
        remaining.add(idx);
    }

    // Every time we delete a position, just revalidate it all.
    // Probably could have done something smarter - if we keep the column,
    // compare future columns only if prev[idx] === curr[idx].
    let deletedPos = true;
    while (deletedPos && remaining.size > 0) {
        deletedPos = false;
        for (let strIdx = 0; strIdx < strs.length - 1; strIdx++) {
            const currStr = strs[strIdx];
            const nextStr = strs[strIdx + 1];
            let currPos = 0;

            while (currPos < strLen) {
                if (!remaining.has(currPos)) {
                    currPos += 1;
                    continue;
                }

                if (currStr[currPos] < nextStr[currPos]) {
                    break;
                } else if (currStr[currPos] === nextStr[currPos]) {
                    currPos += 1;
                } else {
                    remaining.delete(currPos);
                    deletedPos = true;
                    currPos += 1;
                }
            }
        }
    }

    return strLen - remaining.size;
}

assert.equal(minDeletionSize(["ca", "bb", "ac"]), 1);
assert.equal(minDeletionSize(["xc", "yb", "za"]), 0);
assert.equal(minDeletionSize(["zyx", "wvu", "tsr"]), 3);
assert.equal(minDeletionSize(["vdy", "vei", "zvc", "zld"]), 2);
