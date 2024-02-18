package main

func preorder(root *Node) (res []int) {
	var helper func(*Node)
	helper = func(node *Node) {
		if node == nil {
			return
		}
		res = append(res, node.Val)
		for _, child := range node.Children {
			helper(child)
		}
	}
	helper(root)
	return
}
