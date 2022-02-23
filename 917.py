class Solution:
  def reverseOnlyLetters(self, s: str) -> str:
    ans = list(s)
    left, right = 0, len(s) - 1
    print(len(s))
    while left < right:
      while left < right and not s[left].isalpha():
        left += 1
      while left < right and not s[right].isalpha():
        right -= 1
      if left < right:
        ans[left], ans[right] = ans[right], ans[left]
      left += 1
      right -= 1
    return ''.join(ans)



solu = Solution()    
s = 'Test1ng-Leet=code-Q!'
print(solu.reverseOnlyLetters(s))