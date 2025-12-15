import assert from "node:assert";

function plusOne(digits: number[]): number[] {
    const ans: number[] = [];
    let carry = 1;
    while (digits.length > 0) {
        const res = digits.pop()! + carry;
        if (res >= 10) {
            ans.push(res - 10);
            carry = 1;
        } else {
            ans.push(res);
            carry = 0;
        }
    }

    if (carry > 0) {
        ans.push(carry);
    }

    return ans.reverse();
}

assert.deepEqual(plusOne([9]), [1, 0]);
assert.deepEqual(plusOne([1, 2, 3]), [1, 2, 4]);
