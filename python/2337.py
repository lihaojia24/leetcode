class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start.replace('_', '') != target.replace('_', ''):
            return False
        j = 0
        for i, c in enumerate(start):
            if c == '_': continue
            while target[j] == '_': j += 1
            if i != j and (c == 'L') == (i < j):
                return False
            j += 1
        return True