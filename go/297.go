package main

import (
	"fmt"
	"strconv"
	"strings"
)

type TreeNode1 struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type Codec1 struct{}

func Constructor11() (_ Codec) { return }

// Serializes a tree to a single string.
func (this *Codec) serialize(root *TreeNode) string {
	var dfsPre func(root *TreeNode) (preOrder []string)
	dfsPre = func(root *TreeNode) (preOrder []string) {
		if root == nil {
			return
		} else {
			preOrder = append([]string{strconv.Itoa(root.Val)}, dfsPre(root.Left)...)
			preOrder = append(preOrder, dfsPre(root.Right)...)
		}
		return
	}
	var dfsMid func(root *TreeNode) (midOrder []string)
	dfsMid = func(root *TreeNode) (midOrder []string) {
		if root == nil {
			return
		} else {
			midOrder = append(dfsMid(root.Left), strconv.Itoa(root.Val))
			midOrder = append(midOrder, dfsMid(root.Right)...)
		}
		return
	}
	preOrder := dfsPre(root)
	midOrder := dfsMid(root)
	preRes := strings.Join(preOrder, ",")
	midRes := strings.Join(midOrder, ",")
	res := preRes + "|" + midRes
	return res
}

// Deserializes your encoded data to tree.
func (this *Codec) deserialize(data string) *TreeNode {
	if data == "|" {
		return nil
	}
	order := strings.Split(data, "|")
	fmt.Printf("order: %v\n", order)
	preOrder := strings.Split(order[0], ",")
	fmt.Printf("preOrder: %v\n", preOrder)
	midOrder := strings.Split(order[1], ",")
	fmt.Printf("midOrder: %v\n", midOrder)

	var desFromList func([]string, []string) *TreeNode
	desFromList = func(pre []string, mid []string) *TreeNode {
		if len(pre) == 0 {
			return nil
		}
		rootNum := pre[0]
		root := &TreeNode{}
		root.Val, _ = strconv.Atoi(rootNum)
		preLen := 0
		for i, num := range mid {
			if num == rootNum {
				preLen = i
				break
			}
		}
		root.Left = desFromList(pre[1:preLen+1], mid[:preLen])
		root.Right = desFromList(pre[preLen+1:], mid[preLen+1:])
		return root
	}

	return desFromList(preOrder, midOrder)
}

/**
* Your Codec object will be instantiated and called as such:
* ser := Constructor();
* deser := Constructor();
* data := ser.serialize(root);
* ans := deser.deserialize(data);
 */

// func main() {
// 	ser := Constructor()
// 	root := &TreeNode{Val: 3}
// 	root.Left = &TreeNode{Val: 2}
// 	root.Right = &TreeNode{Val: 4}
// 	root.Left.Left = &TreeNode{Val: 3}
// 	// root.Right.Right = &TreeNode{Val: 5}
// 	// root = nil
// 	str := ser.serialize(root)
// 	tree := ser.deserialize(str)
// 	str2 := ser.serialize(tree)
// 	fmt.Printf("str: %v\n", str)
// 	fmt.Printf("tree: %v\n", tree)
// 	fmt.Printf("str2: %v\n", str2)
// }
