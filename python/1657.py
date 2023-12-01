class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        setA = set()
        setB = set()
        countA = [0] * 26
        countB = [0] * 26
        for word in word1:
            setA.add(word)
            countA[ord(word) - ord('a')] += 1
        for word in word2:
            setB.add(word)
            countB[ord(word) - ord('a')] += 1
        if setA != setB:
            return False
        countA.sort()
        countB.sort()
        for i in range(len(countB)):
            if countB[i] != countA[i]:
                return False
        return True