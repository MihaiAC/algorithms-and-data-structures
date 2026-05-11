import assert from "node:assert";

function separateDigits(nums: number[]): number[] {
    return nums.flatMap((num) =>
        num
            .toString()
            .split("")
            .map((x) => parseInt(x))
    );
}

assert.deepEqual(separateDigits([13, 25, 83, 77]), [1, 3, 2, 5, 8, 3, 7, 7]);
assert.deepEqual(separateDigits([7, 1, 3, 9]), [7, 1, 3, 9]);
