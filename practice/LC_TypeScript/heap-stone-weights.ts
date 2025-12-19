import { MaxHeap } from "datastructures-js";
import assert from "node:assert";

function lastStoneWeight(stones: number[]): number {
    const heap = MaxHeap.heapify(stones);
    while (heap.size() > 1) {
        const a = heap.extractRoot()!;
        const b = heap.extractRoot()!;
        if (a === b) {
            continue;
        } else {
            heap.push(a - b);
        }
    }

    return heap.size() > 0 ? heap.extractRoot()! : 0;
}

assert.equal(lastStoneWeight([2, 7, 4, 1, 8, 1]), 1);
assert.equal(lastStoneWeight([1]), 1);
assert.equal(lastStoneWeight([2, 2]), 0);
