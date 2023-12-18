package main

import "math"

func findPeakElement(nums []int) int {
	n := len(nums)
	var get func(i int) int
	get = func(i int) int {
		if i == -1 || i == n {
			return math.MinInt64
		}
		return nums[i]
	}
	l, r := 0, n-1
	for l <= r {
		mid := (l + r) / 2
		if get(mid-1) < nums[mid] && get(mid+1) < nums[mid] {
			return mid
		}
		if get(mid-1) >= nums[mid] {
			r = mid - 1
		} else {
			l = mid + 1
		}
	}
	return -1
}
