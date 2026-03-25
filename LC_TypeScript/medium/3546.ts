import _ from "lodash";
import assert from "node:assert";

function canPartitionGrid(grid: number[][]): boolean {
    const rowSums = grid.map((row: number[]) => _.sum(row));
    const colSums = _.map(_.unzip(grid), (col) => _.sum(col));

    function canPartitionArr(arr: number[]) {
        let total = _.sum(arr);
        let curr = 0;
        for (const num of arr) {
            curr += num;
            total -= num;
            if (curr === total) return true;
        }

        return false;
    }

    return canPartitionArr(rowSums) || canPartitionArr(colSums);
}

assert.equal(
    canPartitionGrid([
        [1, 4],
        [2, 3],
    ]),
    true
);

assert.equal(
    canPartitionGrid([
        [1, 3],
        [2, 4],
    ]),
    false
);
