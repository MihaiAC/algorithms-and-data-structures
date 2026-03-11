import assert from "node:assert";

function isTrionic(nums: number[]): boolean {
    const N = nums.length;

    let ii = 0;
    while (ii < N - 1 && nums[ii] < nums[ii + 1]) ii++;
    if (ii === 0) return false;

    let jj = N - 1;
    while (jj > 0 && nums[jj - 1] < nums[jj]) jj--;
    if (jj === N - 1) return false;

    if (ii >= jj) return false;
    for (let kk = ii; kk < jj; kk++) {
        if (nums[kk] <= nums[kk + 1]) return false;
    }

    return true;
}

assert.equal(isTrionic([1, 3, 5, 4, 2, 6]), true);
assert.equal(isTrionic([2, 1, 3]), false);
