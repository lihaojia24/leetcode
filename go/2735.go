package main

import "slices"

func minCost(nums []int, x int) int64 {
	n := len(nums)
	ans := make([]int, n)
	for i := range ans {
		ans[i] = i * x
	}
	costs := make([]int, n)
	for i := range costs {
		costs[i] = nums[i]
	}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			costs[j] = min(costs[j], nums[(j+i)%n])
		}
		ans[i] += sum(costs)
	}
	res := slices.Min[[]int](ans)
	// res := ans[0]
	// for i := 1; i < n; i++ {
	// 	res = min()
	// }
	return int64(res)
}
