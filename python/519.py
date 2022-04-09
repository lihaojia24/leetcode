from typing import List
import random

class Solution:
  def __init__(self, m: int, n: int):
    self.map = {}
    self.m = m
    self.n = n
    self.tag = m * n - 1

  def flip(self) -> List[int]:
    id = random.randint(0, self.tag)
    idx = self.map.get(id, id)
    self.map[id] = self.map.get(self.tag, self.tag)
    self.tag -= 1
    return [idx // self.n, idx % self.n]


  def reset(self) -> None:
    self.map = {}
    self.tag = self.m * self.n - 1



# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()