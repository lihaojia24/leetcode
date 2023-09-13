from typing import List


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        checks = [[] for _ in range(n * n)]
        if grid[0][0] != 0: return False
        for i in range(n):
            for j in range(n):
                checks[grid[i][j]] = (i, j)
        for i in range(1, n * n):
            x, y = checks[i]
            px, py = checks[i-1]
            # print(i,x,y,px,py)
            dx, dy = abs(x - px), abs(y - py)
            print(dx, dy)
            if not ((dx == 2 and dy == 1) or (dx == 1 and dy == 2)):
                return False
        return True

g = [ [24,11,22,17, 4]
     ,[21,16, 5,12, 9]
     ,[ 6,23,10, 3,18]
     ,[15,20, 1, 8,13]
     ,[ 0, 7,14,19, 2]]
s = Solution()
print(s.checkValidGrid(g))