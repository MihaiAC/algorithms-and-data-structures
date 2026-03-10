import assert from "node:assert";

function minimumAbsDifference(arr: number[]): number[][] {
    arr.sort((a, b) => a - b);

    let ans = [[arr[0], arr[1]]];
    let minDiff = arr[1]! - arr[0]!;
    for (let idx = 1; idx < arr.length - 1; idx++) {
        const currDiff = arr[idx + 1] - arr[idx];
        if (currDiff === minDiff) ans.push([arr[idx], arr[idx + 1]]);
        else if (currDiff < minDiff) {
            minDiff = currDiff;
            ans = [[arr[idx], arr[idx + 1]]];
        }
    }

    return ans;
}

const arr1 = [4, 2, 1, 3];
const out1 = [
    [1, 2],
    [2, 3],
    [3, 4],
];
assert.deepStrictEqual(minimumAbsDifference(arr1), out1);

const arr2 = [3, 8, -10, 23, 19, -4, -14, 27];
const out2 = [
    [-14, -10],
    [19, 23],
    [23, 27],
];
assert.deepStrictEqual(minimumAbsDifference(arr2), out2);
