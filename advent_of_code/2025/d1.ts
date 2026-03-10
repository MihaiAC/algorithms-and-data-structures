import assert from "assert";
import * as fs from "fs";

/**
 * Brings x into the 0-99 range.
 * @param x
 */
function normalize(x: number): number {
    while (x < 0) {
        x += 100;
    }
    return x % 100;
}

/**
 * Brings x into the 0-99 range, counting the number of
 * times it crosses 0.
 * @param x
 * @returns [normalized_x, count]
 */
function normalizeAndCount(x: number): [number, number] {
    let count = 0;
    while (x < 0) {
        x += 100;
        count += 1;
    }

    count += Math.floor(x / 100);
    return [x % 100, count];
}

function p1(rotations: string[]): number {
    let count = 0;
    let curr = 50;

    for (const rotation of rotations) {
        const direction = rotation[0];
        const magnitude = Number(rotation.slice(1));

        if (direction === "L") {
            curr = normalize(curr - magnitude);
        } else {
            curr = normalize(curr + magnitude);
        }

        if (curr === 0) {
            count += 1;
        }
    }

    return count;
}

function p2(rotations: string[]): number {
    let count = 0;
    let curr = 50;

    for (const rotation of rotations) {
        const direction = rotation[0];
        const magnitude = Number(rotation.slice(1));
        let next, add;

        if (direction === "L") {
            [next, add] = normalizeAndCount(curr - magnitude);
        } else {
            [next, add] = normalizeAndCount(curr + magnitude);
        }

        count += add!;
        curr = next!;
    }

    return count;
}

const getRotations = (fileName: string) =>
    fs.readFileSync(fileName, "utf-8").trim().split("\n");

const exampleRotations = getRotations("d1-example.txt");
assert.equal(p1(exampleRotations), 3);
assert.equal(p2(exampleRotations), 6);

const p1Rotations = getRotations("d1-input.txt");
console.log(p1(p1Rotations));
console.log(p2(p1Rotations));
