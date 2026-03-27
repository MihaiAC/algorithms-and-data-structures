import assert from "node:assert";

function areSimilar(mat: number[][], k: number): boolean {
    const [M, N] = [mat.length, mat[0].length];

    for (let ii = 0; ii < M; ii++) {
        for (let jj = 0; jj < N; jj++) {
            if (mat[ii][jj] !== mat[ii][(jj + k) % N]) return false;
        }
    }

    return true;
}

assert(
    !areSimilar(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ],
        4
    )
);

assert(
    areSimilar(
        [
            [1, 2, 1, 2],
            [5, 5, 5, 5],
            [6, 3, 6, 3],
        ],
        2
    )
);

assert(
    areSimilar(
        [
            [2, 2],
            [2, 2],
        ],
        3
    )
);
