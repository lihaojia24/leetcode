from collections import defaultdict
from typing import Tuple


class Node:
    __slots__ = 'prev', 'next', 'key', 'value', 'freq'

    def __init__(self, key=0, value=0, freq=1):
        self.key = key
        self.value = value
        self.freq = freq

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.k2node = dict()
        self.min_freq = 0
        self.n = 0
        def new_list() -> Node:
            head = Node()
            head.prev = head
            head.next = head
            return head
        self.f2list = defaultdict(new_list)

    def _get(self, key: int) -> Tuple[int, int]:
        if key in self.k2node:
            return self.k2node[key].value, self.k2node[key].freq
        return -1, -1
    
    def _insert(self, key: int, value: int, freq: int) -> None:
        self.n += 1
        node = Node(key, value, freq)
        head = self.f2list[freq]
        node.next = head.next
        node.prev = head
        node.next.prev = node
        node.prev.next = node
        self.k2node[key] = node
        if freq < self.min_freq or self.min_freq == 0: self.min_freq = freq

    def _delete(self, key: int) -> None:
        self.n -= 1
        node = self.k2node[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.k2node[key]
        freq = node.freq
        head = self.f2list[freq]
        if head == head.next:
            del self.f2list[freq]
            if freq == self.min_freq:
                self.min_freq = min(self.f2list.keys(), default=0)

    def _delete_last_node(self) -> None:
        head = self.f2list[self.min_freq]
        self._delete(head.prev.key)
        
    def get(self, key: int) -> int:
        value, freq = self._get(key)
        if value == -1: return -1
        self._delete(key)
        self._insert(key, value, freq+1)
        return value

    def put(self, key: int, value: int) -> None:
        o_value, freq = self._get(key)
        if o_value == -1:
            if self.n >= self.capacity:
                self._delete_last_node()
            self._insert(key, value, 1)
        else:
            self._delete(key)
            self._insert(key, value, freq+1)
        




# Your LFUCache object will be instantiated and called as such:
lfu = LFUCache(2)
lfu.put(1,1)
lfu.put(2,2)
print(lfu.get(1))
lfu.put(3,3)
print(lfu.get(2))
print(lfu.get(3))
lfu.put(4,4)
print(lfu.get(1))
print(lfu.get(3))
print(lfu.get(4))
