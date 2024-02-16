package main

import (
	"slices"
)

func zigzagLevelOrder(root *TreeNode) (ans [][]int) {
	if root == nil {
		return
	}
	var help func(nodes []*TreeNode) ([]int, []*TreeNode)
	help = func(nodes []*TreeNode) (res []int, nxtNodes []*TreeNode) {
		if len(nodes) < 1 {
			return
		}
		for _, node := range nodes {
			// fmt.Printf("res: %v\n", res)
			// fmt.Printf("node: %v\n", node)
			res = append(res, node.Val)
			if node.Left != nil {
				nxtNodes = append(nxtNodes, node.Left)
			}
			if node.Right != nil {
				nxtNodes = append(nxtNodes, node.Right)
			}
		}
		return
	}
	nodes := []*TreeNode{root}
	flag := 0
	for res, nodes := help(nodes); len(res) > 0; res, nodes = help(nodes) {
		if flag%2 == 1 {
			slices.Reverse(res)
		}
		ans = append(ans, res)
		flag++
		// fmt.Printf("ans: %v\n", ans)
	}
	return
}
