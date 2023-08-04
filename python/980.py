import copy
from typing import List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        grid_c = copy.deepcopy(grid)
        m, n = len(grid), len(grid[0])
        def dfs(x: int, y: int, remain: int) -> int:
            if x < 0 or y < 0 or x > m-1 or y > n-1 or grid[x][y] < 0: return 0
            # 需配合deepcopy使用，防止终点被修改为0而不是2
            if remain == 0:
                print(remain,x,y,grid[x][y])
                return 1 if grid[x][y] == 2 else 0
            # if grid[x][y] == 2:
            #     return 1 if remain == 0 else 0
            # print(remain,x,y,grid[x][y])
            # print(grid[x][y])
            grid[x][y] = -1
            ans = dfs(x-1,y,remain-1) + dfs(x,y-1,remain-1) + dfs(x+1,y,remain-1) + dfs(x,y+1,remain-1)
            grid[x][y] = grid_c[x][y]
            return ans
        remain = sum(row.count(0) for row in grid)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return dfs(i, j, remain + 1)
                
s = Solution()
grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
print(s.uniquePathsIII(grid))