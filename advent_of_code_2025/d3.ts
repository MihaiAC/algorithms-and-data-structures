import assert from "assert";
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

function p2(joltages: string[], nDials: number): number {
    let maxSum = 0;
    const stringLen = joltages[0]!.length;

    assert(nDials <= stringLen, "TOO MANY DIALS, MAN!");

    for (const joltage of joltages) {
        const digits = [];
        for (let idx = stringLen - nDials; idx < stringLen; idx++) {
            digits.push(joltage.at(idx)!);
        }

        for (let idx = stringLen - nDials - 1; idx >= 0; idx--) {
            const digit = joltage.at(idx)!;
            if (digit >= digits[0]!) {
                let carry = digits[0]!;
                digits[0]! = digit;
                for (let digitIdx = 1; digitIdx < nDials; digitIdx++) {
                    if (carry >= digits[digitIdx]!) {
                        const tmp = digits[digitIdx]!;
                        digits[digitIdx]! = carry;
                        carry = tmp;
                    } else {
                        break;
                    }
                }
            }
        }

        maxSum += Number(digits.join(""));
    }

    return maxSum;
}

const getJoltages = (fileName: string) =>
    fs.readFileSync(fileName, "utf-8").split(/\r?\n/);
console.log(p1(getJoltages("d3-example.txt")));
console.log(p1(getJoltages("d3-input.txt")));
console.log(p2(getJoltages("d3-example.txt"), 2));
console.log(p2(getJoltages("d3-example.txt"), 12));
console.log(p2(getJoltages("d3-input.txt"), 12));
