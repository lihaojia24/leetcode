package main

func insertGreatestCommonDivisors(head *ListNode) *ListNode {
	var gcd func(a, b int) int
	gcd = func(a, b int) int {
		if b == 0 {
			return a
		}
		return gcd(b, a%b)
	}
	pre, nxt := head, head.Next
	for nxt != nil {
		x := gcd(pre.Val, nxt.Val)
		pre.Next = &ListNode{x, nxt}
		pre = nxt
		nxt = nxt.Next
	}
	return head
}
