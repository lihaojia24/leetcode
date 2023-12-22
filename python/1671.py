from bisect import bisect_left
from typing import List

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        preMax = [0] * n
        st = []
        for i, x in enumerate(nums):
            j = bisect_left(st, x)
            if j == len(st):
                st.append(x)
            else:
                st[j] = x
            preMax[i] = j + 1
        sufMax = [0] * n
        st = []
        for i in range(n-1, -1, -1):
            x = nums[i]
            j = bisect_left(st, x)
            if j == len(st):
                st.append(x)
            else:
                st[j] = x
            sufMax[i] = j + 1
        ans = 0
        for i in range(n):
            if preMax[i] > 1 and sufMax[i] > 1:
                ans = max(ans, preMax[i] + sufMax[i] - 1)
        return n - ans
