from re import X


class Solution:
  def countPrimeSetBits(self, left: int, right: int) -> int:
    def isPrime(x):
      if x < 2: return False
      i = 2
      while i * i <= x:
        if x % i == 0: return False
        i += 1
      return True

    primes = (2,3,5,7,11,13,17,19)
    ans = 0
    for i in range(left, right + 1):
      x, c = i, 0
      while x:
        # print(x)
        x -= x & -x
        c += 1
      if isPrime(c): ans += 1
    return ans

s = Solution()
print(s.countPrimeSetBits(6, 10))