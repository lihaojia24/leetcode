from collections import Counter
from typing import List


class Solution:
  def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
    freq = Counter(s1.split()) + Counter(s2.split())

    ans = []
    for item, count in freq.items():
      if count == 1:
        ans.append(item)
        
    return ans