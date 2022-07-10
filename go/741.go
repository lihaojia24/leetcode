package main

import (
	"fmt"
	"math"
)

var steps = [][]int{{0, 0}, {0, -1}, {-1, 0}, {-1, -1}}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func cherryPickup(grid [][]int) int {
	n := len(grid)
	dp := make([][]int, n)
	for i := 0; i < n; i++ {
		dp[i] = make([]int, n)
		for j := 0; j < n; j++ {
			dp[i][j] = math.MinInt
		}
	}
	stepN := 2 * (n - 1)
	dp[0][0] = grid[0][0]
	for k := 1; k <= stepN; k++ {
		for x1 := max(0, k-n+1); x1 <= k && x1 < n; x1++ {
			for x2 := max(0, k-n+1); x2 <= k && x2 < n; x2++ {
				y1, y2 := k-x1, k-x2
				if grid[x1][y1] == -1 || grid[x2][y2] == -1 {
					continue
				}
				for _, step := range steps {
					if x1+step[0] >= 0 && x2+step[1] >= 0 {
						dp[x1][x2] = max(dp[x1][x2], dp[x1+step[0]][x2+step[1]])
					}
				}
				dp[x1][x2] += grid[x1][y1]
				if x2 != x1 {
					dp[x1][x2] += grid[x2][y2]
				}
			}
		}
	}
	fmt.Printf("dp: %v\n", dp)
	return max(dp[n-1][n-1], 0)
}

func main() {

}
