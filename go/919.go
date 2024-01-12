package main

// type TreeNode struct {
// 	Val   int
// 	Left  *TreeNode
// 	Right *TreeNode
// }

type CBTInserter struct {
	root   *TreeNode
	next   []*TreeNode
	isLeft bool
}

func Constructor919(root *TreeNode) CBTInserter {
	tree := CBTInserter{root, make([]*TreeNode, 0), false}
	q := []*TreeNode{root}
	for len(q) > 0 {
		node := q[0]
		if node.Left != nil && node.Right != nil {
			q = append(q, node.Left)
			q = append(q, node.Right)
			q = q[1:]
		} else {
			if node.Left != nil {
				q = append(q, node.Left)
			}
			tree.next = q
			tree.isLeft = node.Left == nil
			break
		}
	}
	return tree
}

func (this *CBTInserter) Insert(val int) int {
	node := this.next[0]
	newNode := &TreeNode{Val: val}
	if this.isLeft {
		node.Left = newNode
	} else {
		node.Right = newNode
		this.next = this.next[1:]
	}
	this.next = append(this.next, newNode)
	this.isLeft = !this.isLeft
	return node.Val
}

func (this *CBTInserter) Get_root() *TreeNode {
	return this.root
}

/**
 * Your CBTInserter object will be instantiated and called as such:
 * obj := Constructor(root);
 * param_1 := obj.Insert(val);
 * param_2 := obj.Get_root();
 */
