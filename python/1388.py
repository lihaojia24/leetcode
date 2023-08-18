from typing import List


class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        n = len(slices) // 3
        def help(sc: List[int]) -> int:
            m = len(sc)
            dp = [[0] * (n+1) for _ in range(m+1)]
            for i in range(1, m+1):
                for j in range(1, n+1):
                    dp[i][j] = max(dp[i-1][j], sc[i-1] + (dp[i-2][j-1] if i >= 2 else 0))
            return dp[m][n]
        x, y = help(slices[1:]), help(slices[:-1])
        return max(x,y)
    
s = Solution()
print(s.maxSizeSlices(slices = [8,9,8,6,1,1]))