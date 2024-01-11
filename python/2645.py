class Solution:
    def addMinimum(self, word: str) -> int:
        res = 0
        if word[0] == 'b':
            res += 1
        if word[0] == 'c':
            res += 2
        for i in range(1, len(word)):
            x = ord(word[i]) - ord(word[i-1])
            if x == 0:
                res += 2
            elif x > 0:
                res += x - 1
            else:
                if x == -1:
                    res += 1
        if word[-1] == 'a':
            res += 2
        if word[-1] == 'b':
            res += 1
        return res