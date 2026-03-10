import * as fs from "fs";
import _ from "lodash";

function getManifold(fileName: string): string[] {
    return fs.readFileSync(fileName, "utf8").split(/\r?\n/);
}

function p1(rows: string[]): number {
    let beams = new Set<number>();
    let ncols = rows[0]!.length;
    let nsplits = 0;

    // Locate first beam.
    for (let col = 0; col < ncols; col++) {
        if (rows[0][col] === "S") {
            beams.add(col);
            break;
        }
    }

    // Go through every row!
    for (const row of rows.slice(1)) {
        const newBeams = new Set<number>();
        for (const col of beams) {
            if (row[col] === ".") {
                newBeams.add(col);
            } else {
                nsplits += 1;

                if (col > 0 && row[col - 1] === ".") {
                    newBeams.add(col - 1);
                }

                if (col < ncols - 1 && row[col + 1] === ".") {
                    newBeams.add(col + 1);
                }
            }
        }

        beams = newBeams;
    }

    return nsplits;
}

function p2(rows: string[]): number {
    let nworlds = 0;
    let ncols = rows[0]!.length;
    let nrows = rows.length;
    let startCol = 0;

    // Locate first beam.
    for (let col = 0; col < ncols; col++) {
        if (rows[0][col] === "S") {
            startCol = col;
            break;
        }
    }

    // Count the worlds!
    const count = _.memoize(
        (row: number, col: number): number => {
            if (row === nrows) {
                return 1;
            }

            if (rows[row][col] === ".") {
                return count(row + 1, col);
            } else {
                let [leftCount, rightCount] = [0, 0];
                if (col > 0) {
                    leftCount = count(row + 1, col - 1);
                }

                if (col < ncols - 1) {
                    rightCount = count(row + 1, col + 1);
                }

                return leftCount + rightCount;
            }
        },
        (row, col) => `${row},${col}`
    );

    return count(1, startCol);
}

const exampleManifold = getManifold("d7-example.txt");
const inputManifold = getManifold("d7-input.txt");

console.log("P1:");
console.log(p1(exampleManifold));
console.log(p1(inputManifold));

console.log("\nP2:");
console.log(p2(exampleManifold));
console.log(p2(inputManifold));
