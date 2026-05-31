import assert from "node:assert";

function asteroidsDestroyed(mass: number, asteroids: number[]): boolean {
    asteroids.sort((a, b) => a - b);
    for (const asteroid of asteroids) {
        if (asteroid > mass) return false;
        mass += asteroid;
    }

    return true;
}

assert.equal(asteroidsDestroyed(10, [3, 9, 19, 5, 21]), true);
assert.equal(asteroidsDestroyed(5, [4, 9, 23, 4]), false);
