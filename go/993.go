package main

import "fmt"

type QNode struct {
	tn     *TreeNode
	father int
}

func isCousins(root *TreeNode, x int, y int) bool {
	var get_level_father func(*TreeNode, int) (int, int)
	get_level_father = func(root *TreeNode, i int) (int, int) {
		q := []*QNode{{root, -1}}
		level := -1
		for len(q) > 0 {
			level++
			lq := len(q)
			for j := 0; j < lq; j++ {
				node := q[0]
				q = q[1:]
				if node.tn.Val == i {
					return level, node.father
				}
				if node.tn.Left != nil {
					q = append(q, &QNode{node.tn.Left, node.tn.Val})
				}
				if node.tn.Right != nil {
					q = append(q, &QNode{node.tn.Right, node.tn.Val})
				}
			}
		}
		return -1, -1
	}
	l1, f1 := get_level_father(root, x)
	l2, f2 := get_level_father(root, y)
	fmt.Printf("level: %v-%v,father: %v-%v", l1, l2, f1, f2)
	return l1 == l2 && f1 != f2
}
