import assert from "node:assert";
import { memoize } from "lodash";

function maximumProfit(prices: number[], k: number): number {
    const N = prices.length;
    const dp = memoize(
        (idx: number, ops: number, mode: number): number => {
            if (idx === N) {
                // If we reach the end with an open position, return -Inf
                return mode === 2 ? -Infinity : 0;
            }

            if (ops === 0) {
                return 0;
            }

            // We must close all open positions
            let maxProfit = mode === 0 ? 0 : -Infinity;

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

            // Or, alternatively: skip operation
            maxProfit = Math.max(maxProfit, dp(idx + 1, ops, mode));

            return maxProfit;
        },
        (idx, ops, mode) => `${idx},${ops},${mode}`
    );

    return dp(0, k, 0);
}

const prices1 = [1, 7, 9, 8, 2];
const k1 = 2;
assert.equal(maximumProfit(prices1, k1), 14);

const prices2 = [12, 16, 19, 19, 8, 1, 19, 13, 9];
const k2 = 3;
assert.equal(maximumProfit(prices2, k2), 36);
