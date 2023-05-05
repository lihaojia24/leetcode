from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        ans, l, t = 0, 0, 0
        for r, (pos, point) in enumerate(fruits):
            t += point
            while l <= r and pos - fruits[l][0] + min(abs(startPos - fruits[l][0]), abs(startPos - pos)) > k:
                t -= fruits[l][1]
                l += 1
            ans = max(ans, t)
        return ans
        

fruits = [[2,8],[6,3],[8,6]]
startPos = 5
k = 4
s = Solution()
print(s.maxTotalFruits(fruits, startPos, k))