package main

import (
	"sort"
)

func kthLargestLevelSum(root *TreeNode, k int) int64 {
	res := []int64{}
	var helper func(node *TreeNode, level int)
	helper = func(node *TreeNode, level int) {
		if len(res) <= level {
			res = append(res, int64(node.Val))
		} else {
			res[level] += int64(node.Val)
		}
		if node.Left != nil {
			helper(node.Left, level+1)
		}
		if node.Right != nil {
			helper(node.Right, level+1)
		}
		return
	}
	helper(root, 0)
	sort.Slice(res, func(i, j int) bool {
		return res[i] > res[j]
	})
	if len(res) < k {
		return -1
	}
	return res[k-1]
}
