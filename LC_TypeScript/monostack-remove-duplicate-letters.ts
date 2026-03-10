import assert from "node:assert";

function removeDuplicateLetters(s: string): string {
    const selected = new Set();
    const lastIdx = new Map<string, number>();
    const stack: string[] = [];

    for (let idx = 0; idx < s.length; idx++) {
        lastIdx.set(s[idx], idx);
    }

    for (let idx = 0; idx < s.length; idx++) {
        const letter = s[idx];
        if (selected.has(letter)) {
            continue;
        }

        while (
            stack.length > 0 &&
            letter < stack.at(-1)! &&
            idx < lastIdx.get(stack.at(-1)!)!
        ) {
            selected.delete(stack.pop()!);
        }

        selected.add(letter);
        stack.push(letter);
    }

    return stack.join("");
}

assert.equal(removeDuplicateLetters("bcabc"), "abc");
assert.equal(removeDuplicateLetters("cbacdcbc"), "acdb");
