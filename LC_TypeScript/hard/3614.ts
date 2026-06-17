import assert from "node:assert";

function processStr(s: string, k: number): string {
    let currLen = 0;

    for (const letter of s) {
        switch (letter) {
            case "#":
                currLen *= 2;
                break;
            case "*":
                currLen = Math.max(0, currLen - 1);
                break;
            case "%":
                break;
            default:
                currLen += 1;
                break;
        }
    }

    if (k >= currLen) return ".";

    for (let idx = s.length - 1; idx >= 0; idx--) {
        const letter = s[idx];
        switch (letter) {
            case "*":
                currLen += 1;
                break;
            case "#":
                const half = Math.ceil(currLen / 2);
                if (k + 1 > half) k -= half;
                currLen = half;
                break;
            case "%":
                k = currLen - k - 1;
                break;
            default:
                if (k + 1 === currLen) return letter;
                currLen -= 1;
                break;
        }
    }

    return "Shouldn't be reached.";
}

assert.equal(processStr("a#b%*", 1), "a");
assert.equal(processStr("cd%#*#", 3), "d");
