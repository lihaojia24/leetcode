class Solution:
    def checkValidString(self, s: str) -> bool:
        minCount, maxCount = 0, 0
        for ch in s:
            if '(' == ch:
                minCount, maxCount = minCount + 1, maxCount + 1
            elif ')' == ch:
                minCount, maxCount = minCount - 1, maxCount - 1
                if maxCount < 0:
                    return False
            else:
                minCount, maxCount = minCount - 1, maxCount + 1
        return minCount <= 0