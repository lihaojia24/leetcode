class Solution:
    def findIntegers(self, n: int) -> int:
        ans = 0
        s = bin(n)[2:]
        fib = [1,2]
        while len(fib) <= len(s):
            fib.append(fib[-1] + fib[-2])
        for i in range(len(s)):
            if i != len(s) - 1 and s[i] == s[i+1] == '1':
                ans += fib[-i-1] 
                break
            elif s[i] == '1':
                ans += fib[-i-2]
            if i == len(s) - 1:
                ans += 1
        return ans
