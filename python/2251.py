from bisect import bisect_right
from collections import defaultdict
from typing import List

def bisect_right(a, x, lo=0, hi=None):
    """Return the index where to insert item x in list a, assuming a is sorted.

    The return value i is such that all e in a[:i] have e <= x, and all e in
    a[i:] have e > x.  So if x already appears in the list, a.insert(x) will
    insert just after the rightmost x already there.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        # Use __lt__ to match the logic in list.sort() and in heapq
        # if x < a[mid]: hi = mid
        # else: lo = mid+1
        if a[mid] <= x: lo = mid + 1
        else: hi = mid
    return lo

def bisect_left(a, x, lo=0, hi=None):
    """Return the index where to insert item x in list a, assuming a is sorted.

    The return value i is such that all e in a[:i] have e < x, and all e in
    a[i:] have e >= x.  So if x already appears in the list, a.insert(x) will
    insert just before the leftmost x already there.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        # Use __lt__ to match the logic in list.sort() and in heapq
        if a[mid] < x: lo = mid+1
        else: hi = mid
    return lo

class Solution:
    def fullBloomFlowers1(self, flowers: List[List[int]], people: List[int]):
        starts = sorted(s for s,_ in flowers)
        ends = sorted(e for _,e in flowers)
        return [bisect_right(starts, t) - bisect_left(ends, t) for t in people]
    
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]):
        diff = defaultdict(int)
        for s, e in flowers:
            diff[s] += 1
            diff[e+1] -= 1
        diff_times = sorted(diff.keys())

        flower, j = 0, 0
        ans = [0] * len(people)
        for t, i in sorted(zip(people, range(len(people)))):
            while j < len(diff_times) and diff_times[j] <= t:
                flower += diff[diff_times[j]]
                j += 1
            ans[i] = flower
        return ans


    