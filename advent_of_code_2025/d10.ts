import * as fs from "fs";
import assert from "node:assert";
import Worker from "web-worker";
// Polyfill Worker for Node.js
global.Worker = Worker as any;
import GLPK from "glpk.js";

type Machine = {
    target: string;
    buttons: number[][];
    joltReqs: number[];
};

function readInput(fileName: string): Machine[] {
    const lines = fs.readFileSync(fileName, "utf8").split(/\r+\n/);
    const machines: Machine[] = [];

    for (const line of lines) {
        const chunks = line.split(" ");
        assert(chunks.length >= 3, `Expected more than 3 chunks on line: ${line}`);

        const target = chunks[0]!
            .replaceAll(/[\[\]]/g, "")
            .replaceAll(".", "0")
            .replaceAll("#", "1");

        const joltReqs = chunks
            .at(-1)!
            .replaceAll(/[\{\}]/g, "")
            .split(",")
            .map(Number);

        const buttons = [];
        for (const chunk of chunks.slice(1, -1)) {
            buttons.push(
                chunk
                    .replaceAll(/[\(\)]/g, "")
                    .split(",")
                    .map(Number)
            );
        }

        machines.push({
            target,
            buttons,
            joltReqs,
        });
    }

    return machines;
}

function pressButton(state: string, button: number[]): string {
    const chars = state.split("");
    for (const pos of button) {
        chars[pos] = chars[pos] === "0" ? "1" : "0";
    }

    return chars.join("");
}

function minOps(machine: Machine): number {
    const dist = new Map<string, number>();
    const N = machine.target.length;

    let currStates = new Set<string>();
    currStates.add("0".repeat(N));
    dist.set("0".repeat(N), 0);

    let currDist = 0;

    while (true) {
        const newStates = new Set<string>();
        currDist += 1;

        for (const currState of currStates) {
            for (const button of machine.buttons) {
                const newState = pressButton(currState, button);
                if (!dist.has(newState)) {
                    if (newState === machine.target) return currDist;
                    dist.set(newState, currDist);
                    newStates.add(newState);
                }
            }
        }

        currStates = newStates;
    }
}

function p1(machines: Machine[]): number {
    return machines.reduce((accum: number, curr: Machine) => accum + minOps(curr), 0);
}

async function minButtonPresses(machine: Machine): Promise<number> {
    const glpk = await GLPK();
    const N = machine.buttons.length;

    const problem = {
        name: "ButtonPresses",
        objective: {
            direction: glpk.GLP_MIN,
            name: "presses",
            vars: machine.buttons.map((_, idx) => ({
                name: `x${idx}`,
                coef: 1.0,
            })),
        },
        subjectTo: machine.joltReqs.map((req, counterIdx) => ({
            name: `counter${counterIdx}`,
            vars: machine.buttons
                .map((button, btnIdx) =>
                    button.includes(counterIdx) ? { name: `x${btnIdx}`, coef: 1.0 } : null
                )
                .filter((v) => v !== null),
            bnds: { type: glpk.GLP_FX, ub: req, lb: req },
        })),
        bounds: machine.buttons.map((_, idx) => ({
            name: `x${idx}`,
            type: glpk.GLP_LO,
            lb: 0.0,
            ub: 500.0,
        })),
    };

    const result = glpk.solve(problem);
    return Math.round((await result).result.z);
}

async function p2(machines: Machine[]): Promise<number> {
    let total = 0;
    for (const machine of machines) {
        total += await minButtonPresses(machine);
    }

    return total;
}

const exampleMachines = readInput("d10-example.txt");
const inputMachines = readInput("d10-input.txt");
console.log(p1(exampleMachines));
console.log(p1(inputMachines));

console.log(await p2(exampleMachines));
