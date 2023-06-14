from typing import List

class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        mx = 0
        ans = 0
        for i in range(len(flips)):
            mx = max(mx, flips[i])
            if mx == i+1:
                ans += 1
        return ans
    
s = Solution()
fps = [3,2,4,1,5] 
print(s.numTimesAllBlue(fps))