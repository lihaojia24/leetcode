class Solution:
  def checkPerfectNumber(self, num: int) -> bool:
    if num == 1:
      return False
    n = 2
    res = 0
    while n * n <= num:
      if num % n:
        res += n
        if n * n < num:
          res += num / n
      n += 1
    return res == num
