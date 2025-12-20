import * as fs from "fs";

function p1(joltages: string[]): number {
    let maxSum = 0;
    for (const joltage of joltages) {
        let firstDigit = joltage.at(-2)!;
        let secondDigit = joltage.at(-1)!;

        for (let idx = joltage.length - 3; idx >= 0; idx--) {
            const digit = joltage.at(idx)!;
            if (digit >= firstDigit) {
                secondDigit = secondDigit < firstDigit ? firstDigit : secondDigit;
                firstDigit = digit;
            }
        }

        maxSum += Number(firstDigit + secondDigit);
    }

    return maxSum;
}

const getJoltages = (fileName: string) =>
    fs.readFileSync(fileName, "utf-8").split(/\r?\n/);
console.log(p1(getJoltages("d3-example.txt")));
console.log(p1(getJoltages("d3-input.txt")));
