import { toNumber } from "lodash";
import assert from "node:assert";

function toKey(row: number, glass: number): string {
    return [row, glass].join(",");
}

function champagneTower(poured: number, queryRow: number, queryGlass: number): number {
    const isAncestor = (row: number, glass: number): boolean =>
        queryGlass >= glass && queryGlass <= glass + queryRow - row;

    let toFill = new Map<string, number>();
    toFill.set(toKey(0, 0), poured);

    // Simulation
    for (let _ii = 0; _ii < queryRow; _ii++) {
        const nextToFill = new Map<string, number>();
        for (const key of toFill.keys()) {
            const [row, glass] = key.split(",").map((x) => toNumber(x));

            const overflow = (toFill.get(key)! - 1) / 2;
            if (overflow <= 0) continue;

            let nextKey = "";
            for (const [x, y] of [
                [row + 1, glass],
                [row + 1, glass + 1],
            ]) {
                if (isAncestor(x, y)) {
                    const nextKey = toKey(x, y);
                    nextToFill.set(nextKey, (nextToFill.get(nextKey) || 0) + overflow);
                }
            }
        }

        toFill = nextToFill;
    }

    return Math.min(1, toFill.get(toKey(queryRow, queryGlass)) ?? 0);
}

function isClose(x: number, y: number, epsilon = 1e-3): boolean {
    return Math.abs(x - y) <= epsilon;
}

assert(isClose(champagneTower(1, 1, 1), 0));
assert(isClose(champagneTower(2, 1, 1), 0.5));
assert(isClose(champagneTower(100000009, 33, 17), 1));
