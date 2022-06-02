package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

//递归
func deleteNode(root *TreeNode, key int) (ans *TreeNode) {
	ans = root
	if root == nil {
		return
	}
	if key > root.Val {
		root.Right = deleteNode(root.Right, key)
	} else if key < root.Val {
		root.Left = deleteNode(root.Left, key)
	} else {
		if root.Left == nil {
			return root.Right
		}
		if root.Right == nil {
			return root.Left
		}
		nxt := root.Right
		for nxt.Left != nil {
			nxt = nxt.Left
		}
		root.Val = nxt.Val
		root.Right = deleteNode(root.Right, nxt.Val)
		return root
	}
	return
}

//迭代
func deleteNode2(root *TreeNode, key int) (ans *TreeNode) {

	// find
	ans = root
	var pre *TreeNode
	for root != nil && root.Val != key {
		pre = root
		if root.Val > key {
			root = root.Left
		} else {
			root = root.Right
		}
	}
	if root == nil {
		return
	}

	if root.Right != nil && root.Left != nil {
		cur := root
		pre, root = root, root.Right
		for root.Left != nil {
			pre, root = root, root.Left
		}
		cur.Val, root.Val = root.Val, cur.Val

	}

	if root.Left == nil {
		root = root.Right
	} else {
		root = root.Left
	}

	if pre == nil {
		return root
	}
	fmt.Printf("pre: %v\n", pre)
	fmt.Printf("pre.Left: %v\n", pre.Left)
	fmt.Printf("pre.Right: %v\n", pre.Right)
	if pre.Left != nil && pre.Left.Val == key {
		pre.Left = root
	} else {
		pre.Right = root
	}

	return
}

func main() {

}
