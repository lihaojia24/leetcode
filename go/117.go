package main

type Node struct {
	Val   int
	Left  *Node
	Right *Node
	Next  *Node
}

func connect(root *Node) *Node {
	if root == nil {
		return nil
	}
	nodeList := []*Node{root}
	levelList := []int{0}
	i := 0
	var node *Node
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

func main() {

}
