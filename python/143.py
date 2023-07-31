from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        

        def printList(node: ListNode) -> None:
            while node:
                print(node.val)
                node = node.next

        def reversList(node: ListNode) -> ListNode:
            nx = node.next
            node.next = None
            while nx:
                nx.next, nx, node = node, nx.next, nx
            return node 
        
        def mergeList(node1:ListNode, node2:ListNode) -> ListNode:
            while node2:
                nx1 = node1.next
                nx2 = node2.next
                node1.next = node2
                node1 = nx1
                if node1:
                    node2.next = node1
                node2 = nx2
        
        # printList(head)
        # s = reversList(head)
        # printList(s)
        if not (head and head.next and head.next.next):
            return
        s, f = head, head
        while f:
            if f.next and f.next.next:
                f = f.next.next
                s = s.next
            else: break
        tmp = s
        s = reversList(s.next)
        tmp.next = None
        f = head

        # 合并f, s
        mergeList(f, s)

        printList(f)

            
        # return None
    
head = ListNode(1)
node = head
for i in range(2,6):
    node.next = ListNode(i)
    node = node.next
s = Solution()
s.reorderList(head)
# s.printls
