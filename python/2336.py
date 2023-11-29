from sortedcontainers import SortedSet

class SmallestInfiniteSet:

    def __init__(self):
        self.minNum = 0
        self.s = SortedSet()

    def popSmallest(self) -> int:
        if len(self.s) > 0:
            return self.s.pop(0)
        self.minNum += 1
        return self.minNum

    def addBack(self, num: int) -> None:
        if num <= self.minNum:
            self.s.add(num)




# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)