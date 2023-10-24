package main

func numRollsToTarget(n int, k int, target int) int {
	if target < n || target > n*k {
		return 0
	}
	const MOD = 1_000_000_007
	dp := make([][]int, n+1)
	for i := range dp {
		dp[i] = make([]int, target+1)
	}
	dp[0][0] = 1
	for i := 1; i < n+1; i++ {
		for j := 1; j < target+1; j++ {
			res := 0
			for d := 1; d < k+1; d++ {
				if j >= d {
					res = (res + dp[i-1][j-d]) % MOD
				}
			}
			dp[i][j] = res
		}
	}
	return dp[n][target]
}

func main() {

}
