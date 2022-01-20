from typing import Counter, List

class Solution:
  def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
    cnt = Counter(ch for ch in licensePlate if ch.isalpha())
    return min((word for word in words if not cnt - Counter(word)) , key=len)