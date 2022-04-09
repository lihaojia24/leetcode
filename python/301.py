from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        ans = []
        lremove, rremove = 0, 0
        for ch in s:
            if ch == '(':
                lremove += 1
            elif ch == ')':
                if lremove > 0:
                    lremove -= 1
                else:
                    rremove += 1
        
        l = len(s) - lremove - rremove

        def isValid(s):
            if len(s) != l:
                return False
            lcount = 0
            for ch in s:
                if ch == '(':
                    lcount += 1
                elif ch == ')':
                    if lcount > 0:
                        lcount -= 1
                    else:
                        return False
            return lcount == 0

        currSet = set([s])

        while True:
            for s in currSet:
                if isValid(s):
                    ans.append(s)
            if len(ans) > 0:
                return ans
            nextSet = set()
            for s in currSet:
                for i in range(len(s)):
                    if i > 0 and s[i] == s[i-1]:
                        continue
                    if s[i] == ')' or s[i] == '(':
                        nextSet.add(s[:i] + s[i+1:])
            currSet = nextSet
        
        

        


        # def helper(s, start, lcount, rcount, lremove, rremove):
        #     if lremove == 0 and rremove == 0:
        #         if isValid(s):
        #             ans.append(s)
        #         return
            
        #     for i in range(start, len(s)):
        #         if i > start and s[i] == s[i-1]:
        #             if s[i] == '(':
        #                 lcount += 1
        #             if s[i] == ')':
        #                 rcount += 1
        #             continue
        #         if lremove + rremove > len(s) - i:
        #             break
        #         if lremove > 0 and s[i] == '(':
        #             helper(s[:i] + s[i+1:], i, lcount, rcount, lremove - 1, rremove)
        #         if rremove > 0 and s[i] == ')':
        #             helper(s[:i] + s[i+1:], i, lcount, rcount, lremove, rremove - 1)
        #         if s[i] == '(':
        #             lcount += 1
        #         if s[i] == ')':
        #             rcount += 1
        #         if rcount > lcount:
        #             break
            
        # helper(s, 0, 0, 0, lremove, rremove)
        return ans
