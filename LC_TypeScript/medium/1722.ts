import assert from "node:assert";

class DSU {
    parent: number[] = [];
    size: number[] = [];

    constructor(n: number) {
        this.parent = [...Array(n).keys()];
        this.size = Array.from<number>({ length: n }).fill(1);
    }

    findRoot(node: number): number {
        if (node === this.parent[node]) {
            return node;
        }

        const root = this.findRoot(this.parent[node]);
        this.parent[node] = root;
        return root;
    }

    union(n1: number, n2: number) {
        n1 = this.findRoot(n1);
        n2 = this.findRoot(n2);

        if (n1 === n2) {
            return;
        }

        if (this.size[n1] > this.size[n2]) {
            [n1, n2] = [n2, n1];
        }

        this.size[n2] += this.size[n1];
        this.parent[n1] = n2;
    }
}

class Counter {
    counter: Map<number, number>;

    constructor() {
        this.counter = new Map<number, number>();
    }

    increment(num: number) {
        if (this.counter.has(num)) {
            this.counter.set(num, 1 + this.counter.get(num)!);
        } else {
            this.counter.set(num, 1);
        }
    }

    decrement(num: number) {
        if (this.counter.has(num)) {
            this.counter.set(num, this.counter.get(num)! - 1);
        } else {
            this.counter.set(num, -1);
        }
    }

    getAbsCountSum(): number {
        let sum = 0;
        for (const count of this.counter.values()) {
            sum += Math.abs(count);
        }

        return sum;
    }
}

function minimumHammingDistance(
    source: number[],
    target: number[],
    allowedSwaps: number[][]
): number {
    const N = source.length;
    const dsu = new DSU(N);

    for (const [u, v] of allowedSwaps) {
        dsu.union(u, v);
    }

    const rootToCounts = new Map<number, Counter>();

    for (let idx = 0; idx < N; idx++) {
        const root = dsu.findRoot(idx);
        if (!rootToCounts.has(root)) {
            rootToCounts.set(root, new Counter());
        }

        rootToCounts.get(root)!.increment(source[idx]);
        rootToCounts.get(root)!.decrement(target[idx]);
    }

    let minDist = 0;
    for (const root of rootToCounts.keys()) {
        minDist += rootToCounts.get(root)!.getAbsCountSum() / 2;
    }

    return minDist;
}

assert.equal(
    minimumHammingDistance(
        [1, 2, 3, 4],
        [2, 1, 4, 5],
        [
            [0, 1],
            [2, 3],
        ]
    ),
    1
);

assert.equal(minimumHammingDistance([1, 2, 3, 4], [1, 3, 2, 4], []), 2);
assert.equal(
    minimumHammingDistance(
        [5, 1, 2, 4, 3],
        [1, 5, 4, 2, 3],
        [
            [0, 4],
            [4, 2],
            [1, 3],
            [1, 4],
        ]
    ),
    0
);

assert.equal(
    minimumHammingDistance(
        [1, 1, 1],
        [2, 2, 2],
        [
            [0, 1],
            [1, 2],
        ]
    ),
    3
);
