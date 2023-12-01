package main

func firstCompleteIndex(arr []int, mat [][]int) int {
	rows := len(mat)
	cols := len(mat[0])
	n := len(arr)
	num2rows := make([]int, n+1)
	num2cols := make([]int, n+1)
	for row := 0; row < rows; row++ {
		for col := 0; col < cols; col++ {
			num2cols[mat[row][col]] = col
			num2rows[mat[row][col]] = row
		}
	}
	rowsF := make([]int, rows)
	colsF := make([]int, cols)
	for i, num := range arr {
		row := num2rows[num]
		col := num2cols[num]
		rowsF[row]++
		colsF[col]++
		if rowsF[row] == cols || colsF[col] == rows {
			return i
		}
	}
	return len(arr) - 1
}
