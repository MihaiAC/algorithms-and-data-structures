import * as fs from "fs";

type Point = { x: number; y: number };

/**
 * Quick and dirty, want to see p2 (sensing something nasty ~~~)
 * @param points
 * @returns
 */
function p1(points: Point[]): number {
    const N = points.length;

    const getArea = (p1: Point, p2: Point): number => {
        return Math.abs(p1.x - p2.x + 1) * Math.abs(p1.y - p2.y + 1);
    };

    let ans = 0;
    for (let idx1 = 0; idx1 < N - 1; idx1++) {
        const p1 = points[idx1]!;
        for (let idx2 = idx1 + 1; idx2 < N; idx2++) {
            const p2 = points[idx2]!;
            ans = Math.max(ans, getArea(p1, p2));
        }
    }

    return ans;
}

const readInput = (fileName: string): Point[] => {
    return fs
        .readFileSync(fileName, "utf8")
        .split(/\r+\n/)
        .map((line: string) => {
            const [x, y] = line.split(",").map(Number);
            return { x, y };
        });
};

/**
 * Surprise! It was pretty nasty.
 * @param coords
 */
function p2(coords: number[][]): number {
    return 0;
}

const example = readInput("d9-example.txt");
const input = readInput("d9-input.txt");

console.log(p1(example));
console.log(p1(input));
