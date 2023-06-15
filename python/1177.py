from typing import List

class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        preSum = [0]
        for ch in s:
            bit = 1 << ord(ch) - ord('a')
            preSum.append(preSum[-1] ^ bit)
        
        ans = []
        for l, r, k in queries:
            bits = (preSum[l] ^ preSum[r+1]).bit_count()
            ans.append(bits//2 <= k)
        return ans
    
s = Solution()
ss = "abcda"
qq = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
print(s.canMakePaliQueries(ss, qq))