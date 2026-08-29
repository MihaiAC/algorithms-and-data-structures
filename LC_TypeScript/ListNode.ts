// oxlint-disable typescript/no-this-alias
export class ListNode {
    val: number;
    next: ListNode | null;

    constructor(val?: number, next?: ListNode | null) {
        this.val = val === undefined ? 0 : val;
        this.next = next === undefined ? null : next;
    }

    /**
     * Builds a ListNode from an array of numbers.
     */
    public static fromArray(arr: number[]): ListNode | null {
        if (arr.length === 0) return null;

        const head = new ListNode(arr[0]);
        let curr = head;
        for (const num of arr.slice(1)) {
            let newNode = new ListNode(num);
            curr.next = newNode;
            curr = newNode;
        }

        return head;
    }

    /**
     * Check linked list equality.
     */
    public equals(node: ListNode | null): boolean {
        if (node === null) return false;
        let head: ListNode | null = this;

        while (head && node && head.val === node.val) {
            head = head.next;
            node = node.next;
        }

        return head === null && node === null;
    }

    public toString(): string {
        const arr = [];
        let curr: ListNode | null = this;
        while (curr !== null) {
            arr.push(curr.val);
            curr = curr.next;
        }

        return arr.toString();
    }
}
