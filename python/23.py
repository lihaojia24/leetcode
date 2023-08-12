# Definition for singly-linked list.
from heapq import heapify, heappop, heappush
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


ListNode.__lt__ = lambda a, b: a.val < b.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = cur = ListNode()
        q = [h for h in lists if h]
        heapify(q)
        while q:
            h  = heappop(q)
            if h.next:
                heappush(q, h.next)
            cur.next = h
            cur = cur.next
        return ans.next
