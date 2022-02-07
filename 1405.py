class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
      ans = []
      cnt = [[a, 'a'], [b, 'b'], [c, 'c']]
      while True:
        cnt.sort(key = lambda x: -x[0])
        if cnt[0][0] <= 0:
          break
        if len(ans) > 1 and cnt[0][1] == ans[-1] == ans[-2]:
          if cnt[1][0] <= 0:
            break
          else:
            ans.append(cnt[1][1])
            cnt[1][0] -= 1
        else:
          ans.append(cnt[0][1])
          cnt[0][0] -= 1
      return ''.join(ans)

a = 7
b = 1
c = 0
solu = Solution()
print(solu.longestDiverseString(a,b,c))