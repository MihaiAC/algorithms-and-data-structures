import assert from "node:assert";

function maximumAmount(coins: number[][]): number {
    const [M, N] = [coins.length, coins[0].length];
    const dp = Array.from({ length: M + 1 }, () =>
        Array.from({ length: N + 1 }, () => Array.from({ length: 3 }, () => -Infinity))
    );

    const maxNeighbours = (ii: number, jj: number, kk: number): number => {
        const max = Math.max(dp[ii][jj + 1][kk], dp[ii + 1][jj][kk]);
        return max !== -Infinity ? max : 0;
    };

    for (let kk = 2; kk >= 0; kk--) {
        for (let jj = N - 1; jj >= 0; jj--) {
            for (let ii = M - 1; ii >= 0; ii--) {
                const maxNormal = coins[ii][jj] + maxNeighbours(ii, jj, kk);
                if (coins[ii][jj] < 0 && kk < 2) {
                    dp[ii][jj][kk] = Math.max(maxNormal, maxNeighbours(ii, jj, kk + 1));
                } else dp[ii][jj][kk] = maxNormal;
            }
        }
    }

    return dp[0][0][0];
}

assert.equal(
    maximumAmount([
        [0, 1, -1],
        [1, -2, 3],
        [2, -3, 4],
    ]),
    8
);

assert.equal(
    maximumAmount([
        [10, 10, 10],
        [10, 10, 10],
    ]),
    40
);

assert.equal(
    maximumAmount([
        [-17, -1, -16, 1, 14],
        [-18, -11, 12, 6, 6],
        [-6, -16, 5, 10, -11],
        [9, 5, -7, -5, -11],
        [14, -6, 4, -6, -5],
    ]),
    11
);
