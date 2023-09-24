class Node:
    __slots__ = 'prev', 'next', 'key', 'val'

    def __init__(self, key=0, val=0) -> None:
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.n = 0
        self.capacity = capacity
        self.k2node = dict()
        self.head = Node()
        self.head.prev = self.head
        self.head.next = self.head

    def _insert(self, key: int, value: int) -> None:
        node = Node(key, value)
        node.next = self.head
        node.prev = self.head.prev
        node.prev.next = node
        node.next.prev = node
        self.k2node[key] = node

    def _delete(self, key: int) -> None:
        node = self.k2node[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.k2node[key]

    def _delete_last(self) -> None:
        node = self.head.next
        self._delete(node.key)
        

    def _update(self, key: int, value: int) -> None:
        self._delete(key)
        self._insert(key, value)

    def _get(self, key: int) -> int:
        if key in self.k2node:
            return self.k2node[key].val
        return -1

    def get(self, key: int) -> int:
        val = self._get(key)
        if val == -1: return -1
        self._update(key, val)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.k2node:
            self._update(key, value)
        else:
            if self.n < self.capacity:
                self._insert(key, value)
                self.n += 1
            else:
                self._delete_last()
                self._insert(key, value)


# Your LRUCache object will be instantiated and called as such:
lru = LRUCache(2)
lru.put(1,1)
lru.put(2,2)
print(lru.get(1))
lru.put(3,3)
print(lru.get(2))
lru.put(4,4)
print(lru.get(1))
print(lru.get(3))
print(lru.get(4))