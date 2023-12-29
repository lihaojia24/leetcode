from typing import List

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        a, b = prices[0], prices[1]
        for c in prices[2:]:
            if c < a:
                if a < b:
                    b = a
                a = c
            elif c < b:
                b = c
        return money if money - a - b < 0 else money - a - b
