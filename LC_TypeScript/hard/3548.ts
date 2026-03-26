import _ from "lodash";
import assert from "node:assert";

function canPartitionHorizontally(grid: number[][], totalSum: number): boolean {
    const [M, N] = [grid.length, grid[0].length];
    if (M === 1) return false;

    let currSum = 0;
    const prevVals = new Set<number>();

    const processRow = (nrow: number): number => {
        let rowSum = 0;
        for (let jj = 0; jj < N; jj++) {
            rowSum += grid[nrow][jj];
            prevVals.add(grid[nrow][jj]);
        }

        return rowSum;
    };

    currSum += processRow(0);
    totalSum -= currSum;
    if (
        currSum === totalSum ||
        currSum - grid[0][0] === totalSum ||
        currSum - grid[0][N - 1] === totalSum
    )
        return true;

    for (let ii = 1; ii < M; ii++) {
        const rowSum = processRow(ii);
        currSum += rowSum;
        totalSum -= rowSum;

        if (currSum === totalSum) return true;
        if (N === 1) {
            if (currSum - grid[0][0] === totalSum || currSum - grid[ii][0] === totalSum)
                return true;
        } else if (prevVals.has(currSum - totalSum)) return true;
    }

    return false;
}

function rotate(grid: number[][]): number[][] {
    const [M, N] = [grid.length, grid[0].length];
    const rotated: number[][] = Array.from({ length: N }, () => new Array(M));

    for (let ii = 0; ii < M; ii++) {
        for (let jj = 0; jj < N; jj++) {
            rotated[jj][M - ii - 1] = grid[ii][jj];
        }
    }

    return rotated;
}

function canPartitionGrid(grid: number[][]): boolean {
    const totalSum = grid.reduce(
        (accum: number, currRow: number[]) => accum + _.sum(currRow),
        0
    );

    if (canPartitionHorizontally(grid, totalSum)) return true;
    for (let kk = 0; kk < 3; kk++) {
        grid = rotate(grid);
        if (canPartitionHorizontally(grid, totalSum)) return true;
    }

    return false;
}

assert.equal(
    canPartitionGrid([
        [1, 4],
        [2, 3],
    ]),
    true
);

assert.equal(
    canPartitionGrid([
        [1, 2],
        [3, 4],
    ]),
    true
);

assert.equal(
    canPartitionGrid([
        [1, 2, 4],
        [2, 3, 5],
    ]),
    false
);

assert.equal(
    canPartitionGrid([
        [4, 1, 8],
        [3, 2, 6],
    ]),
    false
);

assert.equal(canPartitionGrid([[10, 5, 4, 5]]), false);
