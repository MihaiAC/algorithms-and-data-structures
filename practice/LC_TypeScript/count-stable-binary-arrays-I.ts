import assert from "node:assert";

const MODN = 10 ** 9 + 7;

function numberOfStableArrays(zero: number, one: number, limit: number): number {
    // dp[ii][jj][x] = how many valid arrays have ii zeros, jj ones, and end with 'x'
    // (either '0' or '1')
    const dp = Array.from({ length: zero + 1 }, () =>
        Array.from({ length: one + 1 }, () => [0, 0])
    );

    // Init for x = '0'
    for (let ii = 0; ii <= Math.min(zero, limit); ii++) {
        dp[ii][0][0] = 1;
    }

    // Init for x = '1'
    for (let jj = 0; jj <= Math.min(one, limit); jj++) {
        dp[0][jj][1] = 1;
    }

    for (let ii = 1; ii <= zero; ii++) {
        for (let jj = 1; jj <= one; jj++) {
            // Add a zero.
            dp[ii][jj][0] = dp[ii - 1][jj][1] + dp[ii - 1][jj][0];

            // If ii > limit, remove the invalid arrangements (last "limit" digits = 0).
            if (ii > limit) dp[ii][jj][0] -= dp[ii - limit - 1][jj][1];

            // Add a one.
            dp[ii][jj][1] = dp[ii][jj - 1][0] + dp[ii][jj - 1][1];
            // Same as above, remove count of invalid ones.
            if (jj > limit) dp[ii][jj][1] -= dp[ii][jj - limit - 1][0];

            // Keep within bounds
            dp[ii][jj][0] = (dp[ii][jj][0] + MODN) % MODN;
            dp[ii][jj][1] = (dp[ii][jj][1] + MODN) % MODN;
        }
    }

    return (dp[zero][one][0] + dp[zero][one][1]) % MODN;
}

assert.equal(numberOfStableArrays(1, 2, 1), 1);
assert.equal(numberOfStableArrays(3, 3, 2), 14);
assert.equal(numberOfStableArrays(39, 20, 18), 207227572);
