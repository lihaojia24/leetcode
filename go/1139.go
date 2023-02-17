package main

func largest1BorderedSquare(grid [][]int) (ans int) {
	m, n := len(grid), len(grid[0])
	gridRow := make([][]int, m+1)
	gridCol := make([][]int, m+1)
	for i := range gridRow {
		gridRow[i] = make([]int, n+1)
		gridCol[i] = make([]int, n+1)
	}
	for i := 1; i <= m; i++ {
		for j := 1; j <= n; j++ {
			if grid[i-1][j-1] == 1 {
				gridRow[i][j] = gridRow[i][j-1] + 1
				gridCol[i][j] = gridCol[i-1][j] + 1
				//check
				border := min(gridRow[i][j], gridCol[i][j])
				for gridRow[i-border+1][j] < border || gridCol[i][j-border+1] < border {
					border--
				}
				ans = max(ans, border)
			}
		}
	}
	ans *= ans
	return
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}

func main() {

}
