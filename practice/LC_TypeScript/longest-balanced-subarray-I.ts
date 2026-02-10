import assert from "node:assert";

function longestBalanced(nums: number[]): number {
    const N = nums.length;
    if (N === 1) return 0;

    let ans = 0;
    for (let ii = 0; ii < N - 1; ii++) {
        const even = new Set<number>();
        const odd = new Set<number>();

        for (let jj = ii; jj < N; jj++) {
            if (nums[jj] % 2 === 0) even.add(nums[jj]);
            else odd.add(nums[jj]);

            if (even.size === odd.size) {
                ans = Math.max(ans, jj - ii + 1);
            }
        }
    }

    return ans;
}

assert.equal(longestBalanced([2, 5, 4, 3]), 4);
assert.equal(longestBalanced([3, 2, 2, 5, 4]), 5);
assert.equal(longestBalanced([1, 2, 3, 2]), 3);
assert.equal(longestBalanced([1]), 0);
