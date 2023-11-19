from bisect import bisect_left
from typing import List

class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        ans = [-1] * len(queries)
        a = sorted(((a, b) for a, b in zip(nums1, nums2)), key=lambda x: -x[0])
        j = 0
        st = []
        for i, (x, y) in sorted(enumerate(queries), key=lambda q: -q[1][0]):
            while j < len(a) and a[j][0] >= x:
                ax, ay = a[j]
                if not st:
                    st.append((ay, ax + ay))
                elif ay > st[-1][0]:
                    while st and st[-1][1] <= ay + ax:
                        st.pop()
                    st.append((ay, ax + ay))
                j += 1
            p = bisect_left(st, (y, ))
            if p < len(st):
                ans[i] = st[p][1]
        return ans
