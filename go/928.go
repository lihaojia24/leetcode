package main

import "slices"

func minMalwareSpread2(graph [][]int, initial []int) int {
	n := len(graph)
	vis := make([]bool, n)
	isInitial := make([]bool, n)
	for _, x := range initial {
		isInitial[x] = true
	}
	var nodeId, size int
	var dfs func(x int)
	dfs = func(x int) {
		vis[x] = true
		size++
		for y, conn := range graph[x] {
			if conn == 0 {
				continue
			}
			if isInitial[y] {
				if nodeId != -2 && nodeId != y {
					if nodeId == -1 {
						nodeId = y
					} else {
						nodeId = -2
					}
				}
			} else if !vis[y] {
				dfs(y)
			}
		}
	}
	cnt := make([]int, n)
	for i, seen := range vis {
		if seen || isInitial[i] {
			continue
		}
		nodeId = -1
		size = 0
		dfs(i)
		if nodeId > 0 {
			cnt[nodeId] += size
		}
	}
	maxCnt := 0
	minNodeId := -1
	for x, c := range cnt {
		if c > 0 && (c > maxCnt || c == maxCnt && x < minNodeId) {
			maxCnt = c
			minNodeId = x
		}
	}
	if minNodeId > 0 {
		return minNodeId
	}
	return slices.Min(initial)
}
