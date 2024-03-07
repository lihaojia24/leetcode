from typing import List

class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        n = len(word)
        ans = [0] * n
        num = 0
        for i, ch in enumerate(word):
            num = (num * 10 + int(ch)) % m
            if num == 0:
                ans[i] = 1
        return ans

