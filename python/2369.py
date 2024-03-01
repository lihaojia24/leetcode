from typing import List

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * (n + 1)
        dp[0] = True
        dp[1] = False
        dp[2] = nums[1] == nums[0]
        for i in range(2, n):
            if nums[i] == nums[i-1]:
                if dp[i-2+1]: dp[i+1] = True
                if nums[i] == nums[i-2] and dp[i-3+1]: dp[i+1] = True
            elif nums[i] == nums[i-1] + 1 == nums[i-2] + 2 and dp[i-3+1]: dp[i+1] = True
        return dp[-1]