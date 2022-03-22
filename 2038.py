
class Solution:
  def winnerOfGame(self, colors: str) -> bool:
    countA, countB = 0, 0
    ansA, ansB = 0, 0
    for ch in colors:
      if ch == 'A':
        countA += 1
        if countB > 2:
          ansB += countB - 2
        countB = 0
      if ch == 'B':
        countB += 1
        if countA > 2:
          ansA += countA - 2
        countA = 0
    if countA > 2:
      ansA += countA - 2
    if countB > 2:
      print(countB)
      ansB += countB - 2
    print(ansA, ansB)
    return ansA > ansB

colors = "AAABABB"
s = Solution()
print(s.winnerOfGame(colors))


