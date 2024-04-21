package main

import "slices"

func combinationSum3(k int, n int) (ans [][]int) {
	st := []int{}
	var dfs func(i, left int)
	dfs = func(i, left int) {
		if left == 0 && len(st) == k {
			ans = append(ans, slices.Clone(st))
			return
		}
		if i > 9 || left < i || len(st) >= k {
			return
		}
		dfs(i+1, left)
		st = append(st, i)
		dfs(i+1, left-i)
		st = st[:len(st)-1]
	}
	dfs(1, n)
	return ans
}
