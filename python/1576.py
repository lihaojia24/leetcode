class Solution:
  def modifyString(self, s: str) -> str:
    res = list(s)
    n = len(res)
    for index in range(n):
      if res[index] == '?':
        for ch in 'abc':
          if not ((index > 0 and res[index - 1] == ch) or (index < n - 1 and res[index + 1] == ch)):
            res[index] = ch
            break
    return ''.join(res)
