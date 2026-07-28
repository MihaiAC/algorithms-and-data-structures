import assert from "node:assert";
import { Deque } from "@datastructures-js/deque";

const CODE_A = "a".charCodeAt(0);

function smallestPalindrome(s: string): string {
    const N = s.length;
    const halfLength = Math.floor(N / 2);

    const counts = new Array<number>(26).fill(0);
    for (let idx = 0; idx < halfLength; idx++) {
        counts[s.charCodeAt(idx) - CODE_A]++;
    }

    const deque = new Deque<string>();
    if (N % 2 === 1) {
        deque.pushBack(s[halfLength]);
    }

    for (let letterIdx = 25; letterIdx >= 0; letterIdx--) {
        const letter = String.fromCharCode(CODE_A + letterIdx);
        for (let rep = 0; rep < counts[letterIdx]; rep++) {
            deque.pushFront(letter);
            deque.pushBack(letter);
        }
    }

    return deque.toArray().join("");
}

assert.equal(smallestPalindrome("z"), "z");
assert.equal(smallestPalindrome("babab"), "abbba");
assert.equal(smallestPalindrome("daccad"), "acddca");
console.log("ok");
