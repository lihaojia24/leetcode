package main

func stoneGameVII(stones []int) int {
	n := len(stones)
	s := make([]int, n+1)
	for i, stone := range stones {
		s[i+1] = s[i] + stone
	}
	memo := make([][]int, n)
	for i := range memo {
		memo[i] = make([]int, n)
	}
	var dfs func(int, int) int
	dfs = func(i, j int) int {
		if i == j {
			return 0
		}
		if memo[i][j] == 0 {
			memo[i][j] = max(s[j+1]-s[i+1]-dfs(i+1, j), s[j]-s[i]-dfs(i, j-1))
		}
		return memo[i][j]
	}
	return dfs(0, n-1)
}
