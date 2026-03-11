import assert from "node:assert";

function pyramidTransition(bottom: string, allowed: string[]): boolean {
    const allowedMap = new Map<string, string[]>();
    allowed.map((x: string) => {
        const key = x[0]! + x[1]!;
        const arr = allowedMap.get(key) || [];

        arr.push(x[2]!);
        allowedMap.set(key, arr);
    });

    const dp = (idx: number, prev: string, curr: string): boolean => {
        if (idx === prev.length - 1) {
            return dp(0, curr, "");
        }

        if (prev.length === 2) {
            return allowedMap.has(prev[0] + prev[1]);
        }

        const key = prev[idx]! + prev[idx + 1]!;
        if (!allowedMap.has(key)) return false;
        for (const letter of allowedMap.get(key)!) {
            if (dp(idx + 1, prev, curr + letter)) return true;
        }

        return false;
    };

    return dp(0, bottom, "");
}

const bottom1 = "BCD";
const allowed1 = ["BCC", "CDE", "CEA", "FFF"];
assert.equal(pyramidTransition(bottom1, allowed1), true);

const bottom2 = "AAAA";
const allowed2 = ["AAB", "AAC", "BCD", "BBE", "DEF"];
assert.equal(pyramidTransition(bottom2, allowed2), false);
