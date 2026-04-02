import assert from "node:assert";

function maximumAmount(coins: number[][]): number {
    const [M, N] = [coins.length, coins[0].length];
    let next = Array.from({ length: N + 1 }, () =>
        Array.from({ length: 3 }, () => -Infinity)
    );
    let curr = Array.from({ length: N + 1 }, () =>
        Array.from({ length: 3 }, () => -Infinity)
    );

    const maxNeighbours = (jj: number, kk: number): number => {
        const max = Math.max(curr[jj + 1][kk], next[jj][kk]);
        return max !== -Infinity ? max : 0;
    };

    for (let ii = M - 1; ii >= 0; ii--) {
        for (let jj = N - 1; jj >= 0; jj--) {
            const maxN2 = maxNeighbours(jj, 2);
            const maxN1 = maxNeighbours(jj, 1);

            curr[jj][2] = coins[ii][jj] + maxN2;
            curr[jj][1] = Math.max(coins[ii][jj] + maxN1, maxN2);
            curr[jj][0] = Math.max(coins[ii][jj] + maxNeighbours(jj, 0), maxN1);
        }
        [curr, next] = [next, curr];
    }

    return next[0][0];
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
