import * as fs from "fs";
import _ from "lodash";

type Interval = [number, number];

function readInput(fileName: string): [Interval[], number[]] {
    const input = fs.readFileSync(fileName, "utf8").split(/\r?\n/);

    const intervals: Interval[] = [];
    const numbers: number[] = [];
    let sw = true;

    input.map((val: string) => {
        if (val === "") {
            sw = false;
        } else if (sw) {
            const split = val.split("-");
            intervals.push([Number(split[0]!), Number(split[1]!)]);
        } else {
            numbers.push(Number(val) as number);
        }
    });

    return [intervals, numbers];
}

function sortAndMergeIntervals(intervals: Interval[]): [number, number][] {
    intervals.sort((a, b) => a[0] - b[0]);
    let cIdx = 0;
    let newIntervals: [number, number][] = [];

    while (cIdx < intervals.length) {
        const currStart = intervals[cIdx][0];
        let currEnd = intervals[cIdx][1];
        let newIdx = cIdx + 1;

        while (newIdx < intervals.length && intervals[newIdx][0] <= currEnd) {
            currEnd = Math.max(currEnd, intervals[newIdx][1]);
            newIdx += 1;
        }

        newIntervals.push([currStart, currEnd]);
        cIdx = newIdx;
    }

    return newIntervals;
}

function p1(intervals: Interval[], numbers: number[]): number {
    let freshCount = 0;

    intervals = sortAndMergeIntervals(intervals);
    for (const num of numbers) {
        const idx = _.sortedLastIndexBy(intervals, [num, 0], (x) => x[0]);
        if (idx - 1 >= 0 && intervals[idx - 1][1] >= num) {
            freshCount += 1;
        }
    }

    return freshCount;
}

const [exampleIntervals, exampleNumbers] = readInput("d5-example.txt");
const [inputIntervals, inputNumbers] = readInput("d5-input.txt");
console.log(p1(exampleIntervals, exampleNumbers));
console.log(p1(inputIntervals, inputNumbers));
