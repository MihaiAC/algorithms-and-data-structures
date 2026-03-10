import { MaxHeap } from "datastructures-js";
import assert from "node:assert";

function isPossible(target: number[]): boolean {
    const N = target.length;
    const heap = MaxHeap.heapify(target);
    let currSum = target.reduce((accum, curr) => accum + curr, 0);

    while (true) {
        const maxNum = heap.pop()!;
        const rest = currSum - maxNum;

        if (maxNum === 1) return true;
        if (rest === 1) return true;
        if (rest === 0 || maxNum <= rest) return false;

        const prevNum = maxNum % rest;
        if (prevNum === 0) return false;

        heap.push(prevNum);
        currSum = rest + prevNum;
    }
}

assert.equal(isPossible([9, 3, 5]), true);
assert.equal(isPossible([1, 1, 1, 2]), false);
assert.equal(isPossible([8, 5]), true);
