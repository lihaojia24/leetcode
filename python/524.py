from typing import List

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x: (-len(x), x))
        for dic in dictionary:
            i, j = 0, 0
            while i < len(s) and j < len(dic):
                if s[i] == dic[j]:
                    j += 1
                i += 1
            if j == len(dic):
                return dic
        return ""