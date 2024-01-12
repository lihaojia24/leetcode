from collections import defaultdict
from typing import List

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        m1 = defaultdict(int)
        m2 = defaultdict(int)
        for word in words1:
            m1[word] += 1
        for word in words2:
            m2[word] += 1
        res = 0
        for k, v in m1.items():
            if v == 1 and m2[k] == 1:
                res += 1
        return res 

        