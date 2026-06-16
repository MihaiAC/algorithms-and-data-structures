import assert from "node:assert";

function processStr(s: string): string {
    let result: string[] = [];

    for (const letter of s) {
        if (letter == "*") {
            if (result.length > 0) result.pop();
        } else if (letter == "#") result = [...result, ...result];
        else if (letter == "%") result.reverse();
        else result.push(letter);
    }

    return result.join("");
}

assert.equal(processStr("a#b%*"), "ba");
assert.equal(processStr("z*#"), "");
assert.equal(processStr("*%"), "");
