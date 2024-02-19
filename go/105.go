package main

func buildTree(preorder []int, inorder []int) *TreeNode {
	if len(preorder) == 0 {
		return nil
	}
	rootVal := preorder[0]
	i := 0
	for i < len(inorder) {
		if inorder[i] == rootVal {
			break
		}
		i++
	}
	left_preorder := preorder[1 : i+1]
	left_inorder := inorder[:i]
	right_preorder := preorder[i+1:]
	right_inorder := inorder[i+1:]
	node := &TreeNode{Val: rootVal}
	node.Left = buildTree(left_preorder, left_inorder)
	node.Right = buildTree(right_preorder, right_inorder)
	return node
}
