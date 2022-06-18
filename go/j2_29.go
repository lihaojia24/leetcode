package main

type Node struct {
	Val  int
	Next *Node
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func insertNext(node *Node, x int) {
	xNode := &Node{Val: x}
	xNode.Next = node.Next
	node.Next = xNode
	return
}

func insert(aNode *Node, x int) *Node {
	if aNode == nil {
		node := &Node{Val: x}
		node.Next = node
		return node
	}
	head := aNode
	aNode = aNode.Next
	minVal, maxVal := head.Val, head.Val
	for aNode != head {
		maxVal = max(aNode.Val, maxVal)
		minVal = -1 * max(-1*aNode.Val, -1*minVal)
		aNode = aNode.Next
	}
	if minVal == maxVal {
		insertNext(head, x)
		return head
	}
	// find starter
	aNode = aNode.Next
	for aNode != head {
		if aNode.Val == maxVal && aNode.Next.Val == minVal {
			break
		} else {
			aNode = aNode.Next
		}

	}
	if x >= maxVal || x <= minVal {
		insertNext(aNode, x)
		return head
	}
	for {
		if aNode.Next.Val >= x {
			insertNext(aNode, x)
			return head
		}
		aNode = aNode.Next
	}
}

func main() {

}
