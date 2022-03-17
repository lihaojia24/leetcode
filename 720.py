from collections import defaultdict
from typing import List

class Solution:
  def longestWord(self, words: List[str]) -> str:
    wordic = defaultdict(set)
    maxL = 0
    for word in words:
      l = len(word)
      if l > maxL: maxL = l
      wordic[l].add(word)
    print(wordic)
    ansL = maxL
    for i in range(2, maxL + 1):
      tmp = wordic[i].copy()
      for word in wordic[i]:
        if word[:-1] not in wordic[i - 1]:
          tmp.remove(word)
      wordic[i] = tmp
      if len(wordic[i]) == 0:
        ansL = i - 1
        break
    print(wordic)
    if len(wordic[ansL]) == 0: return ""
    ans = wordic[ansL].pop()
    for word in wordic[ansL]:
      if word < ans: ans = word
    return ans



s = Solution()
words = ["wo","wor","worl","world"]
print(s.longestWord(words))