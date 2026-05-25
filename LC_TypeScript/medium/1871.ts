import assert from "node:assert";

function canReach(s: string, minJump: number, maxJump: number): boolean {
    const N = s.length;

    if (s[N - 1] === "1") return false;

    const deltas = new Array<number>(N).fill(0);
    let currDelta = 0;
    for (let idx = 0; idx < N; idx++) {
        currDelta += deltas[idx];
        if ((currDelta > 0 || idx == 0) && s[idx] === "0") {
            if (idx + minJump < N) deltas[idx + minJump] += 1;
            if (idx + maxJump + 1 < N) deltas[idx + maxJump + 1] -= 1;
        }
    }

    return currDelta > 0;
}

assert.equal(canReach("011010", 2, 3), true);
assert.equal(canReach("01101110", 2, 3), false);
assert.equal(canReach("01101110", 2, 4), true);
assert.equal(canReach("01101111", 2, 4), false);
