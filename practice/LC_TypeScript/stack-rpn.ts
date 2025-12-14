import assert from "node:assert";

const OPS = new Set(["*", "+", "-", "/"]);
const OPS_TO_FN = {
    "*": (x: number, y: number) => x * y,
    "+": (x: number, y: number) => x + y,
    "-": (x: number, y: number) => x - y,
    "/": (x: number, y: number) => Math.trunc(x / y),
};

function evalRPN(tokens: string[]): number {
    let ans = 0;
    let stack: number[] = [];

    for (const token of tokens) {
        if (OPS.has(token)) {
            const b = stack.pop();
            const a = stack.pop();
            if (a !== undefined && b !== undefined) {
                stack.push(OPS_TO_FN[token as keyof typeof OPS_TO_FN](a, b));
            }
        } else {
            stack.push(Number(token));
        }
    }

    return stack[0];
}

const tokens1 = ["2", "1", "+", "3", "*"];
assert.equal(evalRPN(tokens1), 9);

const tokens2 = ["4", "13", "5", "/", "+"];
assert.equal(evalRPN(tokens2), 6);

const tokens3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"];
assert.equal(evalRPN(tokens3), 22);
