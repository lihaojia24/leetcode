class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        dp = [0] * (l2 + 1)
        for i in range(1, l1 + 1):
            dpNxt = [0] * (l2 + 1)
            for j in range(1, l2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dpNxt[j] = dp[j - 1] + 1
                else:
                    dpNxt[j] = max(dp[j], dpNxt[j - 1])
            dp = dpNxt
            print(dp)
        return dp[-1]

solu = Solution()
text1 = "abcbdab"
text2 = "bdcaba"
solu.longestCommonSubsequence(text1, text2)