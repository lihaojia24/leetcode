# class Node:
#     __slots__ = 'prev', 'next', 'key', 'val'

#     def __init__(self, key=0, val=0) -> None:
#         self.key = key
#         self.val = val

# class LRUCache:

#     def __init__(self, capacity: int):
#         self.n = 0
#         self.capacity = capacity
#         self.k2node = dict()
#         self.head = Node()
#         self.head.prev = self.head
#         self.head.next = self.head

#     def _insert(self, key: int, value: int) -> None:
#         node = Node(key, value)
#         node.next = self.head
#         node.prev = self.head.prev
#         node.prev.next = node
#         node.next.prev = node
#         self.k2node[key] = node

#     def _delete(self, key: int) -> None:
#         node = self.k2node[key]
#         node.prev.next = node.next
#         node.next.prev = node.prev
#         del self.k2node[key]

#     def _delete_last(self) -> None:
#         node = self.head.next
#         self._delete(node.key)
        

#     def _update(self, key: int, value: int) -> None:
#         self._delete(key)
#         self._insert(key, value)

#     def _get(self, key: int) -> int:
#         if key in self.k2node:
#             return self.k2node[key].val
#         return -1

#     def get(self, key: int) -> int:
#         val = self._get(key)
#         if val == -1: return -1
#         self._update(key, val)
#         return val

#     def put(self, key: int, value: int) -> None:
#         if key in self.k2node:
#             self._update(key, value)
#         else:
#             if self.n < self.capacity:
#                 self._insert(key, value)
#                 self.n += 1
#             else:
#                 self._delete_last()
#                 self._insert(key, value)


# # Your LRUCache object will be instantiated and called as such:
# lru = LRUCache(2)
# lru.put(1,1)
# lru.put(2,2)
# print(lru.get(1))
# lru.put(3,3)
# print(lru.get(2))
# lru.put(4,4)
# print(lru.get(1))
# print(lru.get(3))
# print(lru.get(4))

class Node:
    __slots__ = 'prev', 'next', 'key', 'value'

    def __init__(self, key, value):
        self.key = key
        self.value = value

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.n = 0
        self.head = Node(0, 0)
        self.head.next = self.head
        self.head.prev = self.head
        self.k2node = dict()

    def _move2front(self, node):
        node.prev.next = node.next
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
    
    def _removelast(self) -> Node:
        last = self.head.prev
        last.prev.next = self.head
        self.head.prev = last.prev
        return last 
    
    def _insert(self, node):
        node.next = self.head.next
        node.prev = self.head
        node.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.k2node:
            node = self.k2node[key]
            self._move2front(node)
            return node.value
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.k2node:
            node = self.k2node[key]
            node.value = value
            self._move2front(node)
        else:
            if self.n == self.cap:
                # delete last
                node = self._removelast()
                print(node.key, node.value)
                del self.k2node[node.key]
            else:
                self.n += 1
            node = Node(key, value)
            self.k2node[key] = node
            self._insert(node)
                

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
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)