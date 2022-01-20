from typing import List

class Solution:
    def numRescueBoats(self, peoples: List[int], limit: int) -> int:
        res = 0
        peoples.sort()
        left, right = 0, len(peoples) - 1
        while left <= right:
            if peoples[left] + peoples[right] <= limit:
                left += 1
            right -= 1
            res += 1
        return res 

peoples = [3,2,2,1]
limit = 3
solu = Solution()
print(solu.numRescueBoats(peoples, limit))