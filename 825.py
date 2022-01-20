from typing import List

class Solution:
  def numFriendRequests(self, ages: List[int]) -> int:
    cnt = [0] * 121
    for age in ages:
      cnt[age] += 1
    pre = [0] * 121
    for i in range(1, 121):
      pre[i] = pre[i - 1] + cnt[i]
    ans = 0
    for i in range(15, 121):
      if cnt[i] > 0:
        mIN = i // 2 + 7
        mAX = i
        tmp = pre[mAX] - pre[mIN] - 1
        ans += tmp * cnt[i]
    return ans