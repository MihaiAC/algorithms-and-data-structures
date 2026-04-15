from typing import Optional


class Node:
    def __init__(
        self,
        key: int,
        val: int,
        prev: Optional[Node] = None,
        next: Optional[Node] = None,
    ):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        # curr_capacity = len(self.keyToNode)
        self.keyToNode = dict()
        self.max_capacity = capacity

        # newest = leftmost node
        self.newest = None

        # oldest = rightmost node
        self.oldest = None

    def removeNode(self, key: int) -> int:
        """We assume key is valid. Returns the value."""
        node = self.keyToNode[key]

        if node == self.newest:
            self.newest = self.newest.next

        if node == self.oldest:
            self.oldest = self.oldest.prev

        if node.next is not None:
            node.next.prev = node.prev

        if node.prev is not None:
            node.prev.next = node.next

        del self.keyToNode[key]

        val = node.val
        del node
        return val

    def addNode(self, key: int, val: int):
        new_node = Node(key, val)

        if self.oldest is None:
            self.oldest = new_node
            self.newest = new_node
        else:
            new_node.next = self.newest
            self.newest.prev = new_node
            self.newest = new_node

        self.keyToNode[key] = new_node

    def get(self, key: int) -> int:
        if key not in self.keyToNode:
            return -1

        val = self.removeNode(key)
        self.addNode(key, val)
        return val

    def put(self, key: int, val: int) -> None:
        if key in self.keyToNode:
            self.removeNode(key)
            self.addNode(key, val)
        else:
            if len(self.keyToNode) == self.max_capacity:
                self.removeNode(self.oldest.key)

            self.addNode(key, val)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
