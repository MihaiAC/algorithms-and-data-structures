import * as fs from "fs";

function p1(coords: number[][]): number {
    // Quick and dirty, want to see p2 (sensing something nasty ~~~)
    const N = coords.length;
    const getArea = (p1: number[], p2: number[]): number => {
        return Math.abs(p1[0]! - p2[0]! + 1) * Math.abs(p1[1]! - p2[1]! + 1);
    };

    let ans = 0;
    for (let idx1 = 0; idx1 < N - 1; idx1++) {
        const p1 = coords[idx1]!;
        for (let idx2 = idx1 + 1; idx2 < N; idx2++) {
            const p2 = coords[idx2]!;
            ans = Math.max(ans, getArea(p1, p2));
        }
    }

    return ans;
}

const readInput = (fileName: string): number[][] => {
    return fs
        .readFileSync(fileName, "utf8")
        .split(/\r+\n/)
        .map((line: string) => line.split(",").map((x) => Number(x)));
};

const example = readInput("d9-example.txt");
const input = readInput("d9-input.txt");

console.log(p1(example));
console.log(p1(input));
