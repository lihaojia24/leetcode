# Definition for singly-linked list.
from random import randrange
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:

    def __init__(self, head: Optional[ListNode]):
      self.head = head

    def getRandom(self) -> int:
      res = 0
      count = 0
      node = self.head
      while node:
        count += 1
        if randrange(count) == 0:
          res = node.val
        node = node.next
      return res



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()