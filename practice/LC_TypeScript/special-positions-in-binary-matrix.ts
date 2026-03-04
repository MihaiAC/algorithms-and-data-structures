import assert from "node:assert";

function numSpecial(mat: number[][]): number {
    let ans = 0;

    const M = mat.length;
    const N = mat[0].length;

    const rowSums = new Array<number>(M).fill(0);
    const colSums = new Array<number>(N).fill(0);

    for (let ii = 0; ii < M; ii++) {
        for (let jj = 0; jj < N; jj++) {
            rowSums[ii] += mat[ii][jj];
            colSums[jj] += mat[ii][jj];
        }
    }

    for (let ii = 0; ii < M; ii++) {
        for (let jj = 0; jj < N; jj++) {
            if (mat[ii][jj] === 1 && rowSums[ii] === 1 && colSums[jj] === 1) ans += 1;
        }
    }

    return ans;
}

assert.equal(
    numSpecial([
        [1, 0, 0],
        [0, 0, 1],
        [1, 0, 0],
    ]),
    1
);

assert.equal(
    numSpecial([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
    ]),
    3
);
