class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        strs = list(s)
        l, r = 0, len(strs)-1
        while l < r:
            if strs[l] != strs[r]:
                if ord(strs[l]) < ord(strs[r]):
                    strs[r] = strs[l]
                else:
                    strs[l] = strs[r]
            l += 1
            r -= 1
        return "".join(strs)