package main

func inorderTraversal(root *TreeNode) (ans []int) {

	st := []*TreeNode{}
	for root != nil || len(st) > 0 {
		if root != nil {
			st = append(st, root)
			root = root.Left
		} else {
			root = st[len(st)-1]
			st = st[:len(st)-1]
			ans = append(ans, root.Val)
			root = root.Right
		}
	}
	return
}
