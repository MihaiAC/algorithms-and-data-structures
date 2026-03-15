import assert from "node:assert";

const MODN = 10 ** 9 + 7;
const BIG_MODN = BigInt(MODN);

function mulMod(a: number, b: number): number {
    return Number((BigInt(a) * BigInt(b)) % BIG_MODN);
}

function addMod(a: number, b: number): number {
    return Number((BigInt(a) + BigInt(b) + BIG_MODN) % BIG_MODN);
}

function powMod(base: bigint, exp: bigint): number {
    let res = 1n;

    while (exp > 0n) {
        if (exp % 2n === 1n) res = (res * base) % BIG_MODN;
        exp >>= 1n;
        base = (base * base) % BIG_MODN;
    }

    return Number(res % BIG_MODN);
}

function invMod(x: number): number {
    return powMod(BigInt(x), BIG_MODN - 2n);
}

class Fancy {
    private vals: number[];
    private mul: number;
    private add: number;

    constructor() {
        this.vals = [];
        this.mul = 1;
        this.add = 0;
    }

    append(val: number): void {
        const modifiedVal = mulMod(addMod(val, -this.add), invMod(this.mul));
        this.vals.push(modifiedVal);
    }

    addAll(inc: number): void {
        this.add = addMod(this.add, inc);
    }

    multAll(m: number): void {
        this.add = mulMod(this.add, m);
        this.mul = mulMod(this.mul, m);
    }

    getIndex(idx: number): number {
        if (idx >= this.vals.length) return -1;
        return addMod(mulMod(this.vals[idx], this.mul), this.add);
    }
}

const fancy = new Fancy(); // there's nothing fancy about this..
fancy.append(2);
fancy.addAll(3);
fancy.append(7);
fancy.multAll(2);
assert.equal(fancy.getIndex(0), 10);
fancy.addAll(3);
fancy.append(10);
fancy.multAll(2);
assert.equal(fancy.getIndex(0), 26);
assert.equal(fancy.getIndex(1), 34);
assert.equal(fancy.getIndex(2), 20);
