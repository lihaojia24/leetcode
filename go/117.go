package main

type Node1 struct {
	Val   int
	Left  *Node1
	Right *Node1
	Next  *Node1
}

func connect(root *Node1) *Node1 {
	if root == nil {
		return nil
	}
	nodeList := []*Node1{root}
	levelList := []int{0}
	i := 0
	var node *Node1
	for i < len(nodeList) {
		node = nodeList[i]
		if node.Left != nil {
			nodeList = append(nodeList, node.Left)
			levelList = append(levelList, levelList[i]+1)
		}
		if node.Right != nil {
			nodeList = append(nodeList, node.Right)
			levelList = append(levelList, levelList[i]+1)
		}
		i++
	}
	for i := 0; i < len(nodeList)-1; i++ {
		if levelList[i] == levelList[i+1] {
			nodeList[i].Next = nodeList[i+1]
		}
	}
	return root
}

// func main() {

// }
