import _ from "lodash";
import assert from "node:assert";

function rotate(mat: number[][]): number[][] {
    const N = mat.length;
    const rMat: number[][] = new Array(N).fill([]).map((_) => new Array(N).fill(0));

    for (let ii = 0; ii < N; ii++) {
        for (let jj = 0; jj < N; jj++) {
            rMat[N - jj - 1][ii] = mat[ii][jj];
        }
    }

    return rMat;
}

function findRotation(mat: number[][], target: number[][]): boolean {
    let rMat;
    for (let nRot = 0; nRot < 4; nRot++) {
        rMat = rotate(mat);
        if (_.isEqual(rMat, target)) return true;
        mat = rMat;
    }

    return false;
}

assert.equal(
    findRotation(
        [
            [0, 1],
            [1, 0],
        ],
        [
            [1, 0],
            [0, 1],
        ]
    ),
    true
);

assert.equal(
    findRotation(
        [
            [0, 1],
            [1, 1],
        ],
        [
            [1, 0],
            [0, 1],
        ]
    ),
    false
);

assert.equal(
    findRotation(
        [
            [0, 0, 0],
            [0, 1, 0],
            [1, 1, 1],
        ],
        [
            [1, 1, 1],
            [0, 1, 0],
            [0, 0, 0],
        ]
    ),
    true
);
