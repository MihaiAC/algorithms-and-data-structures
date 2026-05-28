import assert from "node:assert";

class TrieNode {
    public next = new Map<string, TrieNode>();
    public wordLength: number = Infinity;
    public wordIdx: number = Infinity;

    public updatePointers(wordLength: number, wordIdx: number) {
        if (wordLength < this.wordLength) {
            this.wordLength = wordLength;
            this.wordIdx = wordIdx;
        } else if (wordLength === this.wordLength && wordIdx < this.wordIdx) {
            this.wordIdx = wordIdx;
        }
    }
}

class Trie {
    public root = new TrieNode();

    public addWord(word: string, wordIdx: number) {
        this.root.updatePointers(word.length, wordIdx);
        let currNode: TrieNode = this.root;

        for (let letterIdx = word.length - 1; letterIdx >= 0; letterIdx--) {
            const letter = word[letterIdx];

            if (!currNode.next.has(letter)) {
                currNode.next.set(letter, new TrieNode());
            }

            currNode = currNode.next.get(letter)!;
            if (currNode.wordLength > word.length) {
                currNode.wordLength = word.length;
                currNode.wordIdx = wordIdx;
            } else if (
                currNode.wordLength === word.length &&
                currNode.wordIdx > wordIdx
            ) {
                currNode.wordIdx = wordIdx;
            }
        }
    }

    public parseWord(word: string): number {
        let currNode: TrieNode = this.root;

        for (let letterIdx = word.length - 1; letterIdx >= 0; letterIdx--) {
            const letter = word[letterIdx];
            if (!currNode.next.has(letter)) break;
            currNode = currNode.next.get(letter)!;
        }

        return currNode.wordIdx;
    }
}

function stringIndices(wordsContainer: string[], wordsQuery: string[]): number[] {
    const trie = new Trie();

    for (let wordIdx = 0; wordIdx < wordsContainer.length; wordIdx++) {
        trie.addWord(wordsContainer[wordIdx], wordIdx);
    }

    return wordsQuery.map((word) => trie.parseWord(word));
}

assert.deepEqual(stringIndices(["abcd", "bcd", "xbcd"], ["cd", "bcd", "xyz"]), [1, 1, 1]);
assert.deepEqual(
    stringIndices(["abcdefgh", "poiuygh", "ghghgh"], ["gh", "acbfgh", "acbfegh"]),
    [2, 0, 2]
);
