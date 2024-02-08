package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func replaceValueInTree(root *TreeNode) *TreeNode {
	head := &TreeNode{}
	head.Left = root
	sum_per_level := []int{}
	var dfs_1 func(*TreeNode, int)
	var dfs_2 func(*TreeNode, int)
	dfs_1 = func(node *TreeNode, l int) {
		if node == nil {
			return
		}
		if l >= len(sum_per_level) {
			sum_per_level = append(sum_per_level, 0)
		}
		left_node := node.Left
		right_node := node.Right
		if left_node != nil {
			sum_per_level[l] += left_node.Val
		}
		if right_node != nil {
			sum_per_level[l] += right_node.Val
		}
		if left_node != nil && right_node != nil {
			left_node.Val, right_node.Val = left_node.Val+right_node.Val, right_node.Val+left_node.Val
		}
		dfs_1(left_node, l+1)
		dfs_1(right_node, l+1)
	}
	dfs_2 = func(node *TreeNode, l int) {
		if node == nil {
			return
		}
		node.Val = sum_per_level[l] - node.Val
		dfs_2(node.Left, l+1)
		dfs_2(node.Right, l+1)
	}
	dfs_1(head, 0)
	dfs_2(root, 0)
	return root
}
