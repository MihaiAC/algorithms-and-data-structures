import assert from "node:assert";

function findTheString(lcp: number[][]): string {
    const N = lcp.length;
    const ans = new Array<string>(N).fill("");
    let currCode = "a".charCodeAt(0);

    for (let ii = 0; ii < N; ii++) {
        if (ans[ii] !== "") continue;
        const letter = String.fromCharCode(currCode);

        ans[ii] = letter;
        for (let jj = ii + 1; jj < N; jj++) {
            if (lcp[ii][jj] > 0) ans[jj] = letter;
        }

        currCode += 1;
    }

    for (let ii = N - 1; ii >= 0; ii--) {
        for (let jj = N - 1; jj >= 0; jj--) {
            if (ans[ii] === ans[jj]) {
                if (ii !== N - 1 && jj !== N - 1) {
                    if (lcp[ii][jj] !== lcp[ii + 1][jj + 1] + 1) return "";
                } else if (lcp[ii][jj] !== 1) return "";
            } else if (lcp[ii][jj] !== 0) return "";
        }
    }

    return ans.join("");
}

assert.equal(
    findTheString([
        [4, 0, 2, 0],
        [0, 3, 0, 1],
        [2, 0, 2, 0],
        [0, 1, 0, 1],
    ]),
    "abab"
);

assert.equal(
    findTheString([
        [4, 3, 2, 1],
        [3, 3, 2, 1],
        [2, 2, 2, 1],
        [1, 1, 1, 1],
    ]),
    "aaaa"
);
