package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func inOrder(root *TreeNode) (res []int) {
	var dfs func(*TreeNode)
	dfs = func(node *TreeNode) {
		if node == nil {
			return
		} else {
			dfs(node.Left)
			res = append(res, node.Val)
			dfs(node.Right)
		}
	}
	dfs(root)
	return
}

func getAllElements(root1 *TreeNode, root2 *TreeNode) []int {
	nums1 := inOrder(root1)
	nums2 := inOrder(root2)
	p1, n1 := 0, len(nums1)
	p2, n2 := 0, len(nums2)
	res := make([]int, 0)
	for {
		if p1 == n1 {
			res = append(res, nums2[p2:]...)
			break
		}
		if p2 == n2 {
			res = append(res, nums1[p1:]...)
			break
		}
		if nums1[p1] < nums2[p2] {
			res = append(res, nums1[p1])
			p1++
		} else {
			res = append(res, nums2[p2])
			p2++
		}
	}
	return res
}

func main() {

}
