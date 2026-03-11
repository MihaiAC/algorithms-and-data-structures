import assert from "node:assert";

function countStudents(students: number[], sandwiches: number[]): number {
    const studentCounts = {
        0: 0,
        1: 0,
    };
    students.map((x) => (studentCounts[x as 0 | 1] += 1));

    for (const sandwich of sandwiches) {
        if (sandwich !== 0 && sandwich !== 1) {
            throw Error("Incorrect input, m8");
        }

        if (studentCounts[sandwich] === 0) {
            break;
        } else {
            studentCounts[sandwich] -= 1;
        }
    }

    return studentCounts[0] + studentCounts[1];
}

const students1 = [1, 1, 0, 0];
const sandwiches1 = [0, 1, 0, 1];
assert.equal(countStudents(students1, sandwiches1), 0);

const students2 = [1, 1, 1, 0, 0, 1];
const sandwiches2 = [1, 0, 0, 0, 1, 1];
assert.equal(countStudents(students2, sandwiches2), 3);
