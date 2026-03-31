import assert from "node:assert";

function waysToMakeFair(nums: number[]): number {
    let [evenSum, oddSum] = [0, 0];
    for (let idx = 0; idx < nums.length; idx++) {
        if (idx % 2 === 0) evenSum += nums[idx];
        else oddSum += nums[idx];
    }

    let nWays = 0;
    let [currEvenSum, currOddSum] = [0, 0];
    for (let idx = 0; idx < nums.length; idx++) {
        const [remEven, remOdd] = idx % 2 === 0
            ? [evenSum - currEvenSum - nums[idx], oddSum - currOddSum]
            : [evenSum - currEvenSum, oddSum - currOddSum - nums[idx]];

        if (currEvenSum + remOdd === currOddSum + remEven) nWays += 1;

        if (idx % 2 === 0) currEvenSum += nums[idx];
        else currOddSum += nums[idx];
    }

    return nWays;
}

assert.equal(waysToMakeFair([2, 1, 6, 4]), 1);
assert.equal(waysToMakeFair([1, 1, 1]), 3);
assert.equal(waysToMakeFair([1, 2, 3]), 0);
