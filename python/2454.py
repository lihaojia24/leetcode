from typing import List

class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        s1 = []
        s2 = []
        ans = [-1] * len(nums)
        for i, num in enumerate(nums):
            while s2 and num > s2[-1][0]:
                ans[s2[-1][1]] = num
                s2 = s2[:-1]
            x = 0
            while s1 and num > s1[-1][0]:
                x += 1
            s2.extend(s1[-x:])
            s1 = s1[:-x]
            s1.append([num, i])
        return ans