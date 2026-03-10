import assert from "node:assert";

function maxProfit(prices: number[], strategy: number[], k: number): number {
    const N = prices.length;
    const halfK = Math.floor(k / 2);

    // Profit without any changes
    let ans = prices.reduce(
        (acc: number, price: number, idx: number) => acc + price * strategy[idx],
        0
    );

    let rolling = ans;
    for (let idx = 0; idx < halfK; idx++) {
        rolling -= prices[idx] * strategy[idx];
    }

    for (let idx = halfK; idx < k; idx++) {
        if (strategy[idx] === -1) {
            rolling += 2 * prices[idx];
        } else if (strategy[idx] === 0) {
            rolling += prices[idx];
        }
    }

    ans = Math.max(ans, rolling);
    for (let idx = k; idx < N; idx++) {
        // idx - k no longer 0
        rolling += strategy[idx - k] * prices[idx - k];

        // idx - halfK transitions from sell to 0
        rolling -= prices[idx - halfK];

        // idx transitions from whatever it is to 0
        if (strategy[idx] === -1) {
            rolling += 2 * prices[idx];
        } else if (strategy[idx] === 0) {
            rolling += prices[idx];
        }

        ans = Math.max(ans, rolling);
    }

    return ans;
}

const prices1 = [4, 2, 8];
const strategy1 = [-1, 0, 1];
const k1 = 2;
assert.equal(maxProfit(prices1, strategy1, k1), 10);

const prices2 = [5, 4, 3];
const strategy2 = [1, 1, 0];
const k2 = 2;
assert.equal(maxProfit(prices2, strategy2, k2), 9);
