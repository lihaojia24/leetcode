package main

func constructFromPrePost(preorder []int, postorder []int) *TreeNode {
	if len(preorder) == 0 {
		return nil
	}
	if len(preorder) == 1 {
		return &TreeNode{Val: preorder[0]}
	}
	node_val := preorder[0]
	left_root_val := preorder[1]
	i := 0
	for postorder[i] != left_root_val {
		i++
	}
	left_preorder := preorder[1 : i+2]
	right_preorder := preorder[i+2:]
	left_postorder := postorder[:i+1]
	right_postorder := postorder[i+1 : len(postorder)-1]
	return &TreeNode{
		node_val,
		constructFromPrePost(left_preorder, left_postorder),
		constructFromPrePost(right_preorder, right_postorder),
	}
}
