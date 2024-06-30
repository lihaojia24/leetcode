package main

func findTargetSumWays(nums []int, target int) int {
	s := 0
	for _, num := range nums {
		s += num
	}
	s -= abs(target)
	if s < 0 || s%2 == 1 {
		return 0
	}
	m := s / 2

	n := len(nums)
	memo := make([][]int, n)
	for i := range memo {
		memo[i] = make([]int, m+1)
		for j := range memo[i] {
			memo[i][j] = -1
		}
	}
	var dfs func(int, int) int
	dfs = func(i, c int) (res int) {
		if i < 0 {
			if c == 0 {
				return 1
			}
			return 0
		}
		p := &memo[i][c]
		if *p != -1 {
			return *p
		}
		defer func() { *p = res }()
		if c < nums[i] {
			return dfs(i-1, c)
		}
		return dfs(i-1, c) + dfs(i-1, c-nums[i])
	}
	return dfs(n-1, m)
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
