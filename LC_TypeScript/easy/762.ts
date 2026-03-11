import assert from "node:assert";

const PRIMES = new Set([2, 3, 5, 7, 11, 13, 17, 19]);

function countPrimeSetBits(left: number, right: number): number {
    let count = 0;
    for (let num = left; num <= right; num++) {
        const nbits = Array.from(num.toString(2)).reduce(
            (accum, curr) => (accum += curr === "1" ? 1 : 0),
            0
        );
        if (PRIMES.has(nbits)) count++;
    }

    return count;
}

assert.equal(countPrimeSetBits(6, 10), 4);
assert.equal(countPrimeSetBits(10, 15), 5);
