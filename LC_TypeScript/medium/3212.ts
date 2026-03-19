import assert from "node:assert";

type Freq = {
    nx: number;
    ny: number;
};

const DEFAULT_FREQ: Freq = {
    nx: 0,
    ny: 0,
};

const toKey = (x: number, y: number): string => `(${x}, ${y})`;

function numberOfSubmatrices(grid: string[][]): number {
    const [M, N] = [grid.length, grid[0].length];
    const dp = new Map<string, Freq>();

    let count = 0;
    for (let ii = 0; ii < M; ii++) {
        for (let jj = 0; jj < N; jj++) {
            const { nx: leftX, ny: leftY } = dp.get(toKey(ii, jj - 1)) ?? DEFAULT_FREQ;
            const { nx: topX, ny: topY } = dp.get(toKey(ii - 1, jj)) ?? DEFAULT_FREQ;
            const { nx: diagX, ny: diagY } =
                dp.get(toKey(ii - 1, jj - 1)) ?? DEFAULT_FREQ;

            const cx = leftX + topX - diagX + (grid[ii][jj] === "X" ? 1 : 0);
            const cy = leftY + topY - diagY + (grid[ii][jj] === "Y" ? 1 : 0);

            if (cx >= 1 && cx === cy) count += 1;

            dp.set(toKey(ii, jj), { nx: cx, ny: cy });
        }
    }

    return count;
}

assert.equal(
    numberOfSubmatrices([
        ["X", "Y", "."],
        ["Y", ".", "."],
    ]),
    3
);

assert.equal(
    numberOfSubmatrices([
        ["X", "X"],
        ["X", "Y"],
    ]),
    0
);

assert.equal(
    numberOfSubmatrices([
        [".", "."],
        [".", "."],
    ]),
    0
);
