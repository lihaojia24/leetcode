from typing import List

class Solution:
  def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
    m, n = len(img), len(img[0])
    ans = [[0] * n for _ in range(m)]
    for i in range(m):
      for j in range(n):
        count = 0
        for x in range(max(0, i-1), min(m, i+2)):
          for y in range(max(0, j-1), min(n, j+2)):
            ans[i][j] += img[x][y]
            count += 1
        ans[i][j] //= count
    return ans

img = [[100,200,100],[200,50,200],[100,200,100]]
s = Solution()
print(s.imageSmoother(img))