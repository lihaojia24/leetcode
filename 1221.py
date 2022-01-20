class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        res = 0
        for ch in s:
            if 'L' == ch:
                balance += 1
            else:
                balance -= 1
            if 0 == balance:
                res += 1
        return res

solu = Solution()
str = 'RLRRLLRLRL'
print(solu.balancedStringSplit(str))