package main

func preorderTraversal(root *TreeNode) (ans []int) {
	st := []*TreeNode{}
	for root != nil || len(st) > 0 {
		if root != nil {
			ans = append(ans, root.Val)
			st = append(st, root)
			root = root.Left
		} else {
			root = st[len(st)-1]
			st = st[:len(st)-1]
			root = root.Right
		}
	}
	return
}
