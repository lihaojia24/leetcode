package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func inorderSuccessor(root *TreeNode, p *TreeNode) (res *TreeNode) {
	if p.Right != nil {
		res = p.Right
		for res.Left != nil {
			res = res.Left
		}
		return
	}
	node := root
	for node != nil {
		if node.Val > p.Val {
			res = node
			node = node.Left
		} else {
			node = node.Right
		}
	}
	return
}

func main() {

}
