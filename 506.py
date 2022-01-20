from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
      scoreList = sorted(enumerate(score), key=lambda x: x[1], reverse=True)
      ans = [''] * len(score)
      ansList = ["Gold Medal","Silver Medal","Bronze Medal"]
      for index, (pos, _) in enumerate(scoreList):
        ans[pos] = str(index + 1) if index > 2 else ansList[index]
      return ans

solu = Solution()
score = [10,3,8,9,4]
print(solu.findRelativeRanks(score))