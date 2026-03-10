import assert from "node:assert";

function maxSumTrionic(nums: number[]): number {
    const N = nums.length;
    let leftIdx = 0;
    let rightIdx = 0;
    let currSum, currIdx, leftAccum, leftMaxSum, rightAccum, rightMaxSum;
    let ans = -Infinity;

    // Search for a decreasing segment.
    while (leftIdx < N - 1) {
        if (nums[leftIdx] > nums[leftIdx + 1]) {
            // Found a decreasing segment.
            rightIdx = leftIdx + 1;
            currSum = nums[leftIdx] + nums[rightIdx];
            while (rightIdx < N - 1 && nums[rightIdx] > nums[rightIdx + 1]) {
                currSum += nums[rightIdx + 1];
                rightIdx++;
            }

            // Validate segment endpoints.
            if (leftIdx === 0 || rightIdx === N - 1) {
                leftIdx = rightIdx;
                continue;
            }

            // Check neighbouring segments are actually increasing.
            if (
                nums[leftIdx] <= nums[leftIdx - 1] ||
                nums[rightIdx] >= nums[rightIdx + 1]
            ) {
                leftIdx = rightIdx;
                continue;
            }

            leftAccum = nums[leftIdx - 1];
            leftMaxSum = leftAccum;
            currIdx = leftIdx - 1;
            while (currIdx > 0 && nums[currIdx - 1] < nums[currIdx]) {
                leftAccum += nums[currIdx - 1];
                leftMaxSum = Math.max(leftMaxSum, leftAccum);
                currIdx -= 1;
            }

            rightAccum = nums[rightIdx + 1];
            rightMaxSum = rightAccum;
            currIdx = rightIdx + 1;
            while (currIdx < N - 1 && nums[currIdx] < nums[currIdx + 1]) {
                rightAccum += nums[currIdx + 1];
                rightMaxSum = Math.max(rightAccum, rightMaxSum);
                currIdx += 1;
            }

            ans = Math.max(ans, leftMaxSum + currSum + rightMaxSum);
        }

        leftIdx += 1;
    }

    return ans;
}

assert.equal(maxSumTrionic([0, -2, -1, -3, 0, 2, -1]), -4);
assert.equal(maxSumTrionic([1, 4, 2, 7]), 14);
assert.equal(maxSumTrionic([1, 4, 2, 2, 3, 1, 2]), 8);
assert.equal(maxSumTrionic([-522, 534, -883, 111, -145, -682, 662]), -760);
