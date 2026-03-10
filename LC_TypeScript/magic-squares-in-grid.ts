import assert from "node:assert";

function numMagicSquaresInside(grid: number[][]): number {
    const [M, N] = [grid.length, grid[0]!.length];

    let count = 0;
    for (let ii = 0; ii < M - 2; ii++) {
        for (let jj = 0; jj < N - 2; jj++) {
            // Check that all numbers in subgrid are different + within [1, 9]
            const nums = [0, 1, 2].flatMap((dx) =>
                [0, 1, 2].map((dy) => grid[ii + dx][jj + dy])
            );

            const numsSet = new Set(nums);
            if (nums.filter((x) => x >= 1 && x <= 9).length !== 9 || numsSet.size !== 9)
                continue;

            const currSum = grid[ii][jj] + grid[ii][jj + 1] + grid[ii][jj + 2];

            const row2 = grid[ii + 1][jj] + grid[ii + 1][jj + 1] + grid[ii + 1][jj + 2];
            const row3 = grid[ii + 2][jj] + grid[ii + 2][jj + 1] + grid[ii + 2][jj + 2];

            if (row2 !== currSum || row3 !== currSum) continue;

            const col1 = grid[ii][jj] + grid[ii + 1][jj] + grid[ii + 2][jj];
            const col2 = grid[ii][jj + 1] + grid[ii + 1][jj + 1] + grid[ii + 2][jj + 1];
            const col3 = grid[ii][jj + 2] + grid[ii + 1][jj + 2] + grid[ii + 2][jj + 2];

            if (col1 !== currSum || col2 !== currSum || col3 !== currSum) continue;

            const diag1 = grid[ii][jj] + grid[ii + 1][jj + 1] + grid[ii + 2][jj + 2];
            const diag2 = grid[ii + 2][jj] + grid[ii + 1][jj + 1] + grid[ii][jj + 2];

            if (diag1 !== currSum || diag2 !== currSum) continue;

            count += 1;
        }
    }

    return count;
}

assert.equal(
    numMagicSquaresInside([
        [4, 3, 8, 4],
        [9, 5, 1, 9],
        [2, 7, 6, 2],
    ]),
    1
);

assert.equal(
    numMagicSquaresInside([
        [5, 5, 5],
        [5, 5, 5],
        [5, 5, 5],
    ]),
    0
);
