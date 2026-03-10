import assert from "node:assert";

function longestBalanced(nums: number[]): number {
    const N = nums.length;
    if (N === 1) return 0;

    const sign = Array.from<number>({ length: N }).fill(0);
    const maxElem = Math.max(...nums);
    const lastPos = Array.from<number>({ length: maxElem }).fill(-1);

    let ans = 0;
    for (let rightIdx = 0; rightIdx < N; rightIdx++) {
        const num = nums[rightIdx];

        // Update lastPos for num
        if (lastPos[num] != -1) sign[lastPos[num]] = 0;
        lastPos[num] = rightIdx;

        // Assign sign
        if (num % 2 === 0) sign[rightIdx] = 1;
        else sign[rightIdx] = -1;

        // Sum leftward from right. If 0 => update ans.
        let currSum = 0;
        for (let leftIdx = rightIdx; leftIdx >= 0; leftIdx--) {
            currSum += sign[leftIdx];
            if (currSum === 0) ans = Math.max(ans, rightIdx - leftIdx + 1);
        }
    }

    return ans;
}

assert.equal(longestBalanced([2, 5, 4, 3]), 4);
assert.equal(longestBalanced([3, 2, 2, 5, 4]), 5);
assert.equal(longestBalanced([1, 2, 3, 2]), 3);
assert.equal(longestBalanced([1]), 0);
