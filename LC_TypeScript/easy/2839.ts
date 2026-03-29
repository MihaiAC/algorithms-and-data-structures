import assert from "node:assert";

function canBeEqual(s1: string, s2: string): boolean {
    const e1 = [s1[0]!, s1[2]!];
    const o1 = [s1[1]!, s1[3]!];

    const e2 = [s2[0]!, s2[2]!];
    const o2 = [s2[1]!, s2[3]!];

    return (
        e1.sort().join("") === e2.sort().join("") &&
        o1.sort().join("") === o2.sort().join("")
    );
}

assert(canBeEqual("abcd", "cdab"));
assert(!canBeEqual("abcd", "dacb"));
