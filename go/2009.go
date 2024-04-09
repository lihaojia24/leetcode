package main

import "slices"

func minOperations(nums []int) int {
	n := len(nums)
	slices.Sort(nums)
	s_nums := slices.Compact(nums)
	ans, left := 0, 0
	for right, num := range s_nums {
		for s_nums[left] < num-n+1 {
			left++
		}
		ans = max(ans, right-left+1)
	}
	return n - ans
}
