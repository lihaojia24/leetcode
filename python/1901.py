from typing import List

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        l, r = 0, len(mat) - 1
        while l < r:
            i = (l + r) // 2
            mx = max(mat[i])
            if mat[i+1][mat[i].index(mx)] > mx:
                l = i + 1
            else:
                r = i
        return [l, mat[l].index(max(mat[l]))]