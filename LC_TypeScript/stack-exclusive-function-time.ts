import assert from "node:assert";

type Log = {
    id: number;
    type: "start" | "end";
    timestamp: number;
};

/**
 * Extracts the id, type of operation and timestamp
 * from a log.
 * @param log
 */
function parseLog(log: string): Log {
    const parsedLog = log.split(":");
    if (parsedLog.length !== 3) {
        throw Error(`Invalid log: ${log}`);
    }

    const id = Number(parsedLog[0]);
    const timestamp = Number(parsedLog[2]);

    const type = parsedLog[1];
    if (type !== "start" && type !== "end") {
        throw Error(`Expected start|end, got ${type} instead.`);
    }

    return { id, timestamp, type };
}

function exclusiveTime(n: number, logs: string[]): number[] {
    const ans = Array(n).fill(0);
    const stack: number[] = [];
    let prevTime = 0;

    for (const log of logs) {
        const { id, timestamp, type } = parseLog(log);
        if (type === "start") {
            if (stack.length > 0) {
                ans[stack[stack.length - 1]] += timestamp - prevTime;
            }

            stack.push(id);
            prevTime = timestamp;
        } else {
            ans[stack.pop()!] += timestamp - prevTime + 1;
            prevTime = timestamp + 1;
        }
    }

    return ans;
}

const logs1 = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"];
const n1 = 2;
assert.deepEqual(exclusiveTime(n1, logs1), [3, 4]);

const logs2 = ["0:start:0", "0:start:2", "0:end:5", "0:start:6", "0:end:6", "0:end:7"];
const n2 = 1;
assert.deepEqual(exclusiveTime(n2, logs2), [8]);

const logs3 = ["0:start:0", "0:start:2", "0:end:5", "1:start:6", "1:end:6", "0:end:7"];
const n3 = 2;
assert.deepEqual(exclusiveTime(n3, logs3), [7, 1]);
