import assert from "node:assert";

const map: Record<string, number[]> = {
    U: [0, 1],
    D: [0, -1],
    L: [1, 0],
    R: [-1, 0],
};

function judgeCircle(moves: string): boolean {
    const leftUp = [0, 0];

    for (const move of moves) {
        const [dx, dy] = map[move]!;
        leftUp[0] += dx;
        leftUp[1] += dy;
    }

    return leftUp[0] === 0 && leftUp[1] === 0;
}

assert.equal(judgeCircle("UD"), true);
assert.equal(judgeCircle("LL"), false);
