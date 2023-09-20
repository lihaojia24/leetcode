from typing import List

class Solution:
    def minCount(self, coins: List[int]) -> int:
        return sum(coin // 2 + coin % 2 for coin in coins)