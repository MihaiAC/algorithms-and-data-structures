import assert from "node:assert";

const nextSmallest: Record<string, string> = {
    a: "b",
    b: "a",
    c: "a",
};

const nextLargest: Record<string, string> = {
    a: "c",
    b: "c",
    c: "b",
};

function getHappyString(n: number, k: number): string {
    if (k > 3 * 2 ** (n - 1)) return "";

    const happyString: string[] = [];
    if (k <= 2 ** (n - 1)) {
        happyString.push("a");
        k -= 1;
    } else if (k <= 2 ** n) {
        happyString.push("b");
        k = k - 1 - 2 ** (n - 1);
    } else {
        happyString.push("c");
        k = k - 1 - 2 ** n;
    }

    for (let idx = 1; idx < n; idx++) {
        const mid = 2 ** (n - idx - 1);

        if (k < mid) happyString.push(nextSmallest[happyString.at(-1)!]);
        else {
            happyString.push(nextLargest[happyString.at(-1)!]);
            k -= mid;
        }
    }

    return happyString.join("");
}

assert.equal(getHappyString(1, 3), "c");
assert.equal(getHappyString(1, 4), "");
assert.equal(getHappyString(3, 9), "cab");
