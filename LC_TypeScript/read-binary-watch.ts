const HOURS = [1, 2, 4, 8];
const MINUTES = [1, 2, 4, 8, 16, 32];

function generateCombs(
    maxVal: number,
    arr: number[],
    pad: boolean
): Map<number, string[]> {
    const combs = new Map<number, string[]>();
    const maxMask = 1 << arr.length;

    for (let mask = 0; mask < maxMask; mask++) {
        let sum = 0;
        let bitCount = 0;

        for (let bitIndex = 0; bitIndex < arr.length; bitIndex++) {
            if (mask & (1 << bitIndex)) {
                sum += arr[bitIndex];
                bitCount += 1;
            }

            if (sum > maxVal) break;
        }

        if (sum <= maxVal) {
            const formattedSum = pad ? sum.toString().padStart(2, "0") : sum.toString();

            if (!combs.has(bitCount)) combs.set(bitCount, []);
            combs.get(bitCount)!.push(formattedSum);
        }
    }

    return combs;
}

const HOURS_COMBS = generateCombs(11, HOURS, false);
const MINUTES_COMBS = generateCombs(59, MINUTES, true);

function readBinaryWatch(turnedOn: number): string[] {
    const ans = [];
    for (let minsTurnedOn = 0; minsTurnedOn <= turnedOn; minsTurnedOn++) {
        const mins = MINUTES_COMBS.get(minsTurnedOn);
        if (!mins) continue;

        const hours = HOURS_COMBS.get(turnedOn - minsTurnedOn);
        if (!hours) continue;

        for (const hr of hours) {
            for (const min of mins) {
                ans.push(hr + ":" + min);
            }
        }
    }

    return ans;
}

console.log(readBinaryWatch(1));
