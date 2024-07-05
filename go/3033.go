package main

func modifiedMatrix(matrix [][]int) [][]int {
	n := len(matrix[0])
	max_col := make([]int, n)
	for i := range matrix {
		for j := range matrix[0] {
			max_col[j] = max(matrix[i][j], max_col[j])
		}
	}
	for i := range matrix {
		for j := range matrix[0] {
			if matrix[i][j] == -1 {
				matrix[i][j] = max_col[j]
			}
		}
	}
	return matrix
}
