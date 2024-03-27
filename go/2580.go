package main

import "slices"

func countWays(ranges [][]int) int {
	const MOD = 1_000_000_007
	slices.SortFunc(ranges, func(a, b []int) int { return a[0] - b[0] })
	ans, max_r := 1, -1
	for _, p := range ranges {
		l, r := p[0], p[1]
		if l > max_r {
			ans = (ans * 2) % MOD
		}
		max_r = max(max_r, r)
	}
	return ans
}
