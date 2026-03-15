import assert from "node:assert";

const MODN = 10 ** 9 + 7;

class Fancy {
    private vals: number[];
    // mods[0] = max vals index when operation was applied
    // , where operation := mods[1] * x + mods[2]
    private mods: number[][];

    constructor() {
        this.vals = [];
        this.mods = [];
    }

    append(val: number): void {
        this.vals.push(val);
    }

    addAll(inc: number): void {
        if (this.vals.length === 0) return;

        const lastMod = this.mods.length > 0 ? this.mods.at(-1) : undefined;
        if (lastMod && lastMod[0] === this.vals.length - 1) {
            lastMod[2] = (lastMod[2] + inc) % MODN;
        } else {
            this.mods.push([this.vals.length - 1, 1, inc]);
        }
    }

    multAll(m: number): void {
        if (this.vals.length === 0) return;

        const lastMod = this.mods.length > 0 ? this.mods.at(-1) : undefined;
        if (lastMod && lastMod[0] === this.vals.length - 1) {
            lastMod[1] = (lastMod[1] * m) % MODN;
            lastMod[2] = (lastMod[2] * m) % MODN;
        } else {
            this.mods.push([this.vals.length - 1, m, 0]);
        }
    }

    searchModsIndex(valsIdx: number): number {
        if (valsIdx > this.mods.at(-1)![0]) return this.mods.length;
        if (valsIdx < this.mods[0][0]) return 0;

        // Need to find mid so: mods[mid] <= idx < mods[mid+1]
        let [lo, hi] = [0, this.mods.length - 1];
        while (lo < hi) {
            const mid = Math.floor((lo + hi) / 2);

            if (valsIdx < this.mods[mid][0]) {
                hi = mid - 1;
                continue;
            }

            if (mid + 1 === this.mods.length) return mid;
            if (valsIdx < this.mods[mid + 1][0]) return mid;
            lo = mid + 1;
        }

        return lo;
    }

    accumFrom(modsIdx: number): number[] {
        let [mult, add] = [1, 0];
        for (const [_, xMult, xAdd] of this.mods.slice(modsIdx)) {
            mult = (mult * xMult) % MODN;
            add = (((add * xMult) % MODN) + xAdd) % MODN;
        }

        return [mult, add];
    }

    getIndex(idx: number): number {
        if (idx >= this.vals.length) return -1;
        if (this.mods.length === 0) return this.vals[idx];

        // Binary search on the first index of this.mods.
        let modsIdx = this.searchModsIndex(idx);

        if (modsIdx === this.mods.length) return this.vals[idx];
        if (this.mods[modsIdx]![0] < idx) {
            modsIdx += 1;
        }

        const [mult, add] = this.accumFrom(modsIdx);
        return (((mult * this.vals[idx]) % MODN) + add) % MODN;
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
