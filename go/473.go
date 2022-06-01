package main

import (
	"fmt"
	"sort"
)

func makesquare(matchsticks []int) bool {
	total := 0
	for _, v := range matchsticks {
		total += v
	}
	if total%4 != 0 {
		return false
	}
	MAX_SIZE := total / 4

	sort.Slice(matchsticks, func(i, j int) bool {
		return matchsticks[i] > matchsticks[j]
	})
	edges := [4]int{}
	var dfs func(int) bool
	dfs = func(idx int) bool {
		if idx >= len(matchsticks) {
			return true
		}
		for i := 0; i < 4; i++ {
			edges[i] += matchsticks[idx]
			if edges[i] <= MAX_SIZE && dfs(idx+1) {
				return true
			}
			edges[i] -= matchsticks[idx]
		}
		return false
	}

	return dfs(0)
}

func makesquare2(matchsticks []int) bool {
	total := 0
	for _, v := range matchsticks {
		total += v
	}
	if total%4 != 0 {
		return false
	}
	MAX_SIZE := total / 4

	dp := make([]int, 1<<len(matchsticks))
	for i := 0; i < len(dp); i++ {
		dp[i] = -1
	}
	dp[0] = 0
	for s := 1; s < len(dp); s++ {
		for i, v := range matchsticks {
			if 1<<i&s != 0 {
				pre := s - 1<<i
				if dp[pre] != -1 && dp[pre]+v <= MAX_SIZE {
					dp[s] = (dp[pre] + v) % MAX_SIZE
					break
				}
			}
		}
	}
	return dp[len(dp)-1] == 0
}

func main() {
	matchsticks := []int{1, 3, 2, 2, 4, 4}
	fmt.Printf("makesquare(matchsticks): %v\n", makesquare2(matchsticks))
}
