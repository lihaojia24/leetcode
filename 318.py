from typing import DefaultDict, List
from functools import reduce
from itertools import product

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        masksHash = DefaultDict(int)
        for word in words:
            mask = reduce(lambda x, y : x | 1 << (ord(y) - ord('a')), word, 0)
            masksHash[mask] = max(masksHash[mask], len(word))   
        return max((masksHash[x] * masksHash[y] for x, y in product(masksHash, repeat=2) if x & y == 0), default=0)