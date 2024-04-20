package main

import (
	"slices"
	"sort"
)

func combinationSum(candidates []int, target int) (ans [][]int) {
	sort.Slice(candidates, func(i, j int) bool {
		return candidates[i] <= candidates[j]
	})
	n := len(candidates)
	path := []int{}
	var dfs func(i, left int)
	dfs = func(i, left int) {
		if left == 0 {
			ans = append(ans, slices.Clone(path))
			return
		}
		if i == n || candidates[i] > left {
			return
		}
		dfs(i+1, left)
		path = append(path, candidates[i])
		dfs(i, left-candidates[i])
		path = path[:len(path)-1]
	}
	dfs(0, target)
	return
}
