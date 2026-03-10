from typing import List
import heapq


# Doubly-linked list because we need to merge things.
class Node:
    def __init__(self, value, original_idx):
        self.value = value
        self.original_idx = original_idx
        self.prev = None
        self.next = None

    # Needed for comparisons used in the heap.
    def __lt__(self, other):
        return self.original_idx < other.original_idx


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        pq = []
        head = Node(nums[0], 0)
        current = head
        merged = [False] * len(nums)
        decrease_count = 0
        ans = 0

        # Populate DLL, heap, and init decrease_count.
        for ii in range(1, len(nums)):
            new_node = Node(nums[ii], ii)
            current.next = new_node
            new_node.prev = current
            cost = current.value + new_node.value
            heapq.heappush(pq, (cost, current.original_idx, current, new_node))

            if nums[ii - 1] > nums[ii]:
                decrease_count += 1

            current = new_node

        # While there are still things in the incorrect order...
        while decrease_count > 0:
            cost, _, first, second = heapq.heappop(pq)

            # Skip stale stuff.
            if (
                merged[first.original_idx]
                or merged[second.original_idx]
                or first.value + second.value != cost
            ):
                continue

            ans += 1

            # We're removing a wrong from the world
            if first.value > second.value:
                decrease_count -= 1

            # Classic merging nodes in DLL
            prev_node = first.prev
            next_node = second.next
            first.next = next_node
            if next_node:
                next_node.prev = first

            # Update number of wrongs + push new pairs to heap.
            if prev_node:
                if prev_node.value > first.value and prev_node.value <= cost:
                    decrease_count -= 1
                # nums can contain negative values
                elif prev_node.value <= first.value and prev_node.value > cost:
                    decrease_count += 1

                heapq.heappush(
                    pq,
                    (prev_node.value + cost, prev_node.original_idx, prev_node, first),
                )

            # Same as above
            if next_node:
                if second.value > next_node.value and cost <= next_node.value:
                    decrease_count -= 1
                elif second.value <= next_node.value and cost > next_node.value:
                    decrease_count += 1
                heapq.heappush(
                    pq, (cost + next_node.value, first.original_idx, first, next_node)
                )

            first.value = cost
            merged[second.original_idx] = True

        return ans
