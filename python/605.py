from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ans = 0
        l = len(flowerbed)
        i = 0
        while i < l:
            if flowerbed[i] == 0:
                if (i == l - 1 or flowerbed[i+1] == 0):
                    ans += 1
                    i += 2
                else: i += 1
            else : i += 2
        return ans >= n

s = Solution()
print(s.canPlaceFlowers([1,0,0,1,0,0,1], 1))