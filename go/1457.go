package main

// type TreeNode struct {
// 	Val   int
// 	Left  *TreeNode
// 	Right *TreeNode
// }

func pseudoPalindromicPaths(root *TreeNode) int {
	return dfs(root, 0)
}

func dfs(root *TreeNode, mask int) int {
	if root == nil {
		return 0
	}
	mask ^= 1 << root.Val
	if root.Left == root.Right {
		if mask&(mask-1) == 0 {
			return 1
		} else {
			return 0
		}
	}
	return dfs(root.Left, mask) + dfs(root.Right, mask)
}
