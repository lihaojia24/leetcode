from typing import List

class Solution:
  def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
    wordSet = set()
    ans = []
    P = 131
    OFFSET = 128
    for word in words:
      ha = 0
      for ch in word:
        ha = ha * P + (ord(ch) - ord('a')) + OFFSET
      wordSet.add(ha)
    def check(word):
      n = len(word)
      ans = [-1] * (n + 1)
      ans[0] = 0
      for i in range(n + 1):
        if ans[i] == -1: continue
        ha = 0
        for j in range(i + 1, n + 1):
          ha = ha * P + (ord(word[j - 1]) - ord('a')) + OFFSET
          if ha in wordSet: ans[j] = max(ans[j], ans[i] + 1)
          if ans[n] > 1: return True
      return False
    for word in words:
      if check(word): ans.append(word)
    return ans
