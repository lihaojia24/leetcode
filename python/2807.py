from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a: int, b: int) -> int:
            if b == 0:
                return a
            return gcd(b, a % b)
        pre, nxt = head, head.next
        while nxt != None:
            x = gcd(pre.val, nxt.val)
            pre.next = ListNode(x, nxt)
            pre = nxt
            nxt = nxt.next
        return head