import { MinHeap } from "datastructures-js";

function kSmallestPairs(nums1: number[], nums2: number[], k: number): number[][] {
    const res: number[][] = [];

    const N1 = nums1.length;
    const N2 = nums2.length;

    const visited = new Set<string>();
    visited.add("0, 0");

    const heap = new MinHeap<{ sum: number; idx1: number; idx2: number }>(
        (item) => item.sum
    );

    heap.push({ sum: nums1[0] + nums2[0], idx1: 0, idx2: 0 });

    const getKey = (k1: number, k2: number) => `${k1},${k2}`;
    while (res.length < k && heap.size() > 0) {
        const { idx1, idx2 } = heap.extractRoot()!;
        res.push([nums1[idx1], nums2[idx2]]);

        if (idx1 < N1 - 1 && !visited.has(getKey(idx1 + 1, idx2))) {
            heap.push({ sum: nums1[idx1 + 1] + nums2[idx2], idx1: idx1 + 1, idx2: idx2 });
            visited.add(getKey(idx1 + 1, idx2));
        }

        if (idx2 < N2 - 1 && !visited.has(getKey(idx1, idx2 + 1))) {
            heap.push({ sum: nums1[idx1] + nums2[idx2 + 1], idx1: idx1, idx2: idx2 + 1 });
            visited.add(getKey(idx1, idx2 + 1));
        }
    }

    return res;
}
