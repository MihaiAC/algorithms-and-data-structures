import assert from "node:assert";

function minDeletionSize(strs: string[]): number {
    let droppedCount = 0;
    const strLen = strs[0]!.length;

    // Initialise map.
    const map = new Map<number, string>(
        Array.from({ length: strLen }, (_, i) => [i, ""])
    );

    for (const str of strs) {
        for (const idx of map.keys()) {
            if (map.get(idx)! <= str.at(idx)!) {
                map.set(idx, str.at(idx)!);
            } else {
                map.delete(idx);
                droppedCount++;
            }
        }
    }

    return droppedCount;
}

assert.equal(minDeletionSize(["cba", "daf", "ghi"]), 1);
assert.equal(minDeletionSize(["zyx", "wvu", "tsr"]), 3);
