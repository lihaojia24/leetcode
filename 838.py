class Solution:
  def pushDominoes(self, dominoes: str) -> str:
    n = len(dominoes)
    ans = [list(dominoes), list(dominoes)]
    change = True
    tag = 1
    while change:
      tag = 1 - tag
      change = False
      for i in range(n):
        if ans[tag][i] == '.':
          evn = 1 if i > 0 and ans[tag][i-1] == 'R' else 0
          evn += -1 if i < n - 1 and ans[tag][i+1] == 'L' else 0
          if evn != 0:
            change = True
            ans[1-tag][i] = 'R' if evn == 1 else 'L'
        else:
          ans[1-tag][i] = ans[tag][i]
    return ''.join(ans[1-tag])



dominoes = ".L.R...LR..L.."
s = Solution()
print(s.pushDominoes(dominoes))