import assert from "node:assert";

function maximumProfit(prices: number[], k: number): number {
    const N = prices.length;
    const NINF = -1e9;

    // memo[idx][ops][mode]
    const memo: number[][][] = Array.from({ length: N + 1 }, () =>
        Array.from({ length: k + 1 }, () => Array(3).fill(null))
    );

    const dp = (idx: number, ops: number, mode: number): number => {
        if (idx === N) {
            // If we reach the end with an open position, return -Inf
            return mode === 0 ? 0 : NINF;
        }

        if (ops === 0) {
            return 0;
        }

        if (memo[idx][ops][mode] !== null) {
            return memo[idx][ops][mode];
        }

        // We must close all open positions
        let maxProfit = mode === 0 ? 0 : NINF;

        if (mode === 0) {
            // mode = 0 => we're holding no stock;

            // Buy stock
            maxProfit = Math.max(maxProfit, dp(idx + 1, ops, 1) - prices[idx]);

            // Short stock
            maxProfit = Math.max(maxProfit, dp(idx + 1, ops, 2) + prices[idx]);
        } else if (mode === 1) {
            // mode = 1 => we're looking to sell
            maxProfit = Math.max(maxProfit, dp(idx + 1, ops - 1, 0) + prices[idx]);
        } else {
            // mode = 2 => we're looking to buy
            maxProfit = Math.max(maxProfit, dp(idx + 1, ops - 1, 0) - prices[idx]);
        }

        // Or, alternatively skip
        maxProfit = Math.max(maxProfit, dp(idx + 1, ops, mode));

        // Save curr result
        memo[idx][ops][mode] = maxProfit;

        return maxProfit;
    };

    return dp(0, k, 0);
}

const prices1 = [1, 7, 9, 8, 2];
const k1 = 2;
assert.equal(maximumProfit(prices1, k1), 14);
const prices2 = [12, 16, 19, 19, 8, 1, 19, 13, 9];
const k2 = 3;
assert.equal(maximumProfit(prices2, k2), 36);
