package main

import "math/bits"

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
type FindElements struct {
	root *TreeNode
}

func Constructor(root *TreeNode) FindElements {
	return FindElements{root}
}

func (f *FindElements) Find(target int) bool {
	target++
	cur := f.root
	for i := bits.Len(uint(target)) - 2; i > -1; i-- {
		bit := target >> i & 1
		if bit == 0 {
			cur = cur.Left
		} else {
			cur = cur.Right
		}
		if cur == nil {
			return false
		}
	}
	return true
}

/**
 * Your FindElements object will be instantiated and called as such:
 * obj := Constructor(root);
 * param_1 := obj.Find(target);
 */

// type FindElements map[int]bool

// func Constructor(root *TreeNode) FindElements {
// 	f := FindElements{}
// 	var dfs func(node *TreeNode, val int)
// 	dfs = func(node *TreeNode, val int) {
// 		if node == nil {
// 			return
// 		}
// 		f[val] = true
// 		dfs(node.Left, val*2+1)
// 		dfs(node.Right, val*2+2)
// 	}
// 	dfs(root, 0)
// 	return f
// }

// func (f FindElements) Find(target int) bool {
// 	return f[target]
// }

/**
 * Your FindElements object will be instantiated and called as such:
 * obj := Constructor(root);
 * param_1 := obj.Find(target);
 */
