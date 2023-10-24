m = [0] * 1001
for i in range(1, 1001):
    s = str(i*i)
    n = len(s)
    def dfs(p: int, total: int) -> bool:
        if p == n: return total == i
        x = 0
        for j in range(p, n):
            x = x * 10 + int(s[j])
            if dfs(j+1, x + total): return True
        return False
    m[i] = m[i-1] + (i*i if dfs(0, 0) else 0)

class Solution:
    def punishmentNumber(self, n: int) -> int:
        return m[n]