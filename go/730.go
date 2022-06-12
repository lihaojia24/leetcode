package main

import "fmt"

func countPalindromicSubsequences(s string) int {
	n := len(s)
	mod := 1000000007
	dp := make([][]int, 0)
	for i := 0; i < n; i++ {
		dp = append(dp, make([]int, n))
		dp[i][i] = 1
	}

	for l := 2; l < n+1; l++ {
		for i := 0; i+l-1 < n; i++ {
			j := i + l - 1
			if s[i] == s[j] {
				ni, nj := i+1, j-1
				for ni < n && s[ni] != s[i] {
					ni++
				}
				for nj > 0 && s[nj] != s[j] {
					nj--
				}
				if ni == nj {
					dp[i][j] = 2*dp[i+1][j-1] + 1
				} else if ni > nj {
					dp[i][j] = 2*dp[i+1][j-1] + 2
				} else {
					dp[i][j] = 2*dp[i+1][j-1] - dp[ni+1][nj-1]
				}
			} else {
				dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]
			}
			dp[i][j] += mod
			dp[i][j] %= mod
		}
	}
	return dp[0][n-1]
}

func main() {
	s := "abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba"
	fmt.Printf("countPalindromicSubsequences(s): %v\n", countPalindromicSubsequences(s))
}
