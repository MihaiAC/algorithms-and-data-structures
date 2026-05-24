import assert from "node:assert";

function maxJumps(arr: number[], d: number): number {
    const N = arr.length;
    const dp = new Array<number>(N).fill(1);
    const augArr = arr.map((val, idx) => [val, idx]).sort((a, b) => a[0] - b[0]);

    let ans = 0;
    for (const [currVal, currIdx] of augArr) {
        let maxInRange = 0;

        for (let idx = currIdx + 1; idx <= Math.min(currIdx + d, N - 1); idx++) {
            if (arr[idx] >= currVal) break;
            if (dp[idx] > maxInRange) maxInRange = dp[idx];
        }

        for (let idx = currIdx - 1; idx >= Math.max(0, currIdx - d); idx--) {
            if (arr[idx] >= currVal) break;
            if (dp[idx] > maxInRange) maxInRange = dp[idx];
        }

        dp[currIdx] = maxInRange + 1;
        if (dp[currIdx] > ans) ans = dp[currIdx];
    }

    return ans;
}

assert.equal(maxJumps([7, 6, 5, 4, 3, 2, 1], 1), 7);
assert.equal(maxJumps([3, 3, 3, 3], 3), 1);
