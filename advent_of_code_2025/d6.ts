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

const [exampleNumbers, exampleSigns] = readInput("d6-example.txt");
console.log(p1(exampleNumbers, exampleSigns));

const [inputNumbers, inputSigns] = readInput("d6-input.txt");
console.log(p1(inputNumbers, inputSigns));
