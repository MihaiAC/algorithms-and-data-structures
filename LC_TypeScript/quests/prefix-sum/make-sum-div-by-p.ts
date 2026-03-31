import assert from "node:assert";

function minSubarray(nums: number[], p: number): number {
    const N = nums.length;

    let sum = 0;
    for (let idx = 0; idx < N; idx++) {
        nums[idx] = nums[idx] % p;
        sum += nums[idx];
    }

    sum = sum % p;
    if (sum === 0) return 0;

    const modLastIdx = new Map<number, number>();
    let currMod = 0;
    let ans = N;
    for (let idx = 0; idx < N; idx++) {
        currMod = (currMod + nums[idx]) % p;
        if (currMod === sum) ans = Math.min(ans, idx + 1);

        const searchMod = (currMod - sum + p) % p;
        if (modLastIdx.has(searchMod))
            ans = Math.min(ans, idx - modLastIdx.get(searchMod)!);

        modLastIdx.set(currMod, idx);
    }

    return ans < N ? ans : -1;
}

assert.equal(minSubarray([3, 1, 4, 2], 6), 1);
assert.equal(minSubarray([6, 3, 5, 2], 9), 2);
assert.equal(minSubarray([1, 2, 3], 3), 0);
assert.equal(minSubarray([5], 7), -1);
