import * as fs from "fs";

function p1(fileName: string): number {
    const input = fs.readFileSync(fileName, "utf-8").split(/\r+\n/);
    let ans = 0;

    for (const line of input) {
        if (!line.includes("x")) continue;
        const [firstHalf, secondHalf] = line.split(": ");
        const area = firstHalf
            .split("x")
            .map(Number)
            .reduce((accum, x) => accum * x, 1);

        const estimatedArea = secondHalf
            .split(" ")
            .map(Number)
            .reduce((accum, x) => accum + 8 * x, 1);

        if (estimatedArea <= area) ans += 1;
    }

    return ans;
}

console.log(p1("d12-input.txt"));
