import assert from "node:assert";
import * as fs from "fs";

function isInvalidP1(numStr: string): boolean {
    if (numStr.length % 2 === 0) {
        const halfIdx = Math.floor(numStr.length / 2);
        if (numStr.slice(0, halfIdx).endsWith(numStr.slice(halfIdx))) {
            return true;
        }
    }

    return false;
}

function isInvalidP2(numStr: string): boolean {
    const N = numStr.length;
    // Would be faster to only analyse divisors.
    for (let chunkSize = 1; chunkSize <= Math.floor(N / 2); chunkSize++) {
        if (N % chunkSize === 0) {
            const base = numStr.slice(0, chunkSize);
            if (numStr === base.repeat(Math.floor(N / chunkSize))) {
                return true;
            }
        }
    }

    return false;
}

function calculateSum(
    ranges: number[][],
    isInvalid: (numStr: string) => boolean
): number {
    let sum = 0;
    for (const range of ranges) {
        assert(range.length === 2, `Incorrect range in input: ${range}`);

        const min = range[0]!;
        const max = range[1]!;

        for (let num = min; num <= max; num++) {
            if (isInvalid(String(num))) {
                sum += num;
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

console.log(calculateSum(getRanges("d2-example.txt"), isInvalidP1));
console.log(calculateSum(getRanges("d2-p1.txt"), isInvalidP1));
console.log(calculateSum(getRanges("d2-example.txt"), isInvalidP2));
console.log(calculateSum(getRanges("d2-p1.txt"), isInvalidP2));
