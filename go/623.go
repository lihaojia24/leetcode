package main

// type TreeNode struct {
// 	Val   int
// 	Left  *TreeNode
// 	Right *TreeNode
// }

func addOneRow(root *TreeNode, val int, depth int) *TreeNode {
	var helper func(node *TreeNode, level int)
	helper = func(node *TreeNode, level int) {
		if level == depth-1 {
			leftChild := &TreeNode{Val: val, Left: node.Left}
			rightChild := &TreeNode{Val: val, Right: node.Right}
			node.Left = leftChild
			node.Right = rightChild
		} else {
			if node.Left != nil {
				helper(node.Left, level+1)
			}
			if node.Right != nil {
				helper(node.Right, level+1)
			}
		}
	}
	if depth == 1 {
		node := &TreeNode{Val: val, Left: root}
		root = node
	} else {
		helper(root, 1)
	}
	return root
}
