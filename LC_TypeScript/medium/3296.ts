import assert from "node:assert";

function calculateWorkDone(time: number, workerSpeed: number): number {
    const timeOverSpeed = Math.floor(time / workerSpeed);
    return Math.floor((Math.sqrt(8 * timeOverSpeed + 1) - 1) / 2);
}

function minNumberOfSeconds(target: number, workerSpeeds: number[]): number {
    const maxSpeed = Math.max(...workerSpeeds);
    let minTime = 1;
    // Time it takes for the slowest worker to finish by himself
    let maxTime = Math.floor((target * (target + 1)) / 2) * maxSpeed;

    const totalWorkDone = (time: number) =>
        workerSpeeds.reduce(
            (accum: number, workerSpeed: number) =>
                accum + calculateWorkDone(time, workerSpeed),
            0
        );

    while (minTime < maxTime) {
        // Calculate how much work has been done in this time.
        const time = Math.floor((minTime + maxTime) / 2);
        const workDone = totalWorkDone(time);

        if (workDone < target) minTime = time + 1;
        else maxTime = time - 1;
    }

    return totalWorkDone(minTime) < target ? minTime + 1 : minTime;
}

assert.equal(minNumberOfSeconds(4, [2, 1, 1]), 3);
assert.equal(minNumberOfSeconds(10, [3, 2, 2, 4]), 12);
assert.equal(minNumberOfSeconds(5, [1]), 15);
assert.equal(minNumberOfSeconds(100000, [1000000]), 5000050000000000);
