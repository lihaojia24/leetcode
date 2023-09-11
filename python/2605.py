from typing import List

class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        l = [0] * 10
        m1, m2 = 10, 10
        for num in nums1:
            l[num] = 1
            m1 = num if num < m1 else m1
        for num in nums2:
            l[num] += 1
            m2 = num if num < m2 else m2
        for i, num in enumerate(l):
            if num > 1: return i
        return m1 * 10 + m2 if m1 < m2 else m2 * 10 + m1
    
n1 = [3,5,2,6]
n2 = [3,1,7]
s = Solution()
s.minNumber(n1, n2)