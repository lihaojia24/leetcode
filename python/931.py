from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ans = []
        for i in matrix[0]:
            ans.append(i)
        for i in range(1, len(matrix)):
            tmp = []
            for j in range(len(ans)):
                t = ans[j]
                if j > 0:
                    t = min(t, ans[j-1])
                if j < len(ans) - 1:
                    t = min(t, ans[j+1])
                tmp.append(t + matrix[i][j])
            ans = tmp
        return min(ans)

s = Solution()
m = [[2,1,3],[6,5,4],[7,8,9]]
print(s.minFallingPathSum(m))