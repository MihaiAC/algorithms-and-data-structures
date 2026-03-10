import assert from "node:assert";

const LETTERS = ["abc", "ab", "bc", "ac", "a", "b", "c"];

function lettersToKey(letters: string, count: number[]): string {
    switch (letters) {
        case "abc":
            return toKey("abc", [count[0]! - count[1]!, count[0]! - count[2]!]);
        case "ab":
            return toKey("ab", [count[0]! - count[1]!, count[2]!]);
        case "bc":
            return toKey("bc", [count[1]! - count[2]!, count[0]!]);
        case "ac":
            return toKey("ac", [count[0]! - count[2]!, count[1]!]);
        case "a":
            return toKey("a", [count[1]!, count[2]!]);
        case "b":
            return toKey("b", [count[0]!, count[2]!]);
        default:
            return toKey("c", [count[0]!, count[1]!]);
    }
}

function toKey(letters: string, nums: number[]): string {
    return "(" + letters + "," + nums.join(",") + ")";
}

function longestBalanced(s: string): number {
    let ans = 0;
    const count = new Array<number>(3).fill(0);
    const firstIndex = new Map<string, number>();

    for (const letters of LETTERS) {
        firstIndex.set(lettersToKey(letters, count), -1);
    }

    for (let idx = 0; idx < s.length; idx++) {
        count[s.charCodeAt(idx) - "a".charCodeAt(0)] += 1;
        for (const letters of LETTERS) {
            const key = lettersToKey(letters, count);
            if (firstIndex.has(key)) {
                ans = Math.max(ans, idx - firstIndex.get(key)!);
            } else {
                firstIndex.set(key, idx);
            }
        }
    }

    return ans;
}

assert.equal(longestBalanced("abbac"), 4);
assert.equal(longestBalanced("aabcc"), 3);
assert.equal(longestBalanced("aba"), 2);
