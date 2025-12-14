import assert from "node:assert";

function buildArray(target: number[], n: number): string[] {
    let curr_idx = 0;
    let ans = [];

    for (let num = 1; num <= n && curr_idx < target.length; num++) {
        ans.push("Push");
        if (target[curr_idx] == num) {
            curr_idx += 1;
        } else {
            ans.push("Pop");
        }
    }

    return ans;
}

assert.deepEqual(buildArray([1, 3], 3), ["Push", "Push", "Pop", "Push"]);
assert.deepEqual(buildArray([1, 2, 3], 3), ["Push", "Push", "Push"]);
assert.deepEqual(buildArray([1, 2], 4), ["Push", "Push"]);
