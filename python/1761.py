from typing import List

class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int: 
        m = [[False] * (n+1) for _ in range(n+1)]
        nums = [0] * (n+1)
        ans = -1
        for x, y in edges:
            nums[x] += 1
            nums[y] += 1
            m[x][y] = True
            m[y][x] = True
        print(nums)
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                for k in range(j+1, n+1):
                    if m[i][j] and m[j][k] and m[i][k]:
                        x = nums[i] + nums[j] + nums[k] - 6
                        ans = x if ans == -1 else min(ans, x)
        return ans

s = Solution()
e = [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]]
n = 7
print(s.minTrioDegree(n,e))