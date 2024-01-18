package main

import "slices"

func smallestMissingValueSubtree(parents []int, nums []int) []int {
	n := len(nums)
	ans := make([]int, n)
	for i := 0; i < n; i++ {
		ans[i] = 1
	}
	startNode := slices.Index(nums, 1)
	if startNode < 0 {
		return ans
	}
	g := make([][]int, n)
	for i := 1; i < n; i++ {
		pi := parents[i]
		g[pi] = append(g[pi], i)
	}
	vis := make(map[int]bool, n)
	var dfs func(int)
	dfs = func(i int) {
		vis[nums[i]] = true
		for _, c := range g[i] {
			if !vis[nums[c]] {
				dfs(c)
			}
		}
	}
	mex := 2
	for startNode >= 0 {
		dfs(startNode)
		for vis[mex] {
			mex++
		}
		ans[startNode] = mex
		startNode = parents[startNode]
	}
	return ans
}
