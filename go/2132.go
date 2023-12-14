package main

func possibleToStamp(grid [][]int, stampHeight int, stampWidth int) bool {
	m := len(grid)
	n := len(grid[0])
	preSum := make([][]int, m+1)
	for i := range preSum {
		preSum[i] = make([]int, n+1)
	}
	for i := 1; i < m+1; i++ {
		for j := 1; j < n+1; j++ {
			preSum[i][j] = grid[i-1][j-1] - preSum[i-1][j-1] + preSum[i-1][j] + preSum[i][j-1]
		}
	}
	diff := make([][]int, m+2)
	for i := range diff {
		diff[i] = make([]int, n+2)
	}
	for i := 1; i+stampHeight-1 < m+1; i++ {
		for j := 1; j+stampWidth-1 < n+1; j++ {
			x := i + stampHeight - 1
			y := j + stampWidth - 1
			if preSum[x][y]+preSum[i-1][j-1]-preSum[x][j-1]-preSum[i-1][y] == 0 {
				diff[i][j] += 1
				diff[x+1][y+1] += 1
				diff[i][y+1] -= 1
				diff[x+1][j] -= 1
			}
		}
	}
	for i := 1; i < m+1; i++ {
		for j := 1; j < n+1; j++ {
			diff[i][j] = diff[i][j] - diff[i-1][j-1] + diff[i-1][j] + diff[i][j-1]
			if grid[i-1][j-1] == 0 && diff[i][j] == 0 {
				return false
			}
		}
	}
	return true
}
