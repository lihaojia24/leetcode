from typing import List

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        total = 0
        ans = 0
        for score in satisfaction:
            if score + total > 0:
                ans += total + score
                total += score
            else: break
        return ans

satisfaction = [-1,-8,0,5,-9]
s= Solution()
print(s.maxSatisfaction(satisfaction))