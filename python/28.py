# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # if list1 == None: return list2
        # if list2 == None: return list1
        # tmpHead = head = ListNode(-1)
        # while list1 or list2:
        #     val = 0
        #     if list1 and list2:
        #         if list1.val < list2.val:
        #             val = list1.val
        #             list1 = list1.next
        #         else:
        #             val = list2.val
        #             list2 = list2.val
        #     elif list1:
        #         val = list1.val
        #         list1 = list1.next
        #     else:
        #         val = list2.val
        #         list2 = list2.next
        #     head.next = ListNode(val)
        #     head = head.next
        # return tmpHead.next
        tmpHead = head = ListNode(-1)
        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        if list1 == None:
            head.next = list2
        else:
            head.next = list1
        return tmpHead.next