# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head and head.next:
            slow, fast = head, head.next
            # if slow == fast: return True
            while fast:
                if slow == fast: return True
                slow = slow.next
                fast = fast.next
                if slow == fast: return True
                if fast:
                    fast = fast.next
        return False