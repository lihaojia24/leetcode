# class CountIntervals:
#     __slots__ = 'left', 'right', 'l', 'r', 'cnt'

#     def __init__(self, l=1, r=10 ** 9):
#         self.left = self.right = None
#         self.l, self.r = l, r
#         self.cnt = 0

#     def add(self, l: int, r: int) -> None:
#         if self.r - self.l + 1 == self.cnt:
#             return
#         if l <= self.l and self.r <= r:
#             self.cnt = self.r - self.r + 1
#             return
#         mid = (self.l + self.r) // 2
#         if self.left == None: self.left = CountIntervals(self.l, mid)
#         if self.right == None: self.right = CountIntervals(mid+1, self.r)
#         if l <= mid: self.left.add(l, r)
#         if r >= mid+1: self.right.add(l, r)
#         self.cnt = self.left.cnt + self.right.cnt

#     def count(self) -> int:
#         return self.cnt



# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()

from sortedcontainers import SortedDict


class CountIntervals:

    def __init__(self):
        self.d = SortedDict()
        self.cnt = 0

    def add(self, left: int, right: int) -> None:
        i = self.d.bisect_left(left)
        while i < len(self.d) and self.d.values()[i] <= right:
            r, l = self.d.items()[i]
            left = min(left, l)
            right = max(right, r)
            self.cnt -= r - l + 1
            self.d.popitem(i)
        self.cnt += right - left + 1
        self.d[right] = left

    def count(self) -> int:
        return self.cnt


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()