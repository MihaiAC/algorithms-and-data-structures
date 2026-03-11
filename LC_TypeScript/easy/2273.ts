function areCountersEqual(c1: Map<string, number>, c2: Map<string, number>): boolean {
    if (c1.size !== c2.size) {
        return false;
    }

    for (let [k1, v1] of c1) {
        if (!c2.has(k1)) {
            return false;
        }

        const v2 = c2.get(k1);
        if (v1 !== v2) {
            return false;
        }
    }

    return true;
}

function createCounter(word: string): Map<string, number> {
    const counter = new Map();
    for (let char of word) {
        if (counter.has(char)) {
            counter.set(char, counter.get(char) + 1);
        } else {
            counter.set(char, 1);
        }
    }

    return counter;
}

function removeAnagrams(words: string[]): string[] {
    let ans = [];
    let prev_word = words[0];
    let prev_counter = createCounter(prev_word);
    let curr_word, curr_counter;

    for (let idx = 1; idx < words.length; idx++) {
        curr_word = words[idx];
        curr_counter = createCounter(curr_word);

        if (areCountersEqual(prev_counter, curr_counter)) {
            continue;
        }

        ans.push(prev_word);
        [prev_word, prev_counter] = [curr_word, curr_counter];
    }

    ans.push(prev_word);
    return ans;
}
