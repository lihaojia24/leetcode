class Solution:
    def numDecodings(self, s: str) -> int:
        mod = 10**9 + 7

        n = len(s)
        a, b, c = 0, 1, 0
        for i in range(1, n + 1):
            if s[i - 1] != '0':
                if s[i - 1] == '*':
                    c += b * 9
                else:
                    c += b
            if i > 1 and s[i - 2] != '0':
                if s[i - 1] == '*':
                    if s[i - 2] == '*':
                        c += a * 15
                    elif s[i - 2] == '1':
                        c += a * 9
                    elif s[i - 2] == '2':
                        c += a * 6
                else:
                    if s[i - 2] == '*':
                        if int(s[i - 1]) < 7:
                            c += a * 2
                        else:
                            c += a
                    elif int(s[i - 2 : i]) <= 26:
                        c += a
                # elif int(s[i - 2 : i]) <= 26:
                #     if s[i - 2] == '*':
            print(a ,b ,c)
            a ,b ,c = b, c, 0
        print(a ,b ,c)
        return b % mod

solu = Solution()
print(solu.numDecodings("*********"))