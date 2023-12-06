package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func bstToGst(root *TreeNode) *TreeNode {
	var s int
	var helper func(*TreeNode)
	helper = func(root *TreeNode) {
		if root != nil {
			helper(root.Right)
			s += root.Val
			root.Val = s
			helper(root.Left)
		}
	}
	helper(root)
	return root
}
