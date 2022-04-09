class Solution:
    def maxPower(self, s: str) -> int:
      if len(s) == 0:
        return 0
      ans, tmp = 1, 1
      for i in range(1, len(s)):
        if s[i] == s[i - 1]:
          tmp += 1
          ans = tmp if tmp > ans else ans
        else:
          tmp = 1
      return ans