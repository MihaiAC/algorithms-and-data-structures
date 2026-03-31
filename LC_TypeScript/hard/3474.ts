import assert from "node:assert";

function generateString(str1: string, str2: string): string {
    const [M, N] = [str1.length, str2.length];
    const ans = new Array(M + N - 1).fill("a");
    const fixed = new Array(M + N - 1).fill(false);

    // Handle 'T' entries.
    for (let ii = 0; ii < M; ii++) {
        if (str1[ii] === "F") continue;
        for (let jj = 0; jj < N; jj++) {
            const ansIdx = ii + jj;
            if (fixed[ansIdx]) {
                if (ans[ansIdx] !== str2[jj]) return "";
            } else {
                ans[ansIdx] = str2[jj];
                fixed[ansIdx] = true;
            }
        }
    }

    // Handle 'F' entries.
    // Transform rightmost non-fixed to 'a' or 'b'.
    for (let ii = 0; ii < M; ii++) {
        if (str1[ii] === "T") continue;
        let different = false;
        let rightmostIdx = -1;
        for (let jj = ii + N - 1; jj >= ii; jj--) {
            if (ans[jj] !== str2[jj - ii]) {
                different = true;
                break;
            } else if (rightmostIdx === -1 && !fixed[jj]) rightmostIdx = jj;
        }

        if (different) continue;
        if (rightmostIdx !== -1) ans[rightmostIdx] = "b";
        else return "";
    }

    return ans.join("");
}

assert.equal(generateString("TFTF", "ab"), "ababa");
assert.equal(generateString("TFTF", "abc"), "");
assert.equal(generateString("F", "d"), "a");
assert.equal(generateString("F", "acfcfc"), "aaaaaa");
