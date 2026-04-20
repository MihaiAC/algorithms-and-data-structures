import assert from "node:assert";

function maxDistance(colors: number[]): number {
    const N = colors.length;
    let ans = 0;
    for (let ii = 0; ii < N - ans; ii++) {
        let jj = ii + ans + 1;
        while (jj < N) {
            if (colors[ii] !== colors[jj]) {
                ans = Math.max(ans, jj - ii);
            }
            jj += 1;
        }
    }

    return ans;
}

assert.equal(maxDistance([1, 1, 1, 6, 1, 1, 1]), 3);
assert.equal(maxDistance([1, 8, 3, 8, 3]), 4);
assert.equal(maxDistance([0, 1]), 1);
