package main

func sum(li []int) (ans int) {
	for _, v := range li {
		ans += v
	}
	return
}

func projectionArea(grid [][]int) int {
	rowLen := len(grid)
	colLen := len(grid[0])
	rowAns := make([]int, rowLen)
	colAns := make([]int, colLen)
	plainAns := 0
	for row := 0; row < rowLen; row++ {
		for col := 0; col < colLen; col++ {
			if grid[row][col] > 0 {
				plainAns++
			}
			rowAns[row] = max(rowAns[row], grid[row][col])
			colAns[col] = max(colAns[col], grid[row][col])
		}
	}
	return sum(rowAns) + sum(colAns) + plainAns
}
