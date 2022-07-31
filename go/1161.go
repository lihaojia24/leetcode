package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func maxLevelSum(root *TreeNode) int {
	ans := []int{}
	var helper func(*TreeNode, int)
	helper = func(node *TreeNode, level int) {
		if level == len(ans) {
			ans = append(ans, 0)
		}
		ans[level] += node.Val
		if node.Left != nil {
			helper(node.Left, level+1)
		}
		if node.Right != nil {
			helper(node.Right, level+1)
		}
	}
	helper(root, 0)
	res := 0
	max := ans[0]
	for i := 1; i < len(ans); i++ {
		if ans[i] > max {
			res = i
			max = ans[i]
		}
	}
	return res + 1
}

func main() {

}
