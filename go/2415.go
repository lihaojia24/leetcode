package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func reverseOddLevels(root *TreeNode) *TreeNode {
	var helper func(a, b *TreeNode, l int)
	helper = func(a, b *TreeNode, l int) {
		if a == nil {
			return
		}
		if l%2 == 1 {
			a.Val, b.Val = b.Val, a.Val
		}
		helper(a.Left, b.Right, l+1)
		helper(a.Right, b.Left, l+1)
	}
	helper(root.Left, root.Right, 1)
	return root
}
