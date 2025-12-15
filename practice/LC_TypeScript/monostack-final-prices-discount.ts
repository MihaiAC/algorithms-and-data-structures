import assert from "node:assert";

function finalPrices(prices: number[]): number[] {
    const N = prices.length;
    const ans = Array(N).fill(0);
    const stack: number[] = [];

    for (let idx = N - 1; idx >= 0; idx--) {
        const curr = prices[idx];
        while (stack.length > 0 && curr < stack.at(-1)!) {
            stack.pop();
        }

        if (stack.length === 0) {
            ans[idx] = curr;
        } else {
            ans[idx] = curr - stack.at(-1)!;
        }

        stack.push(curr);
    }

    return ans;
}

assert.deepEqual(finalPrices([8, 4, 6, 2, 3]), [4, 2, 4, 2, 3]);
assert.deepEqual(finalPrices([10, 1, 1, 6]), [9, 0, 1, 6]);
