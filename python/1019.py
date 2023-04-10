# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ans = []
        st = []
        while head:
            while st and ans[st[-1]] < head.val:
                ans[st.pop()] = head.val
            st.append(len(ans))
            ans.append(head.val)
            head = head.next
        for i in st:
            ans[i] = 0
        return ans
        