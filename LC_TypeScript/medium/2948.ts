import assert from "node:assert";

function lexicographicallySmallestArray(nums: number[], limit: number): number[] {
    const N = nums.length;

    let ans = Array.from<number>({ length: N }).fill(0);

    let numsWithIdx = nums.map((num, idx) => [num, idx]);
    numsWithIdx.sort((a, b) => a[0] - b[0]);

    const add = (start_idx: number, curr_idx: number) => {
        let indices = numsWithIdx.slice(start_idx, curr_idx + 1).map((x) => x[1]);
        indices.sort((a, b) => a - b);
        indices.map((idx, dx) => (ans[idx] = numsWithIdx[start_idx + dx][0]));
    };

    let start_idx = 0;
    for (let curr_idx = 0; curr_idx < N - 1; curr_idx++) {
        if (numsWithIdx[curr_idx + 1][0] - numsWithIdx[curr_idx][0] > limit) {
            add(start_idx, curr_idx);
            start_idx = curr_idx + 1;
        }
    }
    add(start_idx, N - 1);

    return ans;
}

assert.deepEqual(lexicographicallySmallestArray([1, 5, 3, 9, 8], 2), [1, 3, 5, 8, 9]);
assert.deepEqual(
    lexicographicallySmallestArray([1, 7, 6, 18, 2, 1], 3),
    [1, 6, 7, 18, 1, 2]
);
assert.deepEqual(
    lexicographicallySmallestArray([1, 7, 28, 19, 10], 3),
    [1, 7, 28, 19, 10]
);
