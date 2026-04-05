import assert from "node:assert";

function judgeCircle(moves: string): boolean {
    let [dx, dy] = [0, 0];

    for (const move of moves) {
        if (move === "U") dy++;
        else if (move === "D") dy--;
        else if (move === "L") dx--;
        else dx++;
    }

    return dx === 0 && dy === 0;
}

assert.equal(judgeCircle("UD"), true);
assert.equal(judgeCircle("LL"), false);
