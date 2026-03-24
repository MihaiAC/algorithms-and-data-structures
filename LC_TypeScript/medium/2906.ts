import assert from "node:assert";

const MODN = 12345;

function constructProductMatrix(grid: number[][]): number[][] {
    const [M, N] = [grid.length, grid[0].length];

    for (let ii = 0; ii < M; ii++) {
        for (let jj = 0; jj < N; jj++) {
            grid[ii][jj] = grid[ii][jj] % MODN;
        }
    }

    const suffixProd = new Array<number[]>(M)
        .fill([])
        .map(() => new Array<number>(N).fill(1));
    for (let ii = M - 1; ii >= 0; ii--) {
        if (ii !== M - 1)
            suffixProd[ii][N - 1] = (grid[ii][N - 1] * suffixProd[ii + 1][0]) % MODN;
        else suffixProd[ii][N - 1] = grid[M - 1][N - 1];
        for (let jj = N - 2; jj >= 0; jj--) {
            suffixProd[ii][jj] = (grid[ii][jj] * suffixProd[ii][jj + 1]) % MODN;
        }
    }

    let currPrefixProd = 1;
    for (let ii = 0; ii < M; ii++) {
        for (let jj = 0; jj < N; jj++) {
            let currSuffixProd = 1;
            if (jj < N - 1) currSuffixProd = suffixProd[ii][jj + 1];
            else if (ii < M - 1) currSuffixProd = suffixProd[ii + 1][0];

            suffixProd[ii][jj] = (currPrefixProd * currSuffixProd) % MODN;
            currPrefixProd = (currPrefixProd * grid[ii][jj]) % MODN;
        }
    }

    return suffixProd;
}

assert.deepEqual(
    constructProductMatrix([
        [1, 2],
        [3, 4],
    ]),
    [
        [24, 12],
        [8, 6],
    ]
);

assert.deepEqual(constructProductMatrix([[12345], [2], [1]]), [[2], [0], [0]]);
assert.deepEqual(constructProductMatrix([[414750857], [449145368], [767292749]]), [
    [1462],
    [3103],
    [9436],
]);
