import assert from "node:assert";

function minAbsDiff(grid: number[][], K: number): number[][] {
    const [M, N] = [grid.length, grid[0].length];
    const ans: number[][] = new Array<number[][]>(M - K + 1)
        .fill([])
        .map((_) => new Array<number>(N - K + 1).fill(0));

    for (let ii = 0; ii < M - K + 1; ii++) {
        for (let jj = 0; jj < N - K + 1; jj++) {
            const vals: number[] = [];
            for (let ii_kk = ii; ii_kk < ii + K; ii_kk++) {
                vals.push(...grid[ii_kk].slice(jj, jj + K));
            }

            if (vals.length === 1) continue;

            vals.sort((a, b) => a - b);
            let minVal: number | undefined;
            for (let idx = 0; idx < vals.length - 1; idx++) {
                if (vals[idx + 1] !== vals[idx]) {
                    if (minVal) minVal = Math.min(minVal, vals[idx + 1] - vals[idx]);
                    else minVal = vals[idx + 1] - vals[idx];
                }
            }

            ans[ii][jj] = minVal ?? 0;
        }
    }

    return ans;
}

assert.deepEqual(
    minAbsDiff(
        [
            [1, 8],
            [3, -2],
        ],
        2
    ),
    [[2]]
);

assert.deepEqual(minAbsDiff([[3, -1]], 1), [[0, 0]]);

assert.deepEqual(
    minAbsDiff(
        [
            [1, -2, 3],
            [2, 3, 5],
        ],
        2
    ),
    [[1, 2]]
);

assert.deepEqual(
    minAbsDiff(
        [
            [1, 1, 1],
            [1, 1, 1],
        ],
        2
    ),
    [[0, 0]]
);

assert.deepEqual(
    minAbsDiff(
        [
            [-88242, 79613],
            [-48040, 69929],
        ],
        2
    ),
    [[9684]]
);
