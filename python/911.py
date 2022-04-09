from typing import DefaultDict, List

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
      winners = []
      voteCounts = DefaultDict(int)
      voteCounts[-1] = -1
      winer = -1
      for p in persons:
        voteCounts[p] += 1
        if voteCounts[p] > voteCounts[winer]:
          winer = p
        winners.append(winer)
      self.times = times
      self.winners = winners

    def q(self, t: int) -> int:
      l = 0
      r = len(self.times) - 1
      while l < r:
        mid = (l + r) // 2
        if self.times[mid] == t:
          return self.winners[mid]
        elif self.times[mid] < t:
          l = mid
        else:
          r = mid - 1
      return self.winners[l]

def m(nums, num):
  l = 0
  r = len(nums) - 1
  while l < r:
    mid = (l + r) // 2
    # if nums[mid] == num:
    #   return mid
    if nums[mid] < num:
      l = mid + 1
    else:
      r = mid 
  return l - 1

nums = [1,3,5,9,13,14]
for i in range(15):
  print(i, m(nums, i))