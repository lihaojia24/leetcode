from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0: return [newInterval]
        if newInterval[0] > intervals[-1][1]: return intervals + [newInterval]
        if newInterval[1] < intervals[0][0]: return [newInterval] + intervals
        ans = []
        i = 0
        while intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1
        left = min(intervals[i][0], newInterval[0])
        if intervals[-1][1] < newInterval[1]: return(ans + [[left, newInterval[1]]])
        while intervals[i][1] < newInterval[1]:
            i += 1
        if newInterval[1] >= intervals[i][0]:
            right = intervals[i][1]
            i += 1
        else:
            right = newInterval[1]
        ans.append([left, right])
        while i < len(intervals):
            ans.append(intervals[i])
            i += 1
        return ans
    
class Solution2:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        return self.merge(intervals)

    def merge(self,intervals: List[List[int]]) -> List[List[int]]:
        if(len(intervals) < 2):return intervals
        intervals.sort(key = lambda x:x[0])
        res = []
        res.append(intervals[0].copy())
        for interval in intervals[1:]:
            if interval[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval.copy())

        return res