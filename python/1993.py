from typing import List


class LockingTree:

    def __init__(self, parent: List[int]):
        n = len(parent)
        self.locks = [0] * n
        self.parents = [[] for _ in range(n)]
        self.cgc = [[] for _ in range(n)]
        for node, p in enumerate(parent):
            deep = 1
            while p != -1:
                if deep < 3:
                    self.cgc[p].append(node)
                self.parents[node].append(p)
                p = parent[p]

    def lock(self, num: int, user: int) -> bool:
        if self.locks[num] > 0:
            return False
        self.locks[num] = user
        return True


    def unlock(self, num: int, user: int) -> bool:
        if self.locks[num] == user:
            self.locks[num] = 0
            return True
        return False


    def upgrade(self, num: int, user: int) -> bool:
        can = self.locks[num] == 0
        can = can and any(self.locks[i] > 0 for i in self.cgc[num])
        can = can and all(self.locks[i] == 0 for i in self.parents[num])
        if can:
            self.locks[num] = user
            for node in self.cgc[num]:
                self.locks[node] = 0
            return True
        return False



# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)