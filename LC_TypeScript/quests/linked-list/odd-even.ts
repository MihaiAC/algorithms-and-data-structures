import assert from "node:assert";
import { ListNode } from "../../ListNode";

function oddEvenList(head: ListNode | null): ListNode | null {
    if (head === null) return null;
    if (head.next === null) return head;

    let even = head;
    const oddHead = head.next;
    let odd = head.next;
    let curr = odd.next;
    let idx = 0;
    while (curr !== null) {
        if (idx === 0) {
            even.next = curr;
            even = curr;
        } else {
            odd.next = curr;
            odd = curr;
        }

        curr = curr.next;
        idx = 1 - idx;
    }

    even.next = oddHead;
    odd.next = null;
    return head;
}

const i1 = ListNode.fromArray([1, 2, 3, 4, 5]);
const o1 = ListNode.fromArray([1, 3, 5, 2, 4]);
assert(o1?.equals(oddEvenList(i1)));

const i2 = ListNode.fromArray([2, 1, 3, 5, 6, 4, 7]);
const o2 = ListNode.fromArray([2, 3, 6, 7, 1, 5, 4]);
assert(o2?.equals(oddEvenList(i2)));

const i3 = ListNode.fromArray([1]);
const o3 = ListNode.fromArray([1]);
assert(o3?.equals(oddEvenList(i3)));
