import assert from "node:assert";

function twoSum(nums: number[], target: number): number[] {
    const valToIdx = new Map<number, number>();
    for (let idx = 0; idx < nums.length; idx++) {
        const num = nums[idx];
        if (valToIdx.has(num)) return [valToIdx.get(num)!, idx];
        valToIdx.set(target - num, idx);
    }

    return [-1, -1];
}

assert.deepEqual(twoSum([2, 7, 11, 15], 9), [0, 1]);
assert.deepEqual(twoSum([3, 2, 4], 6), [1, 2]);
assert.deepEqual(twoSum([3, 3], 6), [0, 1]);
