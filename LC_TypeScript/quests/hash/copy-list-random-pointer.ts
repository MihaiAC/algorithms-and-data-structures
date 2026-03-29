class _Node {
    val: number;
    next: _Node | null;
    random: _Node | null;

    constructor(val?: number, next?: _Node, random?: _Node) {
        this.val = val === undefined ? 0 : val;
        this.next = next === undefined ? null : next;
        this.random = random === undefined ? null : random;
    }
}

function copyRandomList(head: _Node | null): _Node | null {
    if (head === null) return null;

    const copyHead = new _Node(head.val);

    const nodeToIdx = new Map<_Node, number>();
    const idxToCopyNode = new Map<number, _Node>();

    let currIdx = 0;
    nodeToIdx.set(head, currIdx);
    idxToCopyNode.set(currIdx, copyHead);
    currIdx++;

    let curr = head.next;
    let currCopy = copyHead;

    while (curr !== null) {
        currCopy.next = new _Node(curr.val);

        nodeToIdx.set(curr, currIdx);
        idxToCopyNode.set(currIdx, currCopy.next);

        currCopy = currCopy.next;
        curr = curr.next;
        currIdx++;
    }

    // Set random links in the copy.
    currCopy = copyHead;
    curr = head;
    while (currCopy !== null) {
        if (curr!.random) {
            const randomIdx = nodeToIdx.get(curr!.random)!;
            currCopy.random = idxToCopyNode.get(randomIdx)!;
        }

        curr = curr!.next;
        currCopy = currCopy.next!;
    }

    return copyHead;
}
