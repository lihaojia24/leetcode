from typing import List


class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        d0, d1 = arr[0], 0
        ans = d0
        for i in range(1, len(arr)):
            d1 = max(d1 + arr[i], d0)
            d0 = max(arr[i], d0+arr[i])
            ans = max(ans, d1, d0)
        return ans