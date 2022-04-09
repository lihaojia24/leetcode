from typing import List

# 树状数组
# https://leetcode-cn.com/problems/range-sum-query-mutable/solution/-by-hu-ge-8-t4rn/
class NumArray:

  def __init__(self, nums: List[int]):
    self.n = len(nums)
    self.nums = nums
    self.tree = [0] * self.n
    for i in range(self.n):
      self.add(i, nums[i])

  def upIndex(self, i: int) -> int:
    i += 1
    i += i & -i
    return i - 1
  
  def downIndex(self, i: int) -> int:
    i += 1
    i -= i & -i
    return i - 1

  def add(self, i: int, num: int) -> None:
    while i < self.n:
      self.tree[i] += num
      i = self.upIndex(i)

  def update(self, i: int, val: int) -> None:
    self.add(i, val - self.nums[i])
    self.nums[i] = val

  def preSum(self, i: int) -> int:
    s = 0
    while i > -1:
      s += self.tree[i]
      i = self.downIndex(i)
    return s

  def sumRange(self, left: int, right: int) -> int:
    return self.preSum(right) - self.preSum(left - 1)



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)