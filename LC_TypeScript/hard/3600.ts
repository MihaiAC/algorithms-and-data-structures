import { MinHeap } from "datastructures-js";
import assert from "node:assert";

function maxStability(n: number, edges: number[][], k: number): number {
    const selectedEdges = new MinHeap<[number, number]>((elem) => elem[0]);

    const group = Array.from<number>({ length: n }).map((_, idx) => idx);
    const size = Array.from<number>({ length: n }).fill(1);

    // Find
    function find(u: number): number {
        if (u === group[u]) return u;
        group[u] = find(group[u]);
        return group[u];
    }

    // Union
    function union(u: number, v: number) {
        let g1 = find(u);
        let g2 = find(v);

        if (g1 !== g2) {
            if (size[g1]! > size[g2]!) [g1, g2] = [g2, g1];
            group[g1] = g2;
            size[g2] += size[g1]!;
        }
    }

    // Go through all edges.
    // must = 1 => add to heap + union.
    // must = 0 => add to nonMustEdges
    const nonMustEdges: number[][] = [];
    for (const edge of edges) {
        const [u, v, weight, must] = edge;
        if (must === 1) {
            // Sanity check
            if (find(u) === find(v)) return -1; // no longer a tree
            union(u, v);
            selectedEdges.insert([weight, must]);
        } else {
            nonMustEdges.push(edge);
        }
    }

    // Sort must=0 edges in decreasing order of their weight
    nonMustEdges.sort((a, b) => b[2] - a[2]);

    // Go through must=0 edges until we have a tree.
    for (const [u, v, weight, _] of nonMustEdges) {
        // Skip if u, v are already in the same group.
        if (find(u) === find(v)) continue;

        union(u, v);
        selectedEdges.insert([weight, 0]);
    }

    // Check that every node belongs to the same group.
    const root = find(0);
    if (group.find((edge) => find(edge) !== root) !== undefined) return -1;

    // Calculate max stability.
    while (selectedEdges.top()![1] !== 1 && k > 0) {
        const [weight, must] = selectedEdges.pop()!;
        selectedEdges.insert([weight * 2, 1]);
        k--;
    }

    return selectedEdges.top()![0];
}

assert.equal(
    maxStability(
        3,
        [
            [0, 1, 4, 0],
            [1, 2, 3, 0],
            [0, 2, 1, 0],
        ],
        2
    ),
    6
);
assert.equal(
    maxStability(
        3,
        [
            [0, 1, 1, 1],
            [1, 2, 1, 1],
            [2, 0, 1, 1],
        ],
        0
    ),
    -1
);
assert.equal(
    maxStability(
        5,
        [
            [0, 1, 2077, 0],
            [2, 4, 31376, 1],
            [3, 4, 36289, 0],
            [0, 3, 78084, 1],
            [2, 3, 89506, 1],
            [0, 2, 82142, 0],
        ],
        5
    ),
    4154
);
