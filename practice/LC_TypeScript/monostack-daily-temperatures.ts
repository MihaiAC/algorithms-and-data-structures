import assert from "node:assert";

function dailyTemperatures(temperatures: number[]): number[] {
    const N = temperatures.length;
    const ans = Array(N).fill(0);
    const stack: [number, number][] = [];

    for (let idx = N - 1; idx >= 0; idx--) {
        const currTemp = temperatures[idx];
        while (stack.length > 0 && currTemp >= stack.at(-1)![0]) {
            stack.pop();
        }

        if (stack.length > 0) {
            ans[idx] = stack.at(-1)![1] - idx;
        }

        stack.push([currTemp, idx]);
    }

    return ans;
}

const temps1 = [73, 74, 75, 71, 69, 72, 76, 73];
const ans1 = [1, 1, 4, 2, 1, 1, 0, 0];
assert.deepEqual(dailyTemperatures(temps1), ans1);

const temps2 = [30, 40, 50, 60];
const ans2 = [1, 1, 1, 0];
assert.deepEqual(dailyTemperatures(temps2), ans2);

const temps3 = [30, 60, 90];
const ans3 = [1, 1, 0];
assert.deepEqual(dailyTemperatures(temps3), ans3);
