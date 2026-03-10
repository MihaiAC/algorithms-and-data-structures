import { Queue } from "datastructures-js";
import * as fs from "fs";

const DELTAS = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
    [1, 1],
    [1, -1],
    [-1, 1],
    [-1, -1],
];

function p1(matrix: string[][]): number {
    const M = matrix.length;
    const N = matrix[0]!.length;

    let ans = 0;
    for (let row = 0; row < M; row++) {
        for (let col = 0; col < N; col++) {
            if (matrix[row]![col]! !== "@") continue;

            let adj = 0;
            for (const [dx, dy] of DELTAS) {
                const nrow = row + dx;
                const ncol = col + dy;
                if (
                    nrow >= 0 &&
                    ncol >= 0 &&
                    nrow < M &&
                    ncol < N &&
                    matrix[nrow]![ncol]! === "@"
                ) {
                    adj += 1;
                }
            }

            if (adj < 4) {
                ans += 1;
            }
        }
    }

    return ans;
}

function p2(matrix: string[][]): number {
    const M = matrix.length;
    const N = matrix[0]!.length;

    const isValid = (row: number, col: number) => {
        return row >= 0 && col >= 0 && row < M && col < N && matrix[row]![col]! === "@";
    };

    const countAdj = (row: number, col: number) => {
        let adj = 0;
        for (const [dx, dy] of DELTAS) {
            const nrow = row + dx;
            const ncol = col + dy;
            if (isValid(nrow, ncol)) {
                adj += 1;
            }
        }

        return adj;
    };

    const getKey = (row: number, col: number) => `${row},${col}`;

    const added = new Set<string>();
    const queue = new Queue<number[]>();

    // Add boxes we can eliminate initially.
    let ans = 0;
    for (let row = 0; row < M; row++) {
        for (let col = 0; col < N; col++) {
            if (matrix[row][col] === "@" && countAdj(row, col) < 4) {
                queue.enqueue([row, col]);
                added.add(getKey(row, col));
            }
        }
    }

    // As we eliminate boxes, add new ones we can remove.
    while (!queue.isEmpty()) {
        const [row, col] = queue.dequeue() as [number, number];
        matrix[row][col] = ".";
        ans += 1;

        for (const [dx, dy] of DELTAS) {
            const nrow = row + dx;
            const ncol = col + dy;
            if (
                !added.has(getKey(nrow, ncol)) &&
                isValid(nrow, ncol) &&
                countAdj(nrow, ncol) < 4
            ) {
                added.add(getKey(nrow, ncol));
                queue.enqueue([nrow, ncol]);
            }
        }
    }

    return ans;
}

const getMatrix = (fileName: string) =>
    fs
        .readFileSync(fileName, "utf-8")
        .trim()
        .split(/\r?\n/)
        .map((row) => row.split(""));

const exampleMatrix = getMatrix("d4-example.txt");
const inputMatrix = getMatrix("d4-input.txt");

console.log(p1(exampleMatrix));
console.log(p1(inputMatrix));
console.log(p2(exampleMatrix));
console.log(p2(inputMatrix));
