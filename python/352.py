from sortedcontainers import SortedDict
from typing import List

class SummaryRanges:

    def __init__(self):
        self.intervals = SortedDict()


    def addNum(self, val: int) -> None:
        intervals_ = self.intervals
        keys_ = intervals_.keys()
        values_ = intervals_.values()
        n = len(intervals_)

        l1 = intervals_.bisect_right(val)
        l0 = l1 - 1 if l1 != 0 else n

        if l0 != n and keys_[l0] <= val <= values_[l0]:
            return
        
        left_aside = (l0 != n) and val == values_[l0] + 1
        right_aside = (l1 != n) and val == keys_[l1] - 1

        if left_aside and right_aside:
            left, right = keys_[l0], values_[l1]
            intervals_.popitem(l1)
            intervals_.popitem(l0)
            intervals_[left] = right
        elif left_aside:
            intervals_[keys_[l0]] += 1
        elif right_aside:
            right = values_[l1]
            intervals_.popitem(l1)
            intervals_[val] = right
        else:
            intervals_[val] = val


    def getIntervals(self) -> List[List[int]]:
        return list(self.intervals.items())



# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()