import assert from "node:assert";

function rotateString(s: string, goal: string): boolean {
    return (s + s).includes(goal) && goal.length == s.length;
}

assert(rotateString("abcde", "cdeab"));
assert(!rotateString("abcde", "abced"));
