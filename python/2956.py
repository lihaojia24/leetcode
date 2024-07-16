from typing import List

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        a1 = sum(x in s2 for x in nums1)
        a2 = sum(x in s1 for x in nums2)
        return [a1, a2]