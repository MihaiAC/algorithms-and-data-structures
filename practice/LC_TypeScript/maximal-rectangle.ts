import assert from "node:assert";

function maximalRectangle(matrix: string[][]): number {
    const [M, N] = [matrix.length, matrix[0]!.length];

    const maxWidth: number[][] = Array.from({ length: M }, () => Array(N).fill(0));
    for (let ii = 0; ii < M; ii++) {
        maxWidth[ii][N - 1] = Number(matrix[ii][N - 1]);
        for (let jj = N - 2; jj >= 0; jj--) {
            if (matrix[ii][jj] === "0") maxWidth[ii][jj] = 0;
            else maxWidth[ii][jj] = maxWidth[ii][jj + 1] + 1;
        }
    }

    let maxArea = 0;
    for (let ii = 0; ii < M; ii++) {
        for (let jj = 0; jj < N; jj++) {
            if (matrix[ii][jj] === "1") {
                let currArea = maxWidth[ii][jj];
                maxArea = Math.max(maxArea, currArea);

                let currWidth = maxWidth[ii][jj];
                let kk = ii + 1;
                while (kk < M && matrix[kk][jj] === "1") {
                    currWidth = Math.min(currWidth, maxWidth[kk][jj]);
                    maxArea = Math.max(maxArea, currWidth * (kk - ii + 1));
                    kk += 1;
                }
            }
        }
    }

    return maxArea;
}

const matrix1 = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"],
];
assert.equal(maximalRectangle(matrix1), 6);
