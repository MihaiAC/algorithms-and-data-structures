import assert from "node:assert";
import * as fs from "fs";

function p1(ranges: number[][]): number {
    let sum = 0;
    for (const range of ranges) {
        assert(range.length === 2, `Incorrect range in input: ${range}`);

        const min = range[0]!;
        const max = range[1]!;

        for (let num = min; num <= max; num++) {
            const numStr = String(num);
            if (numStr.length % 2 === 0) {
                const halfIdx = Math.floor(numStr.length / 2);
                if (numStr.slice(0, halfIdx).endsWith(numStr.slice(halfIdx))) {
                    sum += num;
                }
            }
        }
    }

    return sum;
}

const getRanges = (fileName: string) =>
    fs
        .readFileSync(fileName, "utf-8")
        .trim()
        .split(",")
        .map((x) => x.split("-").map((y) => Number(y)));

console.log(p1(getRanges("d2-example.txt")));
console.log(p1(getRanges("d2-p1.txt")));
