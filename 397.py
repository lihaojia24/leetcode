# 236ms 14.9MB
class Solution:
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        elif n % 2 == 0:
            return 1 + self.integerReplacement(n // 2)
        else:
            return 1 + min(self.integerReplacement(n + 1), self.integerReplacement(n - 1))

# 24ms 14.9MB
from functools import lru_cache
class Solution:
    @lru_cache
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        elif n % 2 == 0:
            return 1 + self.integerReplacement(n // 2)
        else:
            return 1 + min(self.integerReplacement(n + 1), self.integerReplacement(n - 1))

# 36ms 14.8MB
class Solution:
    def integerReplacement(self, n: int) -> int:
        ans = 0
        while n != 1:
            if n % 2 == 0:
                n >>= 1
            elif n != 3 and (n >> 1 & 1) == 1: n += 1
            else: n -= 1
            ans += 1
        return ans
                