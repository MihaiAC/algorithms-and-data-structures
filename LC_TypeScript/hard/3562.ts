import assert from "node:assert";

function maxProfit(
    n: number,
    present: number[],
    future: number[],
    hierarchy: number[][],
    maxBudget: number
): number {
    // underlings[u] -> employees u is the boss of;
    const underlings: number[][] = Array.from({ length: n }, () => []);

    // Get rid of 1-indexed BS.
    for (const [u, v] of hierarchy) {
        underlings[u - 1].push(v - 1);
    }

    // Tree, so memoisation not needed
    const dfs = (u: number) => {
        const uCost = present[u];
        const uDiscountCost = Math.floor(present[u] / 2);

        // dp0 = if parent of u (hmm reminds me of wonder of u) was not bought
        const dp0: number[] = Array(maxBudget + 1).fill(0);
        // dp1 = if parent of u was bought
        const dp1: number[] = Array(maxBudget + 1).fill(0);

        // Profit in subtree of u if discount is not avail (0) or
        // avail (1)
        const subProfit0: number[] = Array(maxBudget + 1).fill(0);
        const subProfit1: number[] = Array(maxBudget + 1).fill(0);

        // Max we could spend in u's subtree (including u)
        let maxSpend = uCost;

        // Calculate subProfit0 and subProfit1.
        for (const v of underlings[u]) {
            const [subDp0, subDp1, subMaxSpend] = dfs(v);
            maxSpend += subMaxSpend;

            // Iterate through every possible budget and subBudget (for u's subtree)
            for (let budget = maxBudget; budget >= 0; budget--) {
                for (
                    let subBudget = 0;
                    subBudget <= Math.min(budget, subMaxSpend);
                    subBudget++
                ) {
                    subProfit0[budget] = Math.max(
                        subProfit0[budget],
                        subProfit0[budget - subBudget] + subDp0[subBudget]
                    );

                    subProfit1[budget] = Math.max(
                        subProfit1[budget],
                        subProfit1[budget - subBudget] + subDp1[subBudget]
                    );
                }
            }
        }

        // Calculate dp0 and dp1.
        for (let budget = 0; budget <= maxBudget; budget++) {
            dp0[budget] = dp1[budget] = subProfit0[budget];

            if (budget >= uDiscountCost) {
                dp1[budget] = Math.max(
                    subProfit0[budget],
                    subProfit1[budget - uDiscountCost] + future[u] - uDiscountCost
                );
            }

            if (budget >= uCost) {
                dp0[budget] = Math.max(
                    subProfit0[budget],
                    subProfit1[budget - uCost] + future[u] - uCost
                );
            }
        }

        return [dp0, dp1, maxSpend] as const;
    };

    return dfs(0)[0][maxBudget];
}

const n = 3;
const present = [5, 2, 3];
const future = [8, 5, 6];
const hierarchy = [
    [1, 2],
    [2, 3],
];
const maxBudget = 7;

assert.equal(maxProfit(n, present, future, hierarchy, maxBudget), 12);
