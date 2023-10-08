from typing import List
from math import inf

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold, nHold = -inf, 0
        for price in prices:
            new_hold = max(hold, nHold - price)
            nHold = max(nHold, hold + price - fee)
            hold = new_hold
        return nHold