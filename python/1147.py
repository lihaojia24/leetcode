class Solution:
    def longestDecomposition(self, text: str) -> int:
        ans = 0
        t = 0
        while len(text) > 0:
            flag = 1
            for i in range(1, len(text) //2 + 1):
                if text[:i] == text[-i:]:
                    ans += 2
                    flag = 0
                    t = i
                    break
            ans += flag
            text = text[t:-t]
        return ans