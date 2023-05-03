class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 3 != 0:
            return False
        stack = []
        for ch in s:
            stack.append(ch)
            if ''.join(stack[-3:]) == 'abc':
                stack[-3:] = []
        return len(stack) == 0
    
s = Solution()
print(s.isValid("abccba"))
            
