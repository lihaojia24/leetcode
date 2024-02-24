package main

import "fmt"

func closestNodes(root *TreeNode, queries []int) (ans [][]int) {
	var getBounds func(nums []int, target int) []int
	getBounds = func(nums []int, target int) []int {
		if nums[0] > target {
			return []int{-1, nums[0]}
		}
		if nums[len(nums)-1] < target {
			return []int{nums[len(nums)-1], -1}
		}
		l, r := 0, len(nums)-1
		for l < r {
			m := (l + r) / 2
			if nums[m] >= target {
				r = m
			} else {
				l = m + 1
			}
		}
		if nums[l] == target {
			return []int{target, target}
		}
		return []int{nums[l-1], nums[l]}
	}
	nums := []int{}
	st := []*TreeNode{}
	for root != nil || len(st) > 0 {
		if root != nil {
			st = append(st, root)
			root = root.Left
		} else {
			root = st[len(st)-1]
			st = st[:len(st)-1]
			nums = append(nums, root.Val)
			root = root.Right
		}
	}
	fmt.Printf("nums: %v\n", nums)
	for _, target := range queries {
		ans = append(ans, getBounds(nums, target))
	}
	return
}
