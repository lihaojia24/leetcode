from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            f, s = head, head
            # while f:
            #     s = s.next
            #     f = f.next
            #     if f: f = f.next
            #     if f == None: return None
            #     if f == s:
            #         f = head
            #         break
            while True:
                if not (f.next and f.next.next): return None
                s, f = s.next, f.next.next
                if s == f:
                    f = head
                    break
            # while True:
            #     if s == f: return s
            #     s = s.next
            #     f = f.next
            while s != f:
                s, f = s.next, f.next
            return s
        return None