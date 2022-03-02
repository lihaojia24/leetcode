class Solution:
  def nearestPalindromic(self, n: str) -> str:
    l = len(n)
    if l < 2: return str(int(n) - 1)
    # 100 -> 99
    if n[0] == '1' and all(ch == '0' for ch in n[1:]): return ''.join(['9'] * (l - 1))
    # 101 -> 99
    if n[0] == '1' and all(ch == '0' for ch in n[1:-1]) and n[-1] == '1': return ''.join(['9'] * (l - 1))
    # 99 -> 101
    if all(ch == '9' for ch in n): return f"{1}{''.join(['0'] * (l - 1))}{1}"
    ansList = []
    prefix = int(n[:(l + 1) // 2])
    for pre in range(prefix - 1, prefix + 2):
      pos = pre if l % 2 == 0 else pre // 10
      while pos:
        pre = 10 * pre + pos % 10
        pos //= 10
      ansList.append(pre)
    ans = -1
    num = int(n)
    for cand in ansList:
      if cand != num:
        if ans == -1 or abs(cand - num) < abs(ans - num) or (abs(cand - num) == abs(ans - num) and cand < ans):
          ans = cand
    return int(ans)



n = '9989999'
s = Solution()
print(s.nearestPalindromic(n))
