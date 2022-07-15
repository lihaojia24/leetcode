package main

type Node struct {
	Val         bool
	IsLeaf      bool
	TopLeft     *Node
	TopRight    *Node
	BottomLeft  *Node
	BottomRight *Node
}

func intersect(quadTree1 *Node, quadTree2 *Node) *Node {
	res := new(Node)
	if quadTree1.IsLeaf && quadTree2.IsLeaf {
		res.IsLeaf = true
		res.Val = quadTree1.Val && quadTree2.Val
	} else {
		res.IsLeaf = false
		res.TopLeft = intersect(quadTree1.TopLeft, quadTree2.TopLeft)
		res.TopRight = intersect(quadTree1.TopRight, quadTree2.TopRight)
		res.BottomLeft = intersect(quadTree1.BottomLeft, quadTree2.BottomLeft)
		res.BottomRight = intersect(quadTree1.BottomRight, quadTree2.BottomRight)
	}
	return res
}

func main() {

}
