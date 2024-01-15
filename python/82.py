# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0, head)
        pre = res
        while pre and pre.next and pre.next.next:
            nxt, nxxt = pre.next, pre.next.next
            if nxt.val != nxxt.val:
                pre = pre.next
            else:
                while nxxt.next and nxxt.val == nxxt.next.val:
                    nxxt = nxxt.next
                pre.next = nxxt.next
        return res.next