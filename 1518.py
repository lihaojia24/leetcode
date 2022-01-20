class Solution:
  def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
    res = numBottles
    while numBottles >= numExchange:
      tmp = numBottles // numExchange
      res += tmp
      numBottles -= (numExchange - 1) * tmp
    return res