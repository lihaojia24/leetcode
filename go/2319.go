package main

func checkXMatrix(grid [][]int) bool {
	l := len(grid)
	for i, row := range grid {
		for j, num := range row {
			if i == j || i+j == l-1 {
				if num == 0 {
					return false
				}
			} else {
				if num != 0 {
					return false
				}
			}
		}
	}
	return true
}
