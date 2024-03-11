class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split()
        for i, word in enumerate(words):
            words[i] = word.lower()
            if len(word) > 2:
                words[i] = word.title()
        return " ".join(words)