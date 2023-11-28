class FrontMiddleBackQueue:

    def __init__(self):
        self.l = []

    def pushFront(self, val: int) -> None:
        self.l = [val] + self.l 

    def pushMiddle(self, val: int) -> None:
        mid = len(self.l) // 2
        self.l = self.l[:mid] + [val] + self.l[mid:]

    def pushBack(self, val: int) -> None:
        self.l.append(val)

    def popFront(self) -> int:
        if len(self.l) == 0:
            return -1
        val = self.l[0]
        self.l = self.l[1:]
        return val

    def popMiddle(self) -> int:
        if len(self.l) == 0:
            return -1
        mid = (len(self.l) - 1) // 2
        val = self.l[mid]
        self.l = self.l[:mid] + self.l[mid+1:]
        return val

    def popBack(self) -> int:
        if len(self.l) == 0:
            return -1
        return self.l.pop()


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()