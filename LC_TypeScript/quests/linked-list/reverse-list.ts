import assert from "node:assert";
import { ListNode } from "../../ListNode";

function reverseList(head: ListNode | null): ListNode | null {
    if (head === null) return null;
    if (head.next === null) return head;

    let prevNode = null;
    let currNode = head;
    let nextNode: ListNode | null = head.next;
    while (nextNode !== null) {
        currNode.next = prevNode;
        prevNode = currNode;
        currNode = nextNode;
        nextNode = currNode.next;
    }

    currNode.next = prevNode;
    return currNode;
}

const i1 = ListNode.fromArray([1, 2, 3, 4, 5]);
const o1 = ListNode.fromArray([5, 4, 3, 2, 1]);
assert(o1?.equals(reverseList(i1)));

const i2 = ListNode.fromArray([1, 2]);
const o2 = ListNode.fromArray([2, 1]);
assert(o2?.equals(reverseList(i2)));
