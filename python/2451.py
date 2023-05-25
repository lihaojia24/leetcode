from typing import List


class Solution:
    def oddString(self, words: List[str]) -> str:
        n, l = len(words), len(words[0])
        for i in range(l - 1):
            d1 = ord(words[0][i+1]) - ord(words[0][i])
            d2 = ord(words[1][i+1]) - ord(words[1][i])
            if d1 == d2:
                for word in words[2:]:
                    if ord(word[i+1]) - ord(word[i]) != d1: return word
            else:
                d3 = ord(words[2][i+1]) - ord(words[2][i])
                return words[1] if d3 == d1 else words[0]
            
                
