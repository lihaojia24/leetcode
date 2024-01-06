package main

import "sort"

func sumDistance(nums []int, s string, d int) int {
	const MOD = 1_000_000_007
	for i, ch := range s {
		nums[i] += d * int(ch&2-1)
	}
	sort.Ints(nums)
	tmp, ans := 0, 0
	for i, num := range nums {
		ans = (ans + i*num - tmp) % MOD
		tmp += num
	}
	return ans
}
