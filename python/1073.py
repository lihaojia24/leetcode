from typing import List

class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = 0
        tmp = 1
        for i in range(len(arr1)-1, -1, -1):
            ans += tmp * arr1[i]
            tmp *= -2
        tmp = 1
        for i in range(len(arr2)-1, -1, -1):
            ans += tmp * arr2[i]
            tmp *= -2
        return ans