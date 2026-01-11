import assert from "node:assert";

function maximalRectangle(matrix: string[][]): number {
    const [M, N] = [matrix.length, matrix[0]!.length];
    const widths: number[] = Array(M + 1).fill(0);
    let maxArea = 0;

    for (let jj = N - 1; jj >= 0; jj--) {
        const stack: number[] = [-1];

        for (let ii = 0; ii <= M; ii++) {
            if (ii < M) {
                if (matrix[ii][jj] === "1") {
                    widths[ii] += 1;
                } else {
                    widths[ii] = 0;
                }
            }

            while (
                stack.length > 1 &&
                (ii === M || widths[ii]! < widths[stack[stack.length - 1]!]!)
            ) {
                const prevRow = stack.pop()!;
                const height = ii - stack[stack.length - 1]! - 1;
                const area = widths[prevRow]! * height;
                maxArea = Math.max(maxArea, area);
            }

            if (ii < M) {
                stack.push(ii);
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
