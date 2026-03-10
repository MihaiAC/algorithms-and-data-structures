import assert from "node:assert";

function addBinary(a: string, b: string): string {
    const revAns = [];

    const revA = Array.from(a).reverse();
    const revB = Array.from(b).reverse();

    let carry = 0;
    for (let idx = 0; idx < Math.max(revA.length, revB.length); idx++) {
        const digA = revA.at(idx) ?? "0";
        const digB = revB.at(idx) ?? "0";

        const sum = parseInt(digA) + parseInt(digB) + carry;
        switch (sum) {
            case 0: {
                revAns.push("0");
                break;
            }
            case 1: {
                carry = 0;
                revAns.push("1");
                break;
            }
            case 2: {
                carry = 1;
                revAns.push("0");
                break;
            }
            case 3: {
                revAns.push("1");
                break;
            }
        }
    }

    if (carry === 1) revAns.push("1");
    return revAns.reverse().join("");
}

assert.equal(addBinary("11", "1"), "100");
assert.equal(addBinary("1010", "1011"), "10101");

const a =
    "10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101";
const b =
    "110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011";
const ans =
    "110111101100010011000101110110100000011101000101011001000011011000001100011110011010010011000000000";
assert.equal(addBinary(a, b), ans);
