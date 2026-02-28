import { memoize } from "lodash";
import assert from "node:assert";

const MODN = 1000000007n;

const expModMemo = memoize(
    (base: bigint, exp: bigint, mod: bigint): bigint => {
        if (exp == 0n) return 1n;
        if (exp % 2n === 0n) {
            const half = expModMemo(base, exp / 2n, mod);
            return (half * half) % mod;
        } else {
            return (base * expModMemo(base, exp - 1n, mod)) % mod;
        }
    },
    (base, exp, mod) => `${base},${exp},${mod}`
);

function concatenatedBinary(n: number): number {
    let ans = 0n;
    let bins = 0n;
    for (let num = n; num >= 1; num--) {
        const nDigits = BigInt(num.toString(2).length);
        ans = (ans + BigInt(num) * expModMemo(2n, bins, MODN)) % MODN;
        bins += nDigits;
    }

    return Number(ans);
}

assert.equal(concatenatedBinary(1), 1);
assert.equal(concatenatedBinary(3), 27);
assert.equal(concatenatedBinary(12), 505379714);
assert.equal(concatenatedBinary(42), 727837408);
