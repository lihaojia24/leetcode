from typing import List
class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []
        for word in words:
            res += [sp for sp in word.split(separator) if len(sp) > 0]
        return 