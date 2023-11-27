from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        left = [-1] * n
        st = [-1]
        for i in range(n):
            while len(st) > 1 and st[-1] >= arr[i]:
                st.pop()
            left[i] = st[-1]
            st.append(i)
        right = [-1] * n
        st = [n]
        for i in range(n, -1):
            while len(st) > 0 and st[-1] > arr[i]:
                st.pop()
            right[i] = st[-1]
            st.append(i)
        ans = 0
        for i in range(n):
            ans += (right[i] - i) * (i - left[i]) * arr[i]
        return ans % (1e9 + 7)