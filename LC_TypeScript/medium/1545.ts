import assert from "node:assert";

function findKthBit(n: number, k: number): string {
    const rec = (len: number, idx: number, inv: number): number => {
        if (len === 1) return inv;

        const prev_len = Math.floor((len - 1) / 2);

        if (idx === prev_len) return 1 - inv;
        else if (idx < prev_len) return rec(prev_len, idx, inv);
        else return rec(prev_len, 2 * prev_len - idx, 1 - inv);
    };

    return String(rec(2 ** n - 1, k - 1, 0));
}

assert.equal(findKthBit(3, 1), "0");
assert.equal(findKthBit(4, 11), "1");
