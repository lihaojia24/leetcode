from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        for i in [0, len(grid)-1]:
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    self.dfs([i,j], grid)
        for i in[0, len(grid[0])-1]:
            for j in range(len(grid)):
                if grid[j][i] == 0:
                    self.dfs([j,i], grid)
        ans = 0
        # print(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    ans += 1
                    self.dfs([i, j], grid)
        return ans
    
    def dfs(self, p:List[int], grid: List[List[int]]) -> None:
        # print(p)
        m, n = len(grid), len(grid[0])
        q = [p]
        trace = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while q:
            p = q.pop()
            x, y = p[0], p[1]
            grid[x][y] = 1
            for dx, dy in trace:
                if 0 <= x + dx < m and  0 <= y + dy < n and grid[x + dx][y + dy] == 0:
                    q.append([x+dx, y+dy])
        
grid = [[0,0,1,1,0,1,0,0,1,0],
        [1,1,0,1,1,0,1,1,1,0],
        [1,0,1,1,1,0,0,1,1,0],
        [0,1,1,0,0,0,0,1,0,1],
        [0,0,0,0,0,0,1,1,1,0],
        [0,1,0,1,0,1,0,1,1,1],
        [1,0,1,0,1,1,0,0,0,1],
        [1,1,1,1,1,1,0,0,0,0],
        [1,1,1,0,0,1,0,1,0,1],
        [1,1,1,0,1,1,0,1,1,0]]
        
g = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
s = Solution()
print(s.closedIsland(grid))