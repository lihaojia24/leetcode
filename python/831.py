class Solution:
    def maskPII(self, s: str) -> str:
        ans = ''
        if '@' in s:
            chs = s.split('@')
            chs[0] = chs[0].lower()
            chs[1] = chs[1].lower()
            ans += chs[0][0]
            ans += '*****'
            ans += chs[0][1]
            ans += '@'
            ans += chs[1]
        else:
            s = "".join([ch for ch in s if ch.isdigit()])
            end = '***-***-' + s[-4:]
            if len(s) > 10:
                ans += '+'
                ans += '*' * (len(s) - 10)
                ans += '-'
            ans += end
        return ans

s = Solution()
print(s.maskPII("1(234)567-890"))