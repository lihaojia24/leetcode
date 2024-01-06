package main

func mergeInBetween(list1 *ListNode, a int, b int, list2 *ListNode) *ListNode {
	p1 := list1
	p2 := list1
	for i := 1; i <= b; i++ {
		if i < a {
			p1 = p1.Next
		}
		p2 = p2.Next
	}
	p2 = p2.Next
	p1.Next = list2
	for p1.Next != nil {
		p1 = p1.Next
	}
	p1.Next = p2
	return list1
}
