package main

import "sort"

func minSubsequence(nums []int) []int {
	sort.Slice(nums, func(i, j int) bool {
		return nums[i] > nums[j]
	})
	sum := 0
	for _, v := range nums {
		sum += v
	}
	sum /= 2
	ans := []int{}
	for _, v := range nums {
		sum -= v
		ans = append(ans, v)
		if sum < 0 {
			break
		}
	}
	return ans
}
