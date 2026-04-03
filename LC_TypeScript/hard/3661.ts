import _ from "lodash";
import assert from "node:assert";

// Python's bisect_left and bisect_right are simply superior...
function maxWalls(robots: number[], distance: number[], walls: number[]): number {
    const nRobots = robots.length;
    const nWalls = walls.length;

    const sortedRD = _.sortBy(_.zip(robots, distance) as [number, number][], 0);
    walls.sort((a, b) => a - b);

    let [prevMaxRight, prevMaxLeft] = [0, 0];
    let prevLeftReach = walls[nWalls - 1] + 1;

    for (let idx = nRobots - 1; idx >= 0; idx--) {
        const currLoc = sortedRD[idx][0]!;
        const currDist = sortedRD[idx][1]!;

        // Calculate reach of the current robot.
        let leftReach = 0;
        if (idx > 0) leftReach = Math.max(sortedRD[idx - 1][0]! + 1, currLoc - currDist);
        else leftReach = currLoc - currDist;

        let rightReach = 0;
        if (idx < nRobots - 1)
            rightReach = Math.min(sortedRD[idx + 1][0]! - 1, currLoc + currDist);
        else rightReach = currLoc + currDist;

        // Calculate max score if current robot shoots to its left.
        const leftRangeMax = _.sortedLastIndex(walls, currLoc);
        const leftRangeMin = _.sortedIndex(walls, leftReach);
        const currMaxLeft =
            leftRangeMax - leftRangeMin + Math.max(prevMaxLeft, prevMaxRight);

        // Slightly more complicated if it shoots to its right.
        // If previous robot shot to its right:
        const rightRangeMin = _.sortedIndex(walls, currLoc);
        const rightRangeMax = _.sortedLastIndex(walls, rightReach);
        const rightMax1 = rightRangeMax - rightRangeMin + prevMaxRight;

        // If previous robot shot to its left:
        const rightRangeMaxSpecial = _.sortedLastIndex(
            walls,
            Math.min(rightReach, prevLeftReach - 1)
        );

        const rightMax2 = rightRangeMaxSpecial - rightRangeMin + prevMaxLeft;
        const currMaxRight = Math.max(rightMax1, rightMax2);

        [prevMaxLeft, prevMaxRight] = [currMaxLeft, currMaxRight];
        prevLeftReach = leftReach;
    }

    return Math.max(prevMaxLeft, prevMaxRight);
}

assert.equal(maxWalls([4], [3], [1, 10]), 1);
assert.equal(maxWalls([10, 2], [5, 1], [5, 2, 7]), 3);
assert.equal(maxWalls([1, 2], [100, 1], [10]), 0);
