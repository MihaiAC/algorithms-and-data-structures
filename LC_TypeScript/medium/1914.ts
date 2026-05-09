import { Queue } from "datastructures-js";
import assert from "node:assert";

function rotateQueue(queue: Queue<number>, k: number) {
    for (let idx = 0; idx < k % queue.size(); idx++) {
        const front = queue.dequeue()!;
        queue.enqueue(front);
    }
}

/**
 * Rotate grid layer that starts at (x, x) k times.
 * @param grid
 * @param x
 * @param k
 */
function rotateLayer(grid: number[][], x: number, k: number) {
    const queue = new Queue<number>();
    const [M, N] = [grid.length, grid[0].length];

    for (let jj = x; jj < N - x - 1; jj++) {
        queue.enqueue(grid[x][jj]);
    }

    for (let ii = x; ii < M - x - 1; ii++) {
        queue.enqueue(grid[ii][N - x - 1]);
    }

    for (let jj = N - x - 1; jj > x; jj--) {
        queue.enqueue(grid[M - x - 1][jj]);
    }

    for (let ii = M - x - 1; ii > x; ii--) {
        queue.enqueue(grid[ii][x]);
    }

    rotateQueue(queue, k);
    for (let jj = x; jj < N - x - 1; jj++) {
        grid[x][jj] = queue.dequeue()!;
    }

    for (let ii = x; ii < M - x - 1; ii++) {
        grid[ii][N - x - 1] = queue.dequeue()!;
    }

    for (let jj = N - x - 1; jj > x; jj--) {
        grid[M - x - 1][jj] = queue.dequeue()!;
    }

    for (let ii = M - x - 1; ii > x; ii--) {
        grid[ii][x] = queue.dequeue()!;
    }
}

function rotateGrid(grid: number[][], k: number): number[][] {
    const [M, N] = [grid.length, grid[0].length];
    for (let x = 0; x < Math.floor(Math.min(M, N) / 2); x++) {
        rotateLayer(grid, x, k);
    }

    return grid;
}

assert.deepEqual(
    rotateGrid(
        [
            [40, 10],
            [30, 20],
        ],
        1
    ),
    [
        [10, 20],
        [40, 30],
    ]
);

assert.deepEqual(
    rotateGrid(
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
        ],
        2
    ),
    [
        [3, 4, 8, 12],
        [2, 11, 10, 16],
        [1, 7, 6, 15],
        [5, 9, 13, 14],
    ]
);
