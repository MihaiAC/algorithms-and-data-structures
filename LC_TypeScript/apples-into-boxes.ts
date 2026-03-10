import assert from "node:assert";

function minimumBoxes(apple: number[], capacity: number[]): number {
    const apples = apple.reduce((accum: number, curr: number) => accum + curr, 0);
    capacity.sort((a: number, b: number) => b - a);

    let curr = 0;
    for (let idx = 0; idx < capacity.length; idx++) {
        curr += capacity[idx];

        if (curr >= apples) {
            return idx + 1;
        }
    }

    return -1;
}

const apple1 = [1, 3, 2];
const capacity1 = [4, 3, 1, 5, 2];
assert.equal(minimumBoxes(apple1, capacity1), 2);
