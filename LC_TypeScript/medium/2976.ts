import assert from "node:assert";

function charToInt(c: string): number {
    return c.charCodeAt(0) - 97;
}

function minimumCost(
    source: string,
    target: string,
    original: string[],
    changed: string[],
    cost: number[]
): number {
    const minCost: number[][] = Array.from({ length: 26 }, () =>
        Array(26).fill(Infinity)
    );

    for (let code = 0; code < 26; code++) {
        minCost[code][code] = 0;
    }

    for (let idx = 0; idx < original.length; idx++) {
        const origCode = charToInt(original[idx]);
        const changedCode = charToInt(changed[idx]!);

        minCost[origCode][changedCode] = Math.min(
            minCost[origCode][changedCode],
            cost[idx]!
        );
    }

    // Floyd-Warshall.
    for (let kk = 0; kk < 26; kk++) {
        for (let ii = 0; ii < 26; ii++) {
            for (let jj = 0; jj < 26; jj++) {
                if (minCost[ii][jj] > minCost[ii][kk] + minCost[kk][jj]) {
                    minCost[ii][jj] = minCost[ii][kk] + minCost[kk][jj];
                }
            }
        }
    }

    let ans = 0;
    for (let idx = 0; idx < source.length; idx++) {
        const sourceCode = charToInt(source[idx]);
        const targetCode = charToInt(target[idx]);

        if (minCost[sourceCode][targetCode] === Infinity) return -1;
        ans += minCost[sourceCode][targetCode];
    }

    return ans;
}

const source = "aaaa";
const target = "bbbb";
const original = ["a", "c"];
const changed = ["c", "b"];
const cost = [1, 2];
assert.equal(minimumCost(source, target, original, changed, cost), 12);
