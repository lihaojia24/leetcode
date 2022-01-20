from typing import DefaultDict, List

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for anchor in points:
            dic = DefaultDict(int)
            for point in points:
                dist = (anchor[0] - point[0]) * (anchor[0] - point[0]) + (anchor[1] - point[1]) * (anchor[1] - point[1])
                dic[dist] += 1
            for distNum in dic.values():
                res += distNum * (distNum - 1)
        return res