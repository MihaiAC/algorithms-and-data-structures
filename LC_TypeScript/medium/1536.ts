import assert from "node:assert";

function minSwaps(grid: number[][]): number {
    const N = grid.length;
    const lastOne = new Array<number>(N).fill(-1);

    // Pre-compute the index of the last '1' for each row.
    for (let ii = 0; ii < N; ii++) {
        for (let jj = N - 1; jj >= 0; jj--) {
            if (grid[ii][jj] === 1) {
                lastOne[ii] = jj;
                break;
            }
        }
    }

    // Top -> bottom choose what row to swap.
    let nSwaps = 0;
    for (let ii = 0; ii < N; ii++) {
        let kk = -1;
        for (let jj = ii; jj < N; jj++) {
            if (lastOne[jj] <= ii) {
                nSwaps += jj - ii;
                kk = jj;
                break;
            }
        }

        if (kk === -1) return -1;

        for (let jj = kk; jj > ii; jj--) {
            [lastOne[jj], lastOne[jj - 1]] = [lastOne[jj - 1], lastOne[jj]];
        }
    }

    return nSwaps;
}

assert.equal(
    minSwaps([
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 1, 1, 0],
    ]),
    -1
);

assert.equal(
    minSwaps([
        [0, 0, 1],
        [1, 1, 0],
        [1, 0, 0],
    ]),
    3
);

assert.equal(
    minSwaps([
        [1, 0, 0],
        [1, 1, 0],
        [1, 1, 1],
    ]),
    0
);
