package main

import (
	"math"
)

func movesToMakeZigzag(nums []int) int {
	s := [2]int{}
	for i, x := range nums {
		left, right := math.MaxInt, math.MaxInt
		if i > 0 {
			left = nums[i-1]
		}
		if i < len(nums)-1 {
			right = nums[i+1]
		}
		s[i%2] += max(x-min(left, right)+1, 0)
	}
	return min(s[0], s[1])
}
