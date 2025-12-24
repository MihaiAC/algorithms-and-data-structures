import * as fs from "fs";

type Point = [number, number, number];

function readInput(fileName: string): Point[] {
    const lines = fs.readFileSync(fileName, "utf8").split(/\r?\n/);
    const points: Point[] = [];

    for (const line of lines) {
        const point = line.split(",").map((x) => Number(x));
        const allNumbers = point.reduce(
            (prev: boolean, curr: number) => prev && Number.isFinite(curr),
            true
        );

        if (point.length !== 3 || !allNumbers) {
            throw new Error(`Incorrect input: ${line}`);
        }

        points.push(point as Point);
    }

    return points;
}

function solve(points: Point[], limit: number, p2: boolean = false): number {
    const calculateDist = (p1: Point, p2: Point): number => {
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2;
    };

    const N: number = points.length;

    // Calculate distances, save as [dist, id1, id2], sort by dist asc
    const dists: Point[] = [];

    for (let idx1 = 0; idx1 < N - 1; idx1++) {
        const p1 = points[idx1];
        for (let idx2 = idx1 + 1; idx2 < N; idx2++) {
            const p2 = points[idx2];
            dists.push([calculateDist(p1, p2), idx1, idx2]);
        }
    }

    dists.sort((p1, p2) => p1[0] - p2[0]);

    // Union find
    const parent = [...Array(N).keys()];
    const size = Array(N).fill(1);

    const find = (node: number): number => {
        if (node === parent[node]) {
            return node;
        }

        const set = find(parent[node]);

        parent[node] = set;
        return set;
    };

    const union = (node1: number, node2: number): number => {
        let set1 = find(node1);
        let set2 = find(node2);

        if (set1 === set2) {
            return set1;
        }

        if (size[set1] < size[set2]) {
            [set1, set2] = [set2, set1];
        }

        parent[set2] = set1;
        size[set1] += size[set2];

        return set1;
    };

    let maxIter = Math.min(limit, dists.length);
    if (p2) {
        maxIter = dists.length;
    }

    for (let idx = 0; idx < maxIter; idx++) {
        const [_, idx1, idx2] = dists[idx];
        const root = union(idx1, idx2);

        if (p2 && size[root] === N) {
            return points[idx1][0] * points[idx2][0];
        }
    }

    // Gather groups + sort
    const groups = new Map<number, number>();
    for (let idx = 0; idx < N; idx++) {
        const root = find(idx);
        if (!groups.has(root)) {
            groups.set(root, size[root]);
        }
    }

    const sizes = Array.from(groups.values()).sort((a, b) => b - a);
    if (sizes.length < 3)
        throw new Error(`sizes has length ${sizes.length}, expected >3`);

    console.log(sizes);
    return sizes[0] * sizes[1] * sizes[2];
}

const example = readInput("d8-example.txt");
console.log(solve(example, 10));
console.log(solve(example, 10, true));

const input = readInput("d8-input.txt");
console.log(solve(input, 1000));
console.log(solve(input, 1000, true));
