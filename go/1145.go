package main

import "fmt"

func main() {

}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func btreeGameWinningMove(root *TreeNode, n int, x int) bool {
	fs, rs, ls := 0, 0, 0
	var dfs func(*TreeNode) int
	dfs = func(node *TreeNode) int {
		if node == nil {
			return 0
		}
		if node.Val != x {
			return 1 + dfs(node.Left) + dfs(node.Right)
		} else {
			rs = dfs(node.Right)
			ls = dfs(node.Left)
			return 1
		}
	}
	fs = dfs(root)
	fmt.Printf("fs: %v\n", fs)
	fmt.Printf("ls: %v\n", ls)
	fmt.Printf("rs: %v\n", rs)
	blueS := fs
	if rs > blueS {
		blueS = rs
	}
	if ls > blueS {
		blueS = ls
	}
	if blueS > n-blueS {
		return true
	}
	return false
}
