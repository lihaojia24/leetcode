from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
      sLen, pLen = len(s), len(p)
      if sLen < pLen:
        return []
      count = [0] * 26
      for i in range(pLen):
        count[ord(s[i]) - 97] += 1
        count[ord(p[i]) - 97] -= 1
      diff = [item == 0 for item in count].count(False)
      ans = []
      if diff == 0:
        ans.append(0)
      for i in range(sLen - pLen):
        if count[ord(s[i]) - 97] == 1:
          diff -= 1
        elif count[ord(s[i]) - 97] == 0:
          diff += 1
        count[ord(s[i]) - 97] -= 1
        if count[ord(s[i + pLen]) - 97] == -1:
          diff -= 1
        elif count[ord(s[i + pLen]) - 97] == 0:
          diff += 1
        count[ord(s[i + pLen]) - 97] += 1

        if diff == 0:
          ans.append(i + 1)
      return ans

      