from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        st = []
        ans = []
        def dfs(i, left: int) -> None:
            if left == 0 and len(st) == k:
                ans.append(st.copy())
                return
            if left < i or i > 9 or len(st) >= k:
                return 
            dfs(i+1, left)
            st.append(i)
            dfs(i+1, left-i)
            st.pop()
        dfs(1, n)
        return ans