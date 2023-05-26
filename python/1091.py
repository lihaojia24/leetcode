from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1: return -1
        directs = [[-1, -1], [-1, 0], [-1, 1],
                  [0, -1], [0, 1],
                  [1, -1], [1, 0], [1, 1]]
        n = len(grid)
        if n == 1: return 1
        q = deque([[0, 0]])
        grid[0][0] = 1
        step = 1
        while q:
            print(q)
            step += 1
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in directs:
                    nx, ny = x + dx, y + dy
                    if -1 < nx < n and -1 < ny < n and grid[nx][ny] == 0:
                        if nx == ny == n-1: return step
                        q.append([nx, ny])
                        grid[nx][ny] = 1
        return -1
    
grid = [[1,0,0],
        [1,1,0],
        [1,1,0]]
s = Solution()
print(s.shortestPathBinaryMatrix(grid))