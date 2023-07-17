class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1, n2 = len(num1), len(num2)
        n = max(n1, n2)
        ans = []
        f = 0
        for i in range(1, n+1):
            a = ord(num1[n1-i]) - 48 if n1 >= i else 0
            b = ord(num2[n2-i]) - 48 if n2 >= i else 0
            c = (a + b + f) % 10
            ans.append(str(c))
            f = (a + b + f - c) // 10
            print(a,b,c,f)
        if f == 1: ans.append('1')
        ans.reverse()
        return ''.join(ans)
    
s = Solution()
num1 = "456"
num2 =  "77"
print(s.addStrings(num1, num2))