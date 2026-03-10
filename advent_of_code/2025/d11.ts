import { Queue } from "datastructures-js";
import * as fs from "fs";

function buildAdjMatrix(fileName: string): Map<string, string[]> {
    const lines = fs.readFileSync(fileName, "utf8").split(/\r+\n/);
    const adjMatrix = new Map<string, string[]>();

    for (const line of lines) {
        const [fromNode, toNodes] = line.split(": ");
        adjMatrix.set(fromNode, toNodes.split(" "));
    }

    return adjMatrix;
}

function p1(
    adjMatrix: Map<string, string[]>,
    startNode: string = "you",
    endNode: string = "out"
): number {
    // Find all nodes reachable from "you"
    const reachable = new Set<string>();
    reachable.add(startNode);

    const dfsQueue = [startNode];

    while (dfsQueue.length > 0) {
        const node = dfsQueue.pop()!;

        for (const neighbor of adjMatrix.get(node) || []) {
            if (!reachable.has(neighbor)) {
                reachable.add(neighbor);
                dfsQueue.push(neighbor);
            }
        }
    }

    // Calculate in degree for each reachable node (only counting edges within reachable subgraph)
    const inDegree = new Map<string, number>();
    for (const node of reachable) {
        if (!inDegree.has(node)) inDegree.set(node, 0);

        for (const neighbor of adjMatrix.get(node) || []) {
            if (reachable.has(neighbor)) {
                inDegree.set(neighbor, (inDegree.get(neighbor) || 0) + 1);
            }
        }
    }

    // Topological sort starting from "you"
    const queue = new Queue<string>();
    queue.enqueue(startNode);

    const orderedNodes = [];
    while (!queue.isEmpty()) {
        const node = queue.dequeue()!;
        orderedNodes.push(node);

        for (const neighbor of adjMatrix.get(node) || []) {
            if (!reachable.has(neighbor)) continue;
            inDegree.set(neighbor, inDegree.get(neighbor)! - 1);
            if (inDegree.get(neighbor) === 0) {
                queue.enqueue(neighbor);
            }
        }
    }

    // Count ways to reach each node
    let ways = new Map<string, number>();
    ways.set(startNode, 1);

    // Traverse in topological order
    for (const node of orderedNodes) {
        for (const neighbor of adjMatrix.get(node) || []) {
            if (reachable.has(neighbor)) {
                ways.set(neighbor, (ways.get(neighbor) || 0) + (ways.get(node) || 0));
            }
        }
    }

    return ways.get(endNode) || 0;
}

const exampleAdj = buildAdjMatrix("d11-example.txt");
const inputAdj = buildAdjMatrix("d11-input.txt");

console.log(p1(exampleAdj));
console.log(p1(inputAdj));

const exampleAdj2 = buildAdjMatrix("d11-example2.txt");
// No routes from 'dac' to 'fft'
console.log(
    p1(exampleAdj2, "svr", "fft") *
        p1(exampleAdj2, "fft", "dac") *
        p1(exampleAdj2, "dac", "out")
);

// HURR DURR IT WORKED
console.log(
    p1(inputAdj, "svr", "fft") * p1(inputAdj, "fft", "dac") * p1(inputAdj, "dac", "out")
);
