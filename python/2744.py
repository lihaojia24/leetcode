from typing import List
class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        ans = 0
        s = set()
        for word in words:
            if word[::-1] in s:
                ans += 1
            s.add(word)
        return ans
