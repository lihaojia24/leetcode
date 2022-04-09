from typing import List

class Solution:
  def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
    text = text.split(' ')
    if len(text) < 3:
      return []
    ans = []
    for i in range(2, len(text)):
      if text[i-2] == first and text[i-1] == second:
        ans.append(text[i])
    return ans