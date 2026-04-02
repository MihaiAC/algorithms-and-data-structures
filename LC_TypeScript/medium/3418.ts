import assert from "node:assert";

function maximumAmount(coins: number[][]): number {
    const [M, N] = [coins.length, coins[0].length];
    const dp = Array.from({ length: M }, () =>
        Array.from({ length: N }, () => Array.from({ length: 3 }, () => -Infinity))
    );

    const withinBounds = (ii: number, jj: number): boolean =>
        ii >= 0 && ii < M && jj >= 0 && jj < N;

    const safeGet = (ii: number, jj: number, kk: number): number | undefined =>
        withinBounds(ii, jj) ? dp[ii][jj][kk] : undefined;

    const maxNeighbours = (ii: number, jj: number, kk: number): number => {
        const right = safeGet(ii, jj + 1, kk);
        const down = safeGet(ii + 1, jj, kk);

        if (right !== undefined && down !== undefined) return Math.max(right, down);
        else if (right !== undefined) return right;
        else if (down !== undefined) return down;
        return 0;
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
