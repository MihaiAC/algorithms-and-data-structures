import * as fs from "fs";

const OPS = {
    "+": (a: number, b: number) => a + b,
    "*": (a: number, b: number) => a * b,
};

const ACCUM_START = {
    "+": 0,
    "*": 1,
};

function readInput(fileName: string): [number[][], string[]] {
    const lines = fs.readFileSync(fileName, "utf-8").split(/\r?\n/);
    const signs = lines.pop()!.trim().split(/\s+/);
    const numbers = lines.map((line) =>
        line
            .trim()
            .split(/\s+/)
            .map((x) => Number(x))
    );

    return [numbers, signs];
}

function p1(numbers: number[][], signs: string[]): number {
    let ans = 0;
    for (let colIdx = 0; colIdx < numbers[0]!.length; colIdx++) {
        const sign = signs[colIdx] as "+" | "*";
        ans += numbers.reduce(
            (accum: number, row: number[]) => OPS[sign](accum, row[colIdx]),
            ACCUM_START[sign]
        );
    }

    return ans;
}

function p2(fileName: string): number {
    const lines = fs.readFileSync(fileName, "utf-8").split(/\r?\n/);
    const signs = lines.pop()!;
    const nrows = lines.length;

    const parseCol = (colIdx: number) => {
        const currNum: string[] = [];
        for (let rowIdx = nrows - 1; rowIdx >= 0; rowIdx--) {
            if (lines[rowIdx][colIdx] !== " ") {
                currNum.push(lines[rowIdx][colIdx]);
            }
        }

        // Column is a separator.
        if (currNum.length === 0) {
            return undefined;
        }

        return Number(currNum.reverse().join(""));
    };

    let ans = 0;
    let partial = 0;
    let currSign: "+" | "*" = "+";
    for (let colIdx = 0; colIdx < signs.length; colIdx++) {
        if (signs[colIdx] === "+" || signs[colIdx] === "*") {
            currSign = signs[colIdx]! as "+" | "*";
            partial = ACCUM_START[currSign];
        }

        const currNum = parseCol(colIdx);
        if (currNum === undefined) {
            ans += partial;
        } else {
            partial = OPS[currSign](partial, currNum);
        }
    }

    return ans + partial;
}

const [exampleNumbers, exampleSigns] = readInput("d6-example.txt");
console.log(p1(exampleNumbers, exampleSigns));

const [inputNumbers, inputSigns] = readInput("d6-input.txt");
console.log(p1(inputNumbers, inputSigns));

console.log(p2("d6-example.txt"));
console.log(p2("d6-input.txt"));
