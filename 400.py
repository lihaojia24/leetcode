class Solution:
    def findNthDigit(self, n: int) -> int:
      d, count = 1, 9
      while n > d * count:
        n -= d * count
        d += 1
        count *= 10
      index = n - 1
      start = 10 ** (d - 1)
      num = start + index // d
      digitalIndex = index % d
      return num // 10 ** (d - digitalIndex - 1) % 10 