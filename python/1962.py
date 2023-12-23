from typing import List
from heapq import heapify, heapreplace

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i] = -piles[i]
        heapify(piles)
        while k > 0 and piles[0] < 0:
            heapreplace(piles, piles[0]//2)
            k-=1
        return -sum(piles)
