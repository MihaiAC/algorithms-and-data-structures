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
    const nodeToCopy = new Map<_Node, _Node>();

    nodeToCopy.set(head, copyHead);

    let curr = head.next;
    let currCopy = copyHead;

    while (curr !== null) {
        currCopy.next = new _Node(curr.val);

        nodeToCopy.set(curr, currCopy.next);

        currCopy = currCopy.next;
        curr = curr.next;
    }

    // Set random links in the copy.
    currCopy = copyHead;
    curr = head;
    while (currCopy !== null) {
        if (curr!.random) currCopy.random = nodeToCopy.get(curr!.random)!;
        curr = curr!.next;
        currCopy = currCopy.next!;
    }

    return copyHead;
}
