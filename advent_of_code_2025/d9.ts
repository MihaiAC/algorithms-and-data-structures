import * as fs from "fs";

type Point = { x: number; y: number };

/**
 * Quick and dirty, want to see p2 (sensing something nasty ~~~)
 * @param points
 * @returns
 */
function p1(points: Point[]): number {
    const N = points.length;

    const getArea = (p1: Point, p2: Point): number => {
        return Math.abs(p1.x - p2.x + 1) * Math.abs(p1.y - p2.y + 1);
    };

    let ans = 0;
    for (let idx1 = 0; idx1 < N - 1; idx1++) {
        const p1 = points[idx1]!;
        for (let idx2 = idx1 + 1; idx2 < N; idx2++) {
            const p2 = points[idx2]!;
            ans = Math.max(ans, getArea(p1, p2));
        }
    }

    return ans;
}

const readInput = (fileName: string): Point[] => {
    return fs
        .readFileSync(fileName, "utf8")
        .split(/\r+\n/)
        .map((line: string) => {
            const [x, y] = line.split(",").map(Number);
            return { x, y };
        });
};

/**
 * Surprise! It was pretty nasty.
 * @param coords
 */
function p2(points: Point[]): number {
    // Coordinate compresison
    const coordVals: number[] = [];
    for (const { x, y } of points) {
        coordVals.push(x, y);
    }

    const uniqueVals = Array.from(new Set(coordVals)).sort((a, b) => a - b);
    const index = new Map<number, number>();
    uniqueVals.forEach((val, idx) => index.set(val, idx));

    // Replace coordinates with compressed ones
    points = points.map(({ x, y }) => {
        return { x: index.get(x)!, y: index.get(y)! };
    });
    const xCoords = points.map((point) => point.x);
    const yCoords = points.map((point) => point.y);

    // Create grid
    const M = Math.max(...xCoords) + 1;
    const N = Math.max(...yCoords) + 1;
    const grid: number[][] = Array.from({ length: M }, () => Array(N).fill(0));

    // Mark red points (which can be corners)
    for (let idx = 0; idx < points.length; idx++) {
        grid[points[idx].x][points[idx].y] = 1;
    }

    // Draw the polygon edges
    const addLine = (p1: Point, p2: Point) => {
        if (p1.x === p2.x) {
            for (let k = Math.min(p1.y, p2.y); k <= Math.max(p1.y, p2.y); k++) {
                grid[p1.x][k] = 1;
            }
        }

        if (p1.y === p2.y) {
            for (let k = Math.min(p1.x, p2.x); k <= Math.max(p1.x, p2.x); k++) {
                grid[k][p1.y] = 1;
            }
        }
    };

    for (let idx = 0; idx < points.length - 1; idx++) {
        addLine(points[idx], points[idx + 1]);
    }
    addLine(points[points.length - 1], points[0]);

    // Fill polygon interior
    for (let y = 0; y < N; y++) {
        const xs: number[] = [];

        for (let x = 0; x < M; x++) {
            if (grid[x][y] !== 0) xs.push(x);
        }

        if (xs.length >= 2) {
            const xLo = Math.min(...xs);
            const xHi = Math.max(...xs);
            for (let x = xLo; x <= xHi; x++) {
                if (grid[x][y] === 0) {
                    grid[x][y] = 1;
                }
            }
        }
    }

    // Function to validate rectangle and return area
    const calcArea = (sw: Point, ne: Point): number => {
        let ok = true;
        for (let x = sw.x; x <= ne.x && ok; x++) {
            for (let y = sw.y; y <= ne.y; y++) {
                if (grid[x][y] === 0) {
                    ok = false;
                    break;
                }
            }
        }

        if (!ok) return 0;
        return (
            (uniqueVals[ne.x] - uniqueVals[sw.x] + 1) *
            (uniqueVals[ne.y] - uniqueVals[sw.y] + 1)
        );
    };

    // Calculate max area
    let maxArea = 0;
    for (let idx1 = 0; idx1 < points.length - 1; idx1++) {
        const p1 = points[idx1];
        for (let idx2 = idx1 + 1; idx2 < points.length; idx2++) {
            const p2 = points[idx2];
            const xSW = Math.min(p1.x, p2.x);
            const xNE = Math.max(p1.x, p2.x);
            const ySW = Math.min(p1.y, p2.y);
            const yNE = Math.max(p1.y, p2.y);

            if (xSW === xNE || ySW === yNE) continue;

            maxArea = Math.max(maxArea, calcArea({ x: xSW, y: ySW }, { x: xNE, y: yNE }));
        }
    }

    // Victory?
    return maxArea;
}

const example = readInput("d9-example.txt");
const input = readInput("d9-input.txt");

console.log(p1(example));
console.log(p1(input));

console.log(p2(example));
console.log(p2(input));
