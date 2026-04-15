from collections import defaultdict
from typing import Optional


class Node:
    def __init__(
        self,
        key: int,
        prev: Optional[Node] = None,
        next: Optional[Node] = None,
    ):
        self.key = key
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self):
        self.keyToNode = dict()

        # newest = leftmost node
        self.newest = None

        # oldest = rightmost node
        self.oldest = None

    def isEmpty(self) -> bool:
        return self.newest is None

    def removeNode(self, key: int):
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
        del node

    def addNode(self, key: int):
        new_node = Node(key)

        if self.oldest is None:
            self.oldest = new_node
            self.newest = new_node
        else:
            new_node.next = self.newest
            self.newest.prev = new_node
            self.newest = new_node

        self.keyToNode[key] = new_node


class LFUCache:
    def __init__(self, capacity: int):
        self.max_capacity = capacity
        self.min_freq = 0

        self.key_to_val = defaultdict(int)
        self.key_to_freq = dict()
        self.freq_to_keys_cache = dict()

    def bumpFreq(self, key: int):
        """Key is assumed to exist."""
        curr_freq = self.key_to_freq[key]

        self.freq_to_keys_cache[curr_freq].removeNode(key)
        if self.min_freq == curr_freq and self.freq_to_keys_cache[curr_freq].isEmpty():
            self.min_freq = curr_freq + 1

        curr_freq += 1
        self.key_to_freq[key] = curr_freq

        if curr_freq not in self.freq_to_keys_cache:
            self.freq_to_keys_cache[curr_freq] = LRUCache()

        self.freq_to_keys_cache[curr_freq].addNode(key)

    def removeOldest(self):
        """We assume the cache is not empty when this is called."""
        oldest_key = self.freq_to_keys_cache[self.min_freq].oldest.key

        self.freq_to_keys_cache[self.min_freq].removeNode(oldest_key)

        del self.key_to_val[oldest_key]
        del self.key_to_freq[oldest_key]

    def get(self, key: int) -> int:
        if key in self.key_to_val:
            self.bumpFreq(key)
            return self.key_to_val[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_val:
            self.key_to_val[key] = value
            self.bumpFreq(key)
        else:
            if len(self.key_to_val) == self.max_capacity:
                self.removeOldest()

            self.key_to_val[key] = value
            self.key_to_freq[key] = 1
            self.min_freq = 1

            if 1 not in self.freq_to_keys_cache:
                self.freq_to_keys_cache[1] = LRUCache()
            self.freq_to_keys_cache[1].addNode(key)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
