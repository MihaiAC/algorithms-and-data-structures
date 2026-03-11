import assert from "node:assert";

function shuffle(nums: number[], n: number): number[] {
    const FLAT = 1001;
    for (let idx = 0; idx < n; idx += 1) {
        if (nums[idx] >= FLAT) {
            continue;
        }
        let next_idx = idx,
            aux = nums[idx];
        while (true) {
            const prev_idx = next_idx;
            if (next_idx < n) {
                next_idx = 2 * next_idx;
            } else {
                next_idx = 2 * (next_idx - n) + 1;
            }

            const temp = nums[next_idx] % FLAT;
            nums[next_idx] = aux + FLAT;
            aux = temp;

            if (next_idx === idx) {
                break;
            }
        }
    }

    for (let i = 0; i < 2 * n; i++) {
        nums[i] %= FLAT;
    }

    return nums;
}

const nums1 = [2, 5, 1, 3, 4, 7];
const n1 = 3;
assert.deepEqual([2, 3, 5, 4, 1, 7], shuffle(nums1, n1));
