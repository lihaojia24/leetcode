from collections import Counter
from typing import List

class Solution:
  def canReorderDoubled(self, arr: List[int]) -> bool:
    cnt = Counter(arr)
    if cnt[0] % 2: return False
    for x in sorted(arr, key=abs):
      if arr[2 * x] < arr[x]: return False
      arr[2 * x] -= arr[x]
    return True
