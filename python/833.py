from typing import List

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        ansNode = [(ch, 1) for ch in s]
        for i, src, tar in zip(indices, sources, targets):
            if s.startswith(src, i):
                ansNode[i] = (tar, len(src))
        ansList = []
        i = 0
        while i < len(s):
            ansList.append(ansNode[i][0])
            i += ansNode[i][1]
        return ''.join(ansList)
