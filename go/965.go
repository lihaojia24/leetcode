package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isUnivalTree(root *TreeNode) bool {
	val := root.Val
	q := []*TreeNode{root}
	for len(q) > 0 {
		tree := q[0]
		q = q[1:]
		if tree.Val != val {
			return false
		}
		if tree.Left != nil {
			q = append(q, tree.Left)
		}
		if tree.Right != nil {
			q = append(q, tree.Right)
		}
	}
	return true
}

func main() {

}
