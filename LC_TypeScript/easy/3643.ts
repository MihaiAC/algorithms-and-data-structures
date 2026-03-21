import assert from "node:assert";

function reverseSubmatrix(grid: number[][], x: number, y: number, k: number): number[][] {
    for (let row = x; row < x + Math.floor(k / 2); row++) {
        const swapRow = x + k - 1 - (row - x);
        for (let col = y; col < y + k; col++) {
            [grid[row][col], grid[swapRow][col]] = [grid[swapRow][col], grid[row][col]];
        }
    }

    return grid;
}

assert.deepEqual(
    reverseSubmatrix(
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
        ],
        1,
        0,
        3
    ),
    [
        [1, 2, 3, 4],
        [13, 14, 15, 8],
        [9, 10, 11, 12],
        [5, 6, 7, 16],
    ]
);

assert.deepEqual(
    reverseSubmatrix(
        [
            [3, 4, 2, 3],
            [2, 3, 4, 2],
        ],
        0,
        2,
        2
    ),
    [
        [3, 4, 4, 2],
        [2, 3, 2, 3],
    ]
);
