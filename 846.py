from typing import Counter, List

class Solution:
  def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
    if len(hand) % groupSize != 0:
      return False
    hand.sort()
    cnt = Counter(hand)
    for num in hand:
      if cnt[num] == 0:
        continue
      for i in range(groupSize):
        if cnt[num + i] == 0:
          return False
        cnt[num + i] -= 1
    return True


