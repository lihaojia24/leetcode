package main

// func postorder(root *Node) (ans []int) {
// 	var helper func(node *Node)
// 	helper = func(node *Node) {
// 		for _, child := range node.Children {
// 			helper(child)
// 		}
// 		ans = append(ans, node.Val)
// 	}
// 	if root == nil {
// 		return
// 	}
// 	helper(root)
// 	return
// }

func postorder(root *Node) (ans []int) {
	if root == nil {
		return
	}
	st := []*Node{root}
	for len(st) > 0 {
		ans = append(ans, st[len(st)-1].Val)
		childs := st[len(st)-1].Children
		st = st[:len(st)-1]
		st = append(st, childs...)
	}
	for i, j := 0, len(ans)-1; i < j; i, j = i+1, j-1 {
		ans[i], ans[j] = ans[j], ans[i]
	}
	return
}
