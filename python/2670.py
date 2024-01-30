from typing import List

class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dis_from_left = [0] * n
        dis_from_right = [0] * (n + 1)
        s = set()
        dis = 0
        for i, num in enumerate(nums):
            if num not in s:
                dis += 1
                s.add(num)
            dis_from_left[i] = dis
        s = set()
        dis = 0
        for i in range(n-1, -1, -1):
            if nums[i] not in s:
                dis += 1
                s.add(nums[i])
            dis_from_right[i] = dis
        res = [0] * n
        for i in range(n):
            res[i] = dis_from_left[i] - dis_from_right[i+1]
        return res