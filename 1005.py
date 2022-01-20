from typing import Counter, List

class Solution:
  def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
    freq = Counter(nums)
    ans = sum(nums)
    # nums range [-100, 100]
    for i in range(-100, 0):
      if freq[i]:
        times = min(k, freq[i])
        ans -= i * times * 2
        # freq[i] -= times
        freq[-i] += times
        k -= times
        if k <= 0: break
    
    if k > 0 and k % 2:
        for i in range(0, 101):
          if freq[i]:
            ans -= i * 2
            break

    return ans