import assert from "node:assert";

const MAX_SUM = 9 * 4;

function sumDigits(num: number): number {
    let sum = 0;
    while (num > 0) {
        sum += num % 10;
        num = Math.floor(num / 10);
    }

    return sum;
}

function minElement(nums: number[]): number {
    return nums.reduce((currMin, num) => Math.min(currMin, sumDigits(num)), MAX_SUM);
}

assert.equal(minElement([10, 11, 12, 20]), 1);
assert.equal(minElement([999, 19, 199]), 10);
