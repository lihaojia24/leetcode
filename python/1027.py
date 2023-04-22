from typing import List

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        ans = 1
        MAX_DIFF = 1001
        n = len(nums)
        dp = [[0] * MAX_DIFF for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j] - 500
                dp[i][diff] = max(dp[i][diff], dp[j][diff] + 1)
                ans = max(ans, dp[i][diff])
        return ans+1