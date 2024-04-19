package main

import (
	"math"
)

func minSkips(dist []int, speed int, hoursBefore int) int {
	const EPS = 1e-7
	n := len(dist)
	dp := make([][]float64, n+1)
	for i := range dp {
		dp[i] = make([]float64, n+1)
		for j := range dp[i] {
			dp[i][j] = math.Inf(1)
		}
	}
	dp[0][0] = 0.0
	for i := 1; i <= n; i++ {
		for j := 0; j <= i; j++ {
			if j != i {
				dp[i][j] = min(dp[i][j], math.Ceil(dp[i-1][j]+float64(dist[i-1])/float64(speed)-EPS))
			}
			if j != 0 {
				dp[i][j] = min(dp[i][j], dp[i-1][j-1]+float64(dist[i-1])/float64(speed))
			}
		}
	}
	for i := 0; i < n+1; i++ {
		if dp[n][i] < float64(hoursBefore)+EPS {
			return i
		}
	}
	return -1
}
