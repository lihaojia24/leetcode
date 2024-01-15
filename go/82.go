package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteDuplicates2(head *ListNode) *ListNode {
	res := &ListNode{0, head}
	pre := res
	for pre != nil && pre.Next != nil && pre.Next.Next != nil {
		nxt, nxxt := pre.Next, pre.Next.Next
		if nxt.Val != nxxt.Val {
			pre = pre.Next
		} else {
			for nxxt.Next != nil && nxxt.Val == nxxt.Next.Val {
				nxxt = nxxt.Next
			}
			pre.Next = nxxt.Next
		}
	}
	return res.Next
}
