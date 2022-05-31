package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func sumRootToLeaf(root *TreeNode) int {
	q := []*TreeNode{root}
	ans := 0
	for len(q) > 0 {
		node := q[0]
		q = q[1:]
		if node.Left == nil && node.Right == nil {
			ans += node.Val
		}
		if node.Left != nil {
			node.Left.Val += node.Val * 2
			q = append(q, node.Left)
		}
		if node.Right != nil {
			node.Right.Val += node.Val * 2
			q = append(q, node.Right)
		}
	}
	return ans
}

func main() {

}
