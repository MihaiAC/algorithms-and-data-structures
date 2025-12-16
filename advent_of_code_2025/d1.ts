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

const getRotations = (fileName: string) =>
    fs.readFileSync(fileName, "utf-8").trim().split("\n");

const exampleRotations = getRotations("d1-p1-example.txt");
assert.equal(p1(exampleRotations), 3);

const p1Rotations = getRotations("d1-p1.txt");
console.log(p1(p1Rotations));
