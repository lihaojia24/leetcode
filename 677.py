
# 32ms, 14.8MB
class MapSum:

    def __init__(self):
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        self.map[key] = val

    def sum(self, prefix: str) -> int:
        res = 0
        for key, val in self.map.items():
            if key.startswith(prefix):
                res += val
        return res


# 36ms, 15.1MB
class MapSum:

    def __init__(self):
        self.map = {}
        self.prefixmap = {}

    def insert(self, key: str, val: int) -> None:
        delta = val
        if key in self.map:
            delta -= self.map[key]
        self.map[key] = val
        for i in range(len(key)):
            currPrefix = key[:i+1]
            if currPrefix in self.prefixmap:
                self.prefixmap[currPrefix] += delta
            else:
                self.prefixmap[currPrefix] = delta

    def sum(self, prefix: str) -> int:
        if prefix in self.prefixmap:
            return self.prefixmap[prefix]
        else:
            return 0

# 40ms, 15.3MB
class TreeNode:
    def __init__(self) -> None:
        self.val = 0
        self.next = [None] * 26

class MapSum:
    def __init__(self):
        self.map = {}
        self.prefixTree = TreeNode()

    def insert(self, key: str, val: int) -> None:
        delta = val
        if key in self.map:
            delta -= self.map[key]
        self.map[key] = val
        node = self.prefixTree
        for ch in key:
            index = ord(ch) - ord('a')
            if node.next[index] == None:
                node.next[index] = TreeNode()
            node.next[index].val += delta
            node = node.next[index]

    def sum(self, prefix: str) -> int:
        node = self.prefixTree
        for ch in prefix:
            index = ord(ch) - ord('a')
            if node.next[index] == None:
                return 0
            else:
                node = node.next[index]
        return node.val
            


# mapSum = MapSum();
# mapSum.insert("apple", 3);  
# mapSum.sum("ap");        
# mapSum.insert("app", 2);    
# mapSum.sum("ap");
