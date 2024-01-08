package main

// type TreeNode struct {
// 	Val   int
// 	Left  *TreeNode
// 	Right *TreeNode
// }

// func max(a, b int) int {
// 	if a > b {
// 		return a
// 	}
// 	return b
// }

func largestValues(root *TreeNode) (ans []int) {
	if root == nil {
		return
	}
	maxV := root.Val
	q := []*TreeNode{root, nil}
	for len(q) > 0 {
		node := q[0]
		q = q[1:]
		if node != nil {
			maxV = max(node.Val, maxV)
			if node.Left != nil {
				q = append(q, node.Left)
			}
			if node.Right != nil {
				q = append(q, node.Right)
			}
		} else {
			ans = append(ans, maxV)
			if len(q) > 0 {
				q = append(q, nil)
				maxV = q[0].Val
			}
		}
	}
	return ans
}
