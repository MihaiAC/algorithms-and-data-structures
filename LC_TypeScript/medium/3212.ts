import assert from "node:assert";

const cond = (nx: number, ny: number): boolean => nx >= 1 && nx === ny;
const toNum = (val: string, ref: string): number => (val === ref ? 1 : 0);

function numberOfSubmatrices(grid: string[][]): number {
    const [M, N] = [grid.length, grid[0].length];
    let prevX: number[] = Array.from<number>({ length: N }).fill(0);
    let prevY: number[] = Array.from<number>({ length: N }).fill(0);

    let currX: number[] = Array.from<number>({ length: N }).fill(0);
    let currY: number[] = Array.from<number>({ length: N }).fill(0);

    let count = 0;
    for (let ii = 0; ii < M; ii++) {
        currX[0] = toNum(grid[ii][0], "X") + prevX[0];
        currY[0] = toNum(grid[ii][0], "Y") + prevY[0];

        if (cond(currX[0], currY[0])) count++;

        for (let jj = 1; jj < N; jj++) {
            currX[jj] =
                currX[jj - 1] + prevX[jj] - prevX[jj - 1] + toNum(grid[ii][jj], "X");
            currY[jj] =
                currY[jj - 1] + prevY[jj] - prevY[jj - 1] + toNum(grid[ii][jj], "Y");

            if (cond(currX[jj], currY[jj])) count += 1;
        }

        [currX, prevX] = [prevX, currX];
        [currY, prevY] = [prevY, currY];
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
