import { Queue } from "datastructures-js";
import assert from "node:assert";

type Delta = {
    dx: number;
    dy: number;
};

type Direction = "left" | "right" | "up" | "down";

const toDelta: Record<Direction, Delta> = {
    left: { dx: 0, dy: -1 },
    right: { dx: 0, dy: +1 },
    up: { dx: -1, dy: 0 },
    down: { dx: 1, dy: 0 },
};

const moves: Record<number, Direction[]> = {
    1: ["left", "right"],
    2: ["up", "down"],
    3: ["left", "down"],
    4: ["down", "right"],
    5: ["left", "up"],
    6: ["up", "right"],
};

const opposite: Record<Direction, Direction> = {
    down: "up",
    up: "down",
    left: "right",
    right: "left",
};

function coordsToString(x: number, y: number): string {
    return `${x},${y}`;
}

function hasValidPath(grid: number[][]): boolean {
    const [M, N] = [grid.length, grid[0].length];
    if (M === 1 && N === 1) return true;

    const within_bounds = (x: number, y: number): boolean =>
        x >= 0 && y >= 0 && x < M && y < N;

    const visited = new Set<string>();
    visited.add(coordsToString(0, 0));

    const queue = new Queue<number[]>();
    queue.enqueue([0, 0]);

    while (queue.size() > 0) {
        const [cx, cy] = queue.dequeue()!;

        for (const direction of moves[grid[cx][cy]]) {
            const { dx, dy } = toDelta[direction];
            const [nx, ny] = [cx + dx, cy + dy];
            if (
                within_bounds(nx, ny) &&
                !visited.has(coordsToString(nx, ny)) &&
                moves[grid[nx][ny]].some((val) => opposite[val] === direction)
            ) {
                if (nx === M - 1 && ny === N - 1) return true;
                visited.add(coordsToString(nx, ny));
                queue.enqueue([nx, ny]);
            }
        }
    }

    return false;
}

assert.equal(
    hasValidPath([
        [2, 4, 3],
        [6, 5, 2],
    ]),
    true
);

assert.equal(
    hasValidPath([
        [1, 2, 1],
        [1, 2, 1],
    ]),
    false
);

assert.equal(hasValidPath([[1, 1, 2]]), false);
