package main

// type P struct {
// 	from int
// 	tip  int
// }

// func maxTaxiEarnings(n int, rides [][]int) int64 {
// 	dp := make([]int64, n+1)
// 	g := make([][]P, n+1)
// 	for _, ride := range rides {
// 		x, y, p := ride[0], ride[1], ride[2]
// 		g[y] = append(g[y], P{x, p})
// 	}
// 	for i := 1; i < n+1; i++ {
// 		dp[i] = dp[i-1]
// 		for _, p := range g[i] {
// 			dp[i] = max(dp[i], dp[p.from]+int64(i-p.from+p.tip))
// 		}
// 	}
// 	return dp[n]
// }
