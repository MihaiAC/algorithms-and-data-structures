import assert from "node:assert";

function largestMagicSquare(grid: number[][]): number {
    const M = grid.length;
    const N = grid[0]!.length;

    const check = (ii: number, jj: number, side: number) => {
        const theSum = grid[ii]!.slice(jj, jj + side).reduce(
            (x: number, accum: number) => x + accum,
            0
        );

        // Check columns
        for (let col = jj; col < jj + side; col++) {
            let rowSum = 0;
            for (let row = ii; row < ii + side; row++) {
                rowSum += grid[row]![col]!;
            }
            if (rowSum !== theSum) return false;
        }

        // Check rows
        for (let row = ii; row < ii + side; row++) {
            const colSum = grid[row]!.slice(jj, jj + side).reduce(
                (x: number, accum: number) => x + accum,
                0
            );
            if (colSum !== theSum) return false;
        }

        // Check diagonals
        let diagOne = 0;
        let diagTwo = 0;
        for (let delta = 0; delta < side; delta++) {
            diagOne += grid[ii + delta]![jj + delta]!;
            diagTwo += grid[ii + delta]![jj + side - 1 - delta]!;
        }
        if (diagOne !== theSum) return false;
        if (diagTwo !== theSum) return false;

        return true;
    };

    for (let side = Math.min(M, N); side > 1; side--) {
        for (let ii = 0; ii <= M - side; ii++) {
            for (let jj = 0; jj <= N - side; jj++) {
                if (check(ii, jj, side)) return side;
            }
        }
    }

    return 1;
}

const grid = [
    [5, 1, 3, 1],
    [9, 3, 3, 1],
    [1, 3, 3, 8],
];
assert.equal(largestMagicSquare(grid), 2);
