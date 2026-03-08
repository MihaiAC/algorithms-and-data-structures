import assert from "node:assert";

const opp = {
    "0": "1",
    "1": "0",
};

function findDifferentBinaryString(nums: string[]): string {
    let diff = [];

    const N = nums.length;
    for (let idx = 0; idx < N; idx++) {
        diff.push(opp[nums[idx]![idx]! as "0" | "1"]);
    }

    return diff.join("");
}

assert.equal(findDifferentBinaryString(["01", "10"]), "11");
assert.equal(findDifferentBinaryString(["00", "01"]), "10");
assert.equal(findDifferentBinaryString(["111", "011", "001"]), "000");
