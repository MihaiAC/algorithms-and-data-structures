import { MinPriorityQueue } from "datastructures-js";

function minCost(n: number, edges: number[][]): number {
    const neighbours = new Map<number, [number, number][]>();
    for (const edge of edges) {
        const [u, v, w] = edge;

        if (!neighbours.has(u)) neighbours.set(u, []);
        neighbours.get(u)!.push([v, w]);

        if (!neighbours.has(v)) neighbours.set(v, []);
        neighbours.get(v)!.push([u, 2 * w]);
    }

    const cost: number[] = Array(n).fill(Infinity);
    cost[0] = 0;

    const pq = new MinPriorityQueue((item: number[]) => item[1]);
    pq.enqueue([0, 0]);

    while (!pq.isEmpty()) {
        const [currNode, currDist] = pq.dequeue()!;

        if (currNode === n - 1) return currDist;
        if (currDist > cost[currNode]) continue;

        for (const [nextNode, edgeCost] of neighbours.get(currNode) || []) {
            const nextDist = currDist + edgeCost;
            if (nextDist < cost[nextNode]) {
                cost[nextNode] = nextDist;
                pq.enqueue([nextNode, nextDist]);
            }
        }
    }

    return cost[n - 1] !== Infinity ? cost[n - 1] : -1;
}
