from typing import List

class Solution:
  def findRadius(self, houses: List[int], heaters: List[int]) -> int:
    houses.sort()
    heaters.sort()
    n = len(heaters)
    m = len(houses)
    i = 0
    res = [0] * m
    for j in range(m):
      while houses[j] > heaters[i] and i + 1 < n: i += 1
      if houses[j] <= heaters[i]:
        res[j] = heaters[i] - houses[j]
        if i > 0:
          res[j] = min(res[j], houses[j] - heaters[i - 1])
      else:
        res[j] = houses[j] - heaters[i]
    print(res)
    return max(res)

solu = Solution()
houses = [282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923]
heaters = [823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]
# [282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923]
# [823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]
# 161834419
# 841401046
print(solu.findRadius(houses, heaters))