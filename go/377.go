package main

func combinationSum4(nums []int, target int) int {
	memo := make([]int, target+1)
	for i := range memo {
		memo[i] = -1
	}
	var dfs func(i int) int
	dfs = func(i int) int {
		if i == 0 {
			return 1
		}
		if memo[i] != -1 {
			return memo[i]
		}
		res := 0
		for _, num := range nums {
			if num <= i {
				res += dfs(i - num)
			}
		}
		memo[i] = res
		return res
	}
}
