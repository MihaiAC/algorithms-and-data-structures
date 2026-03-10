import assert from "node:assert";

const countStreak = (x: number) => Math.trunc((x * (x + 1)) / 2);

function getDescentPeriods(prices: number[]): number {
    let streak = 1;
    let ans = 0;

    for (let idx = 1; idx < prices.length; idx += 1) {
        if (prices[idx] === prices[idx - 1] - 1) {
            streak += 1;
        } else {
            ans += countStreak(streak);
            streak = 1;
        }
    }

    ans += countStreak(streak);
    return ans;
}

assert.equal(getDescentPeriods([3, 2, 1, 4]), 7);
assert.equal(getDescentPeriods([8, 6, 7, 7]), 4);
assert.equal(getDescentPeriods([1]), 1);
