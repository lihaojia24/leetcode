class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        # dp = [0] * (l2 + 1)
        dp = [i for i in range(l2 + 1)]
        for i in range(1, l1 + 1):
            dpNxt = [i] * (l2 + 1)
            for j in range(1, l2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dpNxt[j] = dp[j - 1]
                else:
                    dpNxt[j] = min(dp[j], dpNxt[j - 1]) + 1
            dp = dpNxt
            print(dp)
        return dp[-1]

solu = Solution()
text1 = "sea"
text2 = "eat"
solu.minDistance(text1, text2)