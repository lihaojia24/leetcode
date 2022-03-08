

from typing import List

# s = "**|**|***|", queries = [[2,5],[5,9]]
class Solution:
  def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
    candles = []
    candlesPreSum = []
    ans = []
    n, plateNum = len(s), 0
    leftCandles, rightCandles = [-1] * n, [-1] * n
    # PreSum
    preIndex = 0
    for i in range(n):
      if s[i] == '*': 
        plateNum += 1
        if candles: leftCandles[i] = len(candles) - 1
      else:
        candles.append(i)
        candlesPreSum.append(plateNum)
        leftCandles[i], rightCandles[i] = len(candles) - 1, len(candles) - 1
        for j in range(preIndex, i):
          rightCandles[j] = len(candles) - 1
        preIndex = i + 1
    # print(rightCandles)
    # print(leftCandles)
    # print(candles)
    if not candles: return [0] * len(queries)
    for q in queries:
      l, r = q[0], q[1]
      # print(l ,r )
      # print(rightCandles[l])
      # print(leftCandles[r])
      if rightCandles[l] == -1 or leftCandles[r] == -1 or rightCandles[l] >= leftCandles[r]: ans.append(0)
      else: ans.append(candlesPreSum[leftCandles[r]] - candlesPreSum[rightCandles[l]])
    return ans

solu = Solution()
s = "***|**|*****|**||**|*"
queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
print(solu.platesBetweenCandles(s, queries))