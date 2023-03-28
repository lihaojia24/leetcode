class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        ans = 0
        m, n = len(s), len(t)
        ends = [[0] * (n+1) for _ in range(m+1)]
        starts = [[0] * (n+1) for _ in range(m+1)]
        for i, a in enumerate(s, 1):
            for j, b in enumerate(t, 1):
                if a == b:
                    ends[i][j] = ends[i-1][j-1] + 1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if s[i] == t[j]:
                    starts[i][j] = starts[i+1][j+1] + 1
                else:
                    ans += (ends[i][j] + 1) * (starts[i+1][j+1] + 1)
        return ans