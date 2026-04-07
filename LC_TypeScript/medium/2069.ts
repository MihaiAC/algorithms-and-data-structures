import assert from "node:assert";

type Direction = "North" | "South" | "West" | "East";

const delta: Record<Direction, number[]> = {
    North: [0, 1],
    South: [0, -1],
    West: [-1, 0],
    East: [1, 0],
};

const kaiten: Record<Direction, Direction> = {
    North: "West",
    West: "South",
    South: "East",
    East: "North",
};

class Robot {
    M: number;
    N: number;
    perimeter: number;
    cDir: Direction = "East";
    x: number = 0;
    y: number = 0;

    constructor(width: number, height: number) {
        this.M = width;
        this.N = height;
        this.perimeter = 2 * (width + height - 2);
    }

    withinBounds(x: number, y: number): boolean {
        return 0 <= x && x < this.M && 0 <= y && y < this.N;
    }

    clampX(x: number): number {
        return Math.min(this.M - 1, Math.max(0, x));
    }

    clampY(y: number): number {
        return Math.min(this.N - 1, Math.max(0, y));
    }

    onEdge(): boolean {
        return (
            this.x === 0 || this.y === 0 || this.x === this.M - 1 || this.y === this.N - 1
        );
    }

    step(steps: number): void {
        if (this.onEdge() && steps > this.perimeter) {
            steps %= this.perimeter;
            if (steps === 0) {
                if (this.x === 0 && this.y === 0) this.cDir = "South";
                else if (this.x === this.M - 1 && this.y === 0) this.cDir = "East";
                else if (this.x === this.M - 1 && this.y === this.N - 1)
                    this.cDir = "North";
                else if (this.x === 0 && this.y === this.N - 1) this.cDir = "West";
                return;
            }
        }

        const [dx, dy] = delta[this.cDir];
        let [nx, ny] = [this.x + dx * steps, this.y + dy * steps];

        if (this.withinBounds(nx, ny)) {
            [this.x, this.y] = [nx, ny];
            return;
        }

        // Clamp nx, ny to be within bounds.
        [nx, ny] = [this.clampX(nx), this.clampY(ny)];

        // Subtract the number of steps taken to reach the edge.
        steps -= Math.abs(this.x - nx) + Math.abs(this.y - ny);

        // Update robot position and direction.
        [this.x, this.y] = [nx, ny];
        this.cDir = kaiten[this.cDir];

        // Call step recursively.
        this.step(steps);
    }

    getPos(): number[] {
        return [this.x, this.y];
    }

    getDir(): string {
        return this.cDir;
    }
}

const robot = new Robot(6, 3);
robot.step(2);
robot.step(2);
assert.deepEqual(robot.getPos(), [4, 0]);
assert.deepEqual(robot.getDir(), "East");
robot.step(2);
robot.step(1);
robot.step(4);
assert.deepEqual(robot.getPos(), [1, 2]);
assert.equal(robot.getDir(), "West");
