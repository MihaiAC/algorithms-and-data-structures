/** Used to efficiently convert strings to IDs. */
class Trie {
    child: (Trie | null)[];
    id: number;

    constructor() {
        this.child = new Array(26).fill(null);
        this.id = -1;
    }
}

/** Add word to trie and return its ID. */
function add(node: Trie, word: string, counter: { value: number }): number {
    for (const c of word) {
        const code = charToInt(c);

        if (!node.child[code]) {
            node.child[code] = new Trie();
        }

        node = node.child[code]!;
    }

    if (node.id === -1) {
        counter.value++;
        node.id = counter.value;
    }

    return node.id;
}

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
    const M: number = source.length;
    const N: number = original.length;

    const root: Trie = new Trie();

    const counter = { value: -1 };
    const nodeCount: number = N * 2;

    // Floyd-Warshall.
    const G: number[][] = Array.from({ length: nodeCount }, () =>
        Array(nodeCount).fill(Infinity)
    );

    for (let idx = 0; idx < nodeCount; idx++) {
        G[idx][idx] = 0;
    }

    for (let idx = 0; idx < N; idx++) {
        const x: number = add(root, original[idx], counter);
        const y: number = add(root, changed[idx], counter);

        G[x][y] = Math.min(G[x][y], cost[idx]);
    }

    const size: number = counter.value + 1;
    for (let kk = 0; kk < size; kk++) {
        for (let ii = 0; ii < size; ii++) {
            for (let jj = 0; jj < size; jj++) {
                G[ii][jj] = Math.min(G[ii][jj], G[ii][kk] + G[kk][jj]);
            }
        }
    }

    // DP + use the computed min distances.
    // dp[ii] = minimum cost to transform source[0..ii] into
    // target[0..ii]
    const dp: number[] = new Array(M).fill(-1);
    for (let ii = 0; ii < M; ii++) {
        // Skip if we couldn't transform dp[ii-1].
        if (ii > 0 && dp[ii - 1] === -1) {
            continue;
        }

        // Free match.
        const base: number = ii === 0 ? 0 : dp[ii - 1];
        if (source[ii] === target[ii]) {
            if (dp[ii] === -1 || base < dp[ii]) {
                dp[ii] = base;
            }
        }

        // Try replacing source[ii..jj] with target[ii..jj].
        let u: Trie | null = root;
        let v: Trie | null = root;
        for (let jj = ii; jj < M; jj++) {
            u = u?.child[charToInt(source[jj])] ?? null;
            v = v?.child[charToInt(target[jj])] ?? null;

            if (!u || !v) {
                break;
            }

            if (u.id !== -1 && v.id !== -1 && G[u.id][v.id] !== Infinity) {
                const newVal: number = base + G[u.id][v.id];

                if (dp[jj] === -1 || newVal < dp[jj]) {
                    dp[jj] = newVal;
                }
            }
        }
    }

    return dp[M - 1];
}
