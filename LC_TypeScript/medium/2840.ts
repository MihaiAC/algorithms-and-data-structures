import assert from "node:assert";

function checkStrings(s1: string, s2: string): boolean {
    const [e1, o1]: [string[], string[]] = [[], []];
    const [e2, o2]: [string[], string[]] = [[], []];

    const extract = (s: string, e: string[], o: string[]) => {
        Array.from(s).map((letter: string, idx: number) => {
            if (idx % 2 === 0) e.push(letter);
            else o.push(letter);
        });
    };

    const checkEq = (a1: string[], a2: string[]): boolean =>
        a1.sort().join("") === a2.sort().join("");

    extract(s1, e1, o1);
    extract(s2, e2, o2);

    return checkEq(e1, e2) && checkEq(o1, o2);
}

assert(checkStrings("abcdba", "cabdab"));
assert(!checkStrings("abe", "bea"));
