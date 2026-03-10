import assert from "node:assert";

function maximizeSquareHoleArea(
    n: number,
    m: number,
    hBars: number[],
    vBars: number[]
): number {
    hBars.sort((a, b) => a - b);
    vBars.sort((a, b) => a - b);

    const getMaxConsec = (arr: number[]) => {
        let [curr, max] = [1, 1];

        for (let ii = 1; ii < arr.length; ii++) {
            if (arr[ii] === arr[ii - 1] + 1) curr++;
            else curr = 1;
            max = Math.max(max, curr);
        }

        return max;
    };

    const side = Math.min(getMaxConsec(hBars), getMaxConsec(vBars)) + 1;
    return side * side;
}

const n = 1;
const m = 1;
const hBars = [2];
const vBars = [2];
assert.equal(maximizeSquareHoleArea(n, m, hBars, vBars), 4);
