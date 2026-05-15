import assert from "node:assert";

function findMin(nums: number[]): number {
    const N = nums.length;

    if (N == 1) return nums[0];
    else if (nums[0] <= nums[N - 1]) return nums[0];

    let [left, right, middle] = [0, N - 1, 0];
    while (true) {
        middle = Math.floor((left + right) / 2);
        if (nums[middle] < nums[middle - 1]) return nums[middle];
        else if (middle != N - 1 && nums[middle] > nums[middle + 1])
            return nums[middle + 1];
        else if (nums[middle] <= nums[right]) right = middle;
        else left = middle;
    }
}

assert.equal(findMin([3, 4, 5, 1, 2]), 1);
assert.equal(findMin([4, 5, 6, 7, 0, 1, 2]), 0);
assert.equal(findMin([11, 13, 15, 17]), 11);
