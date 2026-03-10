import assert from "node:assert";

function largestRectangleArea(heights: number[]): number {
    let maxArea = 0;
    const stack: number[] = [];

    for (let idx = 0; idx <= heights.length; idx++) {
        const currHeight = idx < heights.length ? heights[idx] : 0;
        while (stack.length > 0 && currHeight < heights[stack.at(-1)!]) {
            const lastHeight = heights[stack.pop()!];
            const width = stack.length === 0 ? idx : idx - stack.at(-1)! - 1;
            maxArea = Math.max(maxArea, lastHeight * width);
        }
        stack.push(idx);
    }

    return maxArea;
}

assert.deepEqual(largestRectangleArea([2, 1, 5, 6, 2, 3]), 10);
assert.deepEqual(largestRectangleArea([2, 4]), 4);
