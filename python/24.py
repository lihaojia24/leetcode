# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return head
        preHead = ListNode(-1)
        preHead.next = head
        head = preHead
        while head.next and head.next.next:
            print(head.val)
            nx = head.next
            head.next = nx.next
            nx.next = nx.next.next
            head.next.next = nx
            head = nx
        return preHead.next
    def creatList(self, arr: List) -> ListNode:
        preHead = ListNode(-1)
        head = preHead
        for node in arr:
            head.next = ListNode(node)
            head = head.next
        return preHead.next
    def printList(self, node):
        str = ""
        while node:
            str += f' {node.val}'
            node = node.next
        print(str)

s = Solution()
head = s.creatList([1,2,3,4])
s.printList(head)
head2 = s.swapPairs(head)
s.printList(head2)