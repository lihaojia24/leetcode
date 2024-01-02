package main

import "fmt"

func removeNodes(head *ListNode) *ListNode {
	l := []int{}
	node := head
	for node != nil {
		l = append(l, node.Val)
		node = node.Next
	}
	m := l[len(l)-1]
	rm := []int{}
	for i := len(l) - 2; i > -1; i-- {
		if l[i] < m {
			rm = append(rm, i)
		} else {
			m = l[i]
		}
	}
	h := &ListNode{}
	h.Next = head
	node = h
	fmt.Printf("rm: %v\n", rm)
	for i, j := 0, len(rm)-1; j > -1; i++ {
		fmt.Printf("rm: %v, %v, %v\n", i, j, node.Val)
		if i == rm[j] {
			node.Next = node.Next.Next
			j--
		} else {
			node = node.Next
		}
	}
	return h.Next
}
