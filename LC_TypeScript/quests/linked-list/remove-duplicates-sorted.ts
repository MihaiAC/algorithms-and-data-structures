import assert from "node:assert";
import { ListNode } from "../../ListNode";

function deleteDuplicates(head: ListNode | null): ListNode | null {
    if (!head) return null;

    let curr: ListNode | null = head;
    while (curr) {
        while (curr.next && curr.next.val === curr.val) {
            curr.next = curr.next.next;
        }

        curr = curr.next;
    }

    return head;
}

const i1 = ListNode.fromArray([1, 1, 2]);
const o1 = ListNode.fromArray([1, 2]);
assert.equal(o1?.equals(deleteDuplicates(i1)), true);

const i2 = ListNode.fromArray([1, 1, 2, 3, 3]);
const o2 = ListNode.fromArray([1, 2, 3]);
assert.equal(o2?.equals(deleteDuplicates(i2)), true);
