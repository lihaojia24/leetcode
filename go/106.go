package main

func buildTree2(inorder []int, postorder []int) *TreeNode {
	if len(inorder) == 0 {
		return nil
	}
	node_val := postorder[len(postorder)-1]
	i := 0
	for inorder[i] != node_val {
		i++
	}
	left_inorder := inorder[:i]
	right_inorder := inorder[i+1:]
	left_postorder := postorder[:i]
	right_postorder := postorder[i : len(postorder)-1]
	node := &TreeNode{}
	node.Val = node_val
	node.Left = buildTree2(left_inorder, left_postorder)
	node.Right = buildTree2(right_inorder, right_postorder)
	return node
}
