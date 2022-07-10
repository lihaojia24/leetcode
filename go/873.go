package main

import "fmt"

func max(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}

func lenLongestFibSubseq(arr []int) (ans int) {
	n := len(arr)
	m := map[int]int{}
	for i, v := range arr {
		m[v] = i
	}
	dp := make([][]int, n)
	for i := range dp {
		dp[i] = make([]int, n)
	}
	for i, num := range arr {
		for j := i - 1; j > 0; j-- {
			if num-arr[j] >= arr[j] {
				break
			}
			if idx, ok := m[num-arr[j]]; ok {
				dp[i][j] = max(dp[j][idx]+1, 3)
				ans = max(ans, dp[i][j])
			}
		}
	}
	return
}

func main() {
	arr := []int{1, 2, 3, 4, 5, 6, 7, 8}
	fmt.Printf("lenLongestFibSubseq(arr): %v\n", lenLongestFibSubseq(arr))
}
