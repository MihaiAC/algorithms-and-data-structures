import assert from "node:assert";

function minFlips(s: string): number {
    const N = s.length;
    /* Counts the number of mismatches if we start with 0 or 1, respectively. */
    let counts = [0, 0];

    for (let idx = 0; idx < N; idx++) {
        const num = parseInt(s[idx]);

        // If idx is even, +1 to counts[0] if '1' and +1 to counts[1] if '0'
        // If idx is odd, +1 to counts[0] if '0' and +1 to counts[1] if '1'
        if (idx % 2 === 0) counts[1 - num]++;
        else counts[num]++;
    }

    let minFlips = Math.min(...counts);
    for (let idx = 0; idx < N; idx++) {
        // We move s[idx] to the back.
        const num = parseInt(s[idx]);

        // Counts get swapped.
        counts = [counts[1], counts[0]];

        // Idx is 0 (even), so -1 to counts[0] if '1' and -1 to counts[1] if '0'.
        counts[num]--;

        // Same as above..
        if ((N - 1) % 2 === 0) counts[1 - num]++;
        else counts[num]++;

        minFlips = Math.min(minFlips, ...counts);
    }

    return minFlips;
}

assert.equal(minFlips("111000"), 2);
assert.equal(minFlips("010"), 0);
assert.equal(minFlips("1110"), 1);
assert.equal(minFlips("10001100101000000"), 5);
