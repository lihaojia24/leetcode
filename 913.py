from typing import List

DRAW = 0
MOUSE_WIN = 1
CAT_WIN = 2

class Solution:
  def catMouseGame(self, graph: List[List[int]]) -> int:
    n = len(graph)
    dp = [[[-1] * n for _ in range(n)] for _ in range(2 * n)]

    def getResult(step, mouse, cat):
      if step >= 2 * n:
        return DRAW
      res = dp[step][mouse][cat]
      if res != -1:
        return res
      if mouse == 0:
        res = MOUSE_WIN
      elif mouse == cat:
        res = CAT_WIN
      else:
        res = getNextResult(step, mouse, cat)
      dp[step][mouse][cat] = res
      return res

    def getNextResult(step, mouse, cat):
      curMove = mouse if step % 2 == 0 else cat
      defaultRes = MOUSE_WIN if curMove == cat else CAT_WIN
      res = defaultRes
      for next in graph[curMove]:
        if curMove == cat and next == 0:
          continue
        nxtCat = next if curMove == cat else cat
        nxtMouse = next if curMove == mouse else mouse
        nxtRes = getResult(step + 1, nxtMouse, nxtCat)
        if nxtRes != defaultRes:
          res = nxtRes
          if nxtRes != DRAW:
            break
      return res

    return getResult(0,1,2)