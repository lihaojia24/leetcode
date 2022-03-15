from cmath import inf
from typing import List

class Solution:
  def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
    hSet = {k: v for v, k in enumerate(list1)}
    ans, indexSum = [], inf
    for i, item in enumerate(list2):
      if item in hSet:
        if i + hSet[item] < indexSum:
          ans = [item]
          indexSum = i + hSet[item]
        elif i + hSet[item] == indexSum:
          ans.append(item)
    return ans