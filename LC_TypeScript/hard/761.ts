import assert from "node:assert";

function makeLargestSpecial(s: string): string {
    let count = 0;
    let idx = 0;
    const res = [];

    for (let jj = 0; jj < s.length; jj++) {
        if (s[jj] == "1") count += 1;
        else count -= 1;

        if (count === 0) {
            res.push("1" + makeLargestSpecial(s.slice(idx + 1, jj)) + "0");
            idx = jj + 1;
        }
    }

    res.sort((a, b) => {
        if (a < b) return 1;
        return -1;
    });

    return res.join("");
}

assert.equal(makeLargestSpecial("11011000"), "11100100");
assert.equal(makeLargestSpecial("10"), "10");
