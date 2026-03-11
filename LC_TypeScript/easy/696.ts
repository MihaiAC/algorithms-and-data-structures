import assert from "node:assert";

function countBinarySubstrings(s: string): number {
    let ans = 0;
    let prevOcc = 0;
    let currBin = s[0];
    let currOcc = 1;

    for (let idx = 1; idx < s.length; idx++) {
        if (s[idx] === currBin) {
            currOcc += 1;
        } else {
            ans += Math.min(prevOcc, currOcc);
            prevOcc = currOcc;
            currOcc = 1;
            currBin = s[idx];
        }
    }

    ans += Math.min(prevOcc, currOcc);

    return ans;
}

assert.equal(countBinarySubstrings("00110011"), 6);
assert.equal(countBinarySubstrings("10101"), 4);
