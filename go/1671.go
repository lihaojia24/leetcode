package main

import "sort"

func minimumMountainRemovals(nums []int) int {
	n := len(nums)
	preMax := make([]int, n)
	st := []int{}
	for i := 0; i < n; i++ {
		x := nums[i]
		j := sort.SearchInts(st, x)
		if j == len(st) {
			st = append(st, x)
		} else {
			st[j] = x
		}
		preMax[i] = j + 1
	}
	st = []int{}
	sufMax := make([]int, n)
	for i := n - 1; i > -1; i-- {
		x := nums[i]
		j := sort.SearchInts(st, x)
		if j == len(st) {
			st = append(st, x)
		} else {
			st[j] = x
		}
		sufMax[i] = j + 1
	}
	ans := 0
	for i := 0; i < n; i++ {
		if preMax[i] > 1 && sufMax[i] > 1 {
			ans = max(ans, preMax[i]+sufMax[i]-1)
		}
	}
	return n - ans
}
