
class Solution:
  def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
    n = len(answerKey)
    def countChar(ch: str) -> int:
      left, sum, ans = 0, 0, 0
      for right in range(n):
        if answerKey[right] != ch:
          sum += 1
        while sum > k:
          if answerKey[left] != ch: sum -= 1
          left += 1
        ans = max(ans, right - left + 1)
      return ans
    return max(countChar('T'), countChar('F'))

s = Solution()
print(s.maxConsecutiveAnswers('TTFTTFTT', 1))