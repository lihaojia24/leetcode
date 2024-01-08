package main

// type TreeNode struct {
// 	Val   int
// 	Left  *TreeNode
// 	Right *TreeNode
// }

func findFrequentTreeSum(root *TreeNode) (ans []int) {
	m := map[int]int{}
	var sum func(*TreeNode) int
	sum = func(node *TreeNode) int {
		ans := node.Val
		if node.Left != nil {
			ans += sum(node.Left)
		}
		if node.Right != nil {
			ans += sum(node.Right)
		}
		m[ans] += 1
		return ans
	}
	sum(root)
	maxV := 0
	for k, v := range m {
		if v > maxV {
			maxV = v
			ans = []int{k}
		} else if v == maxV {
			ans = append(ans, k)
		}
	}
	return
}
