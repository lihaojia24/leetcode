from typing import List

class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        pairs = sorted(zip(nums1, nums2), key=lambda p: p[1])
        n = len(pairs)
        res = [0] * (n + 1)
        for i, (a, b) in enumerate(pairs):
            for j in range(i+1, 0, -1):
                res[j] = max(res[j], res[j-1] + a + b * j)
        s1 = sum(nums1)
        s2 = sum(nums2)
        for j, v in enumerate(res):
            if s1 + s2 * j - v <= x:
                return j
        return -1
