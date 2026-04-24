import assert from "node:assert";

function furthestDistanceFromOrigin(moves: string): number {
    let [left, right, underscore] = [0, 0, 0];

    for (const move of moves) {
        switch (move) {
            case "L":
                left += 1;
                break;
            case "R":
                right += 1;
                break;
            default:
                underscore += 1;
        }
    }

    return Math.max(left, right) - Math.min(left, right) + underscore;
}

assert.equal(furthestDistanceFromOrigin("L_RL__R"), 3);
assert.equal(furthestDistanceFromOrigin("_R__LL_"), 5);
assert.equal(furthestDistanceFromOrigin("_______"), 7);
