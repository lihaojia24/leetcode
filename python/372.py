from typing import List

class Solution:
  def superPow(self, a: int, b: List[int]) -> int:
    MOD = 1337
    def helper(a, b, p):
      if p == -1: return 1
      return ((helper(a, b, p - 1) ** 10) * a ** b[p]) % MOD
    
    def quick_pow(a, b):
      res = 1
      while b:
        if b % 2 == 1:
          res = (res * a) % MOD
        b >> 1
        a = (a * a) % MOD
      return res
        
    return helper(a, b, len(b)-1)