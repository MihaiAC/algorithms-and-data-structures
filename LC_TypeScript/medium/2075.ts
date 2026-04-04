import assert from "node:assert";

function decodeCiphertext(encodedText: string, nRows: number): string {
    let ans = [];
    const N = encodedText.length;
    const nCols = Math.ceil(N / nRows);

    for (let startCol = 0; startCol < nCols; startCol++) {
        let [row, col] = [0, startCol];
        while (row < nRows && col < nCols) {
            ans.push(encodedText[row * nCols + col]);
            row++;
            col++;
        }
    }

    return ans.join("").trimEnd();
}

assert.equal(decodeCiphertext("ch   ie   pr", 3), "cipher");
assert.equal(decodeCiphertext("iveo    eed   l te   olc", 4), "i love leetcode");
assert.equal(decodeCiphertext("coding", 1), "coding");
