class Solution:
  def numberOfSteps(self, num: int) -> int:
    step = 0
    while num:
      step += 1
      if num & 1:
        num -= 1
      else:
        num >>= 1
    return step
