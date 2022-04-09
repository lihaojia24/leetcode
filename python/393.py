from typing import List


class Solution:
  def validUtf8(self, datas: List[int]) -> bool:
    MASK1, MASK2 = 1 << 7, (1 << 7) | (1 << 6)
    def getBytes(data):
      n, mask = 0, MASK1
      while (data & mask):
        n += 1
        if n > 4:
          return -1
        mask >>= 1
      return n
    n = len(datas)
    i = 0
    while i < n:
      # print(datas[i])
      m = getBytes(datas[i])
      # print(m)
      if m == -1 or m == 1: return False
      if m > 1:
        for j in range(1, m):
          if i + j > n - 1: return False
          if getBytes(datas[i + j]) != 1: return False
        i += m - 1
      i += 1
    return True

s = Solution()
datas = [240,162,138,147,145]
print(s.validUtf8(datas))