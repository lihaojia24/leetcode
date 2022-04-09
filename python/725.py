# Definition for singly-linked list.
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        n = 0
        tmp = head
        while tmp:
            n += 1
            tmp = tmp.next
        
        length = n // k
        res = n % k

        rest = [None for _ in range(k)]
        for i in range(k):
            lengthT = length + (1 if i < res else 0)
            if lengthT == 0:
                pass
            else:
                rest[i] = head
                for _ in range(lengthT - 1):
                    head = head.next
                tmp = head.next
                head.next = None
                head = tmp
        return rest

