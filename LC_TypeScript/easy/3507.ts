import assert from "node:assert";

function minimumPairRemoval(nums: number[]): number {
    let ans = 0;

    while (nums.length > 1) {
        let ascending = true;
        let minSum = Infinity;
        let targetIdx = 0;

        for (let idx = 0; idx < nums.length - 1; idx++) {
            const currSum = nums[idx] + nums[idx + 1];

            if (nums[idx] > nums[idx + 1]) {
                ascending = false;
            }

            if (currSum < minSum) {
                minSum = currSum;
                targetIdx = idx;
            }
        }

        if (ascending) break;

        ans++;
        nums[targetIdx] += nums[targetIdx + 1];
        nums.splice(targetIdx + 1, 1);
    }

    return ans;
}

assert.equal(minimumPairRemoval([5, 2, 3, 1]), 2);
assert.equal(minimumPairRemoval([1, 2, 2]), 0);
