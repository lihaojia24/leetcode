from collections import Counter
from typing import List

class Solution:
  def canReorderDoubled(self, arr: List[int]) -> bool:
    cnt = Counter(arr)
    if cnt[0] % 2: return False
    for x in sorted(cnt, key=abs):
      if cnt[2 * x] < cnt[x]: return False
      cnt[2 * x] -= cnt[x]
    return True
