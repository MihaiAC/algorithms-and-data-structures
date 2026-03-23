import assert from "node:assert";

const MODN = BigInt(10 ** 9 + 7);

function maxProductPath(grid: number[][]): number {
    const [M, N] = [grid.length, grid[0].length];

    let maxDp: bigint[][] = new Array<bigint[]>(M)
        .fill([])
        .map(() => new Array<bigint>(N).fill(0n));
    let minDp: bigint[][] = new Array<bigint[]>(M)
        .fill([])
        .map(() => new Array<bigint>(N).fill(0n));

    maxDp[0][0] = minDp[0][0] = BigInt(grid[0][0]);
    for (let jj = 1; jj < N; jj++) {
        maxDp[0][jj] = minDp[0][jj] = BigInt(grid[0][jj]) * maxDp[0][jj - 1];
    }

    for (let ii = 1; ii < M; ii++) {
        maxDp[ii][0] = minDp[ii][0] = BigInt(grid[ii][0]) * maxDp[ii - 1][0];
    }

    for (let ii = 1; ii < M; ii++) {
        for (let jj = 1; jj < N; jj++) {
            const maxPrev =
                maxDp[ii][jj - 1] > maxDp[ii - 1][jj]
                    ? maxDp[ii][jj - 1]
                    : maxDp[ii - 1][jj];

            const minPrev =
                minDp[ii][jj - 1] < minDp[ii - 1][jj]
                    ? minDp[ii][jj - 1]
                    : minDp[ii - 1][jj];

            const curr = BigInt(grid[ii][jj]);
            if (curr >= 0n) {
                maxDp[ii][jj] = maxPrev * curr;
                minDp[ii][jj] = minPrev * curr;
            } else {
                maxDp[ii][jj] = minPrev * curr;
                minDp[ii][jj] = maxPrev * curr;
            }
        }
    }

    return maxDp[M - 1][N - 1] < 0n ? -1 : Number(maxDp[M - 1][N - 1] % MODN);
}

assert.equal(
    maxProductPath([
        [-1, -2, -3],
        [-2, -3, -3],
        [-3, -3, -2],
    ]),
    -1
);

assert.equal(
    maxProductPath([
        [1, -2, 1],
        [1, -2, 1],
        [3, -4, 1],
    ]),
    8
);

assert.equal(
    maxProductPath([
        [1, 3],
        [0, -4],
    ]),
    0
);
