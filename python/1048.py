from functools import cache
from typing import List

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        f = {}
        for word in words:
            res = 0
            for i in range(len(word)):
                nWord = word[:i] + word[i+1:]
                res = max(res, f.get(nWord, 0))
            f[word] = res + 1
        return max(f.values)

    
    def longestStrChain1(self, words: List[str]) -> int:
        ws = set(words)
        @cache
        def dfs(word: str) -> int:
            res = 0
            for i in range(len(word)):
                nWord = word[:i] + word[i+1:]
                if nWord in ws:
                    res = max(res, dfs(nWord))
            return res + 1
        return max([dfs(word) for word in words])
