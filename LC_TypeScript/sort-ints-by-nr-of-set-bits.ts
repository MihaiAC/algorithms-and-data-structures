import assert from "node:assert";
import { sortBy } from "lodash";

function sortByBits(arr: number[]): number[] {
    return sortBy(arr, [
        (num: number) =>
            Array.from(num.toString(2)).reduce(
                (accum: number, curr: string) => accum + (curr === "1" ? 1 : 0),
                0
            ),
        (num: number) => num,
    ]);
}

const arr1 = [0, 1, 2, 3, 4, 5, 6, 7, 8];
const res1 = [0, 1, 2, 4, 8, 3, 5, 6, 7];
assert.deepEqual(sortByBits(arr1), res1);

const arr2 = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1];
const res2 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024];
assert.deepEqual(sortByBits(arr2), res2);
