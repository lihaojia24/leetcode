class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) > 1 and word[0].islower() and word[1].isupper():
            return False
        return all(word[i].isupper() == word[1].isupper() for i in range(2, len(word)))