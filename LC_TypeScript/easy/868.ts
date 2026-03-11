import assert from "node:assert";

function binaryGap(n: number): number {
    const nStr = n.toString(2);
    let gap = 0;
    let lastIdx = -1;

    for (let idx = 0; idx < nStr.length; idx++) {
        if (nStr[idx] === "1") {
            if (lastIdx !== -1) {
                gap = Math.max(gap, idx - lastIdx);
            }

            lastIdx = idx;
        }
    }

    return gap;
}

assert.equal(binaryGap(22), 2);
assert.equal(binaryGap(8), 0);
assert.equal(binaryGap(5), 2);
